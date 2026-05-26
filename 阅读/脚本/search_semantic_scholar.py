"""
Semantic Scholar 检索脚本 · evil-thesis 阅读子模块

用法:
    python search_semantic_scholar.py --query "distant viewing multimodal" --limit 10
    python search_semantic_scholar.py --config config.yaml --out candidates.json
    python search_semantic_scholar.py --query "..." --api-key <key>

输出: JSON 文件 + stdout 简表。把 JSON 喂给 LLM 做后续筛选 / 评分。
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path
from typing import Any

import requests

try:
    import yaml
except ImportError:
    yaml = None

S2_SEARCH_ENDPOINT = "https://api.semanticscholar.org/graph/v1/paper/search"
DEFAULT_FIELDS = [
    "title",
    "authors",
    "year",
    "venue",
    "abstract",
    "citationCount",
    "influentialCitationCount",
    "externalIds",
    "openAccessPdf",
    "url",
]


def load_config(config_path: Path | None) -> dict[str, Any]:
    if config_path is None or not config_path.exists():
        return {}
    if yaml is None:
        print("[warn] PyYAML not installed; ignoring config file", file=sys.stderr)
        return {}
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def search_once(
    query: str,
    api_key: str | None,
    limit: int,
    fields: list[str],
    max_retries: int = 4,
) -> list[dict[str, Any]]:
    headers = {"User-Agent": "evil-thesis-reader/1.0"}
    if api_key:
        headers["x-api-key"] = api_key

    params = {
        "query": query,
        "limit": limit,
        "fields": ",".join(fields),
    }

    delay = 1.5
    for attempt in range(max_retries):
        resp = requests.get(S2_SEARCH_ENDPOINT, headers=headers, params=params, timeout=30)
        if resp.status_code == 200:
            data = resp.json()
            return data.get("data", []) or []
        if resp.status_code in (429, 503):
            print(f"[retry] HTTP {resp.status_code} — backing off {delay:.1f}s", file=sys.stderr)
            time.sleep(delay)
            delay *= 2
            continue
        print(f"[error] HTTP {resp.status_code}: {resp.text[:200]}", file=sys.stderr)
        return []

    print(f"[error] exceeded max retries for query: {query}", file=sys.stderr)
    return []


def normalize_paper(paper: dict[str, Any], source_query: str) -> dict[str, Any]:
    authors = paper.get("authors") or []
    author_names = [a.get("name", "") for a in authors if isinstance(a, dict)]
    external = paper.get("externalIds") or {}
    open_pdf = paper.get("openAccessPdf") or {}
    return {
        "source_api": "semantic_scholar",
        "source_query": source_query,
        "title": paper.get("title", ""),
        "authors": author_names,
        "year": paper.get("year"),
        "venue": paper.get("venue", ""),
        "doi": external.get("DOI"),
        "arxiv_id": external.get("ArXiv"),
        "s2_paper_id": paper.get("paperId"),
        "citation_count": paper.get("citationCount"),
        "influential_citation_count": paper.get("influentialCitationCount"),
        "abstract": paper.get("abstract", ""),
        "open_pdf_url": open_pdf.get("url"),
        "url": paper.get("url", ""),
    }


def dedupe(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for p in papers:
        key = p.get("doi") or p.get("s2_paper_id") or (p.get("title", "") + str(p.get("year", "")))
        if key in seen:
            continue
        seen.add(key)
        out.append(p)
    return out


def print_summary(papers: list[dict[str, Any]]) -> None:
    if not papers:
        print("[result] no papers found")
        return
    print(f"\n[result] {len(papers)} unique paper(s):\n")
    for i, p in enumerate(papers, 1):
        authors = ", ".join(p.get("authors", [])[:3])
        if len(p.get("authors", [])) > 3:
            authors += " et al."
        year = p.get("year") or "?"
        citations = p.get("citation_count") or 0
        infl = p.get("influential_citation_count") or 0
        pdf = "PDF" if p.get("open_pdf_url") else "—"
        title = p.get("title", "")[:90]
        print(f"  {i:2d}. [{year}] {title}")
        print(f"      {authors} | cites={citations} (infl={infl}) | {pdf}")


def run(
    queries: list[str],
    api_key: str | None,
    limit: int,
    fields: list[str],
    pause_between_queries: float,
) -> list[dict[str, Any]]:
    all_papers: list[dict[str, Any]] = []
    for q in queries:
        print(f"[query] {q}", file=sys.stderr)
        results = search_once(q, api_key=api_key, limit=limit, fields=fields)
        for paper in results:
            all_papers.append(normalize_paper(paper, source_query=q))
        if pause_between_queries > 0 and q != queries[-1]:
            time.sleep(pause_between_queries)
    return dedupe(all_papers)


def main() -> int:
    parser = argparse.ArgumentParser(description="Search Semantic Scholar (evil-thesis reader)")
    parser.add_argument("--query", action="append", help="Single query (repeatable)")
    parser.add_argument("--config", type=Path, help="config.yaml with keyword_groups")
    parser.add_argument("--out", type=Path, help="Output JSON path")
    parser.add_argument("--limit", type=int, default=10, help="Results per query (max 100)")
    parser.add_argument("--api-key", type=str, help="Semantic Scholar API key (or set S2_API_KEY env)")
    parser.add_argument(
        "--pause",
        type=float,
        default=1.5,
        help="Seconds to wait between queries (default 1.5; raise if you hit 429)",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    api_key = (
        args.api_key
        or os.environ.get("S2_API_KEY")
        or config.get("semantic_scholar_api_key")
    )

    queries: list[str] = []
    if args.query:
        queries.extend(args.query)
    if not queries and config:
        groups = config.get("keyword_groups", {}) or {}
        for group in groups.values():
            qs = (group or {}).get("queries", []) or []
            queries.extend(qs)

    if not queries:
        parser.error("provide --query (repeatable) or --config with keyword_groups")

    fields = DEFAULT_FIELDS
    limit = args.limit
    if config:
        s2_cfg = config.get("semantic_scholar", {}) or {}
        fields = s2_cfg.get("fields", DEFAULT_FIELDS)
        limit = args.limit or s2_cfg.get("limit", 10)

    papers = run(
        queries=queries,
        api_key=api_key,
        limit=limit,
        fields=fields,
        pause_between_queries=args.pause,
    )

    print_summary(papers)

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(
            json.dumps(papers, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"\n[saved] {len(papers)} papers → {args.out}")
    elif papers:
        print("\n[hint] use --out candidates.json to save full results", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
