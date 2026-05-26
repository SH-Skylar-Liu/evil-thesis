"""
arXiv 检索脚本 · evil-thesis 阅读子模块

用法:
    python search_arxiv.py --query "distant viewing multimodal" --max 10
    python search_arxiv.py --query 'ti:"vision-language" AND abs:"archive"' --max 20
    python search_arxiv.py --config config.yaml --out arxiv_candidates.json

支持的字段前缀（参考 https://arxiv.org/help/api/user-manual）:
    ti:    title
    abs:   abstract
    au:    author
    cat:   subject category (e.g. cs.CV, cs.LG)
    all:   all fields
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any
from urllib.parse import quote_plus

import requests

try:
    import yaml
except ImportError:
    yaml = None

ARXIV_ENDPOINT = "http://export.arxiv.org/api/query"
ATOM_NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "arxiv": "http://arxiv.org/schemas/atom",
}


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
    max_results: int,
    sort_by: str,
    sort_order: str,
) -> list[dict[str, Any]]:
    params = (
        f"search_query={quote_plus(query)}"
        f"&max_results={max_results}"
        f"&sortBy={sort_by}"
        f"&sortOrder={sort_order}"
    )
    url = f"{ARXIV_ENDPOINT}?{params}"
    headers = {"User-Agent": "evil-thesis-reader/1.0"}

    resp = requests.get(url, headers=headers, timeout=30)
    if resp.status_code != 200:
        print(f"[error] HTTP {resp.status_code}: {resp.text[:200]}", file=sys.stderr)
        return []

    return parse_atom(resp.text, source_query=query)


def parse_atom(xml_text: str, source_query: str) -> list[dict[str, Any]]:
    root = ET.fromstring(xml_text)
    entries = root.findall("atom:entry", ATOM_NS)
    papers: list[dict[str, Any]] = []
    for entry in entries:
        title_el = entry.find("atom:title", ATOM_NS)
        summary_el = entry.find("atom:summary", ATOM_NS)
        published_el = entry.find("atom:published", ATOM_NS)
        id_el = entry.find("atom:id", ATOM_NS)

        title = (title_el.text or "").strip() if title_el is not None else ""
        summary = (summary_el.text or "").strip() if summary_el is not None else ""
        published = published_el.text if published_el is not None else None
        arxiv_url = id_el.text if id_el is not None else None
        arxiv_id = arxiv_url.rsplit("/", 1)[-1] if arxiv_url else None

        authors = [
            (a.find("atom:name", ATOM_NS).text or "").strip()
            for a in entry.findall("atom:author", ATOM_NS)
            if a.find("atom:name", ATOM_NS) is not None
        ]

        pdf_url = None
        for link in entry.findall("atom:link", ATOM_NS):
            if link.get("type") == "application/pdf":
                pdf_url = link.get("href")
                break

        primary_cat_el = entry.find("arxiv:primary_category", ATOM_NS)
        primary_cat = primary_cat_el.get("term") if primary_cat_el is not None else None

        papers.append(
            {
                "source_api": "arxiv",
                "source_query": source_query,
                "title": title,
                "authors": authors,
                "year": int(published[:4]) if published else None,
                "venue": "arXiv preprint",
                "doi": None,
                "arxiv_id": arxiv_id,
                "primary_category": primary_cat,
                "abstract": summary,
                "open_pdf_url": pdf_url,
                "url": arxiv_url,
                "published": published,
            }
        )
    return papers


def dedupe(papers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    for p in papers:
        key = p.get("arxiv_id") or p.get("title", "")
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
        cat = p.get("primary_category") or "—"
        aid = p.get("arxiv_id") or "—"
        title = p.get("title", "")[:90].replace("\n", " ")
        print(f"  {i:2d}. [{year}] {title}")
        print(f"      {authors} | {cat} | arXiv:{aid}")


def run(
    queries: list[str],
    max_results: int,
    sort_by: str,
    sort_order: str,
    delay: float,
) -> list[dict[str, Any]]:
    all_papers: list[dict[str, Any]] = []
    for q in queries:
        print(f"[query] {q}", file=sys.stderr)
        results = search_once(q, max_results=max_results, sort_by=sort_by, sort_order=sort_order)
        all_papers.extend(results)
        if delay > 0 and q != queries[-1]:
            time.sleep(delay)
    return dedupe(all_papers)


def main() -> int:
    parser = argparse.ArgumentParser(description="Search arXiv (evil-thesis reader)")
    parser.add_argument("--query", action="append", help="arXiv query (repeatable)")
    parser.add_argument("--config", type=Path, help="config.yaml with keyword_groups")
    parser.add_argument("--out", type=Path, help="Output JSON path")
    parser.add_argument("--max", type=int, default=10, dest="max_results")
    parser.add_argument(
        "--sort-by",
        default="submittedDate",
        choices=["relevance", "lastUpdatedDate", "submittedDate"],
    )
    parser.add_argument(
        "--sort-order",
        default="descending",
        choices=["ascending", "descending"],
    )
    parser.add_argument("--delay", type=float, default=3.0, help="Seconds between queries (>=3 recommended)")
    args = parser.parse_args()

    config = load_config(args.config)

    queries: list[str] = []
    if args.query:
        queries.extend(args.query)
    if not queries and config:
        groups = config.get("keyword_groups", {}) or {}
        for group in groups.values():
            apis = (group or {}).get("apis", []) or []
            if "arxiv" not in apis:
                continue
            qs = (group or {}).get("queries", []) or []
            queries.extend(qs)

    if not queries:
        parser.error("provide --query (repeatable) or --config with keyword_groups (apis: arxiv)")

    arxiv_cfg = config.get("arxiv", {}) if config else {}
    max_results = args.max_results or arxiv_cfg.get("max_results", 10)
    sort_by = args.sort_by or arxiv_cfg.get("sort_by", "submittedDate")
    sort_order = args.sort_order or arxiv_cfg.get("sort_order", "descending")
    delay = args.delay if args.delay is not None else arxiv_cfg.get("request_delay_seconds", 3.0)

    papers = run(
        queries=queries,
        max_results=max_results,
        sort_by=sort_by,
        sort_order=sort_order,
        delay=delay,
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
