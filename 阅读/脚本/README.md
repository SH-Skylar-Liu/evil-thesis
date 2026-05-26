# 脚本 · Literature Search Scripts

两个轻量 Python 脚本，把"调 API"这一步从 LLM 手里拿出来——避免 LLM 凭记忆瞎报文献。

| 脚本 | 用途 | API |
|---|---|---|
| `search_semantic_scholar.py` | 跨学科主检索（人文 / 社科 / 跨领域） | Semantic Scholar Graph API |
| `search_arxiv.py` | CV / NLP / ML / 数学 / 物理预印本 | arXiv API |

两个脚本都输出**统一格式的 JSON**，你可以直接把 JSON 喂给 LLM 让它做后续筛选 / 评分 / 写候选表。

## 安装

```bash
# 进入脚本目录
cd D:/GitHub/evil-thesis/阅读/脚本   # 或你 fork 后的路径

# 装依赖
pip install -r requirements.txt
```

依赖很少：`requests` + `PyYAML`，没有 numpy / pandas / 等重依赖。

## 三种用法

### 用法 1 · 单 query 快速跑

```bash
python search_semantic_scholar.py --query "distant viewing multimodal" --limit 10
```

stdout 会打印简表。要保存完整 JSON：

```bash
python search_semantic_scholar.py --query "..." --out candidates.json
```

### 用法 2 · 多 query 批量跑

```bash
python search_semantic_scholar.py \
  --query "distant viewing multimodal" \
  --query "computational visual humanities" \
  --query "AI-generated metadata archives" \
  --out candidates.json
```

每个 `--query` 是一组，结果会去重合并。

### 用法 3 · 从 config 跑（推荐）

复制 `config.example.yaml` 为 `config.yaml`，按你的研究改 `keyword_groups`：

```yaml
keyword_groups:
  facet_concept_method:
    description: "概念-方法对"
    queries:
      - '"distant viewing" "vision-language model"'
      - '"distant viewing" "multimodal"'
    apis:
      - semantic_scholar
      - arxiv
```

然后:

```bash
python search_semantic_scholar.py --config config.yaml --out candidates.json
python search_arxiv.py            --config config.yaml --out arxiv.json
```

config 里 `apis:` 字段决定一组关键词走哪些 API；`search_arxiv.py` 会自动只跑 `apis: arxiv` 的组。

## Semantic Scholar API key

不设也能跑（限速约 1 req/s）。如果你要批量检索：

1. 免费申请：https://www.semanticscholar.org/product/api#api-key （邮件审核，几天内回复）
2. 拿到 key 后任选一种方式：

```bash
# 方式 A: 命令行
python search_semantic_scholar.py --query "..." --api-key YOUR_KEY

# 方式 B: 环境变量（推荐）
export S2_API_KEY=YOUR_KEY                  # macOS / Linux
$env:S2_API_KEY = "YOUR_KEY"                # Windows PowerShell
python search_semantic_scholar.py --query "..."

# 方式 C: 写进 config.yaml
# semantic_scholar_api_key: "YOUR_KEY"
```

优先级：CLI > env var > config 文件。

## 速率与限流

| API | 无 key | 有 key | 脚本默认 |
|---|---|---|---|
| Semantic Scholar | ~1 req/s（429 频繁） | 5000 req / 5min | `--pause 1.5` 秒 / query |
| arXiv | 建议 ≥ 3 秒 / query | 同左 | `--delay 3.0` 秒 / query |

如果遇到 429：
- Semantic Scholar 脚本会自动指数退避重试 4 次；超过就跳过该 query 继续
- arXiv 不重试——直接放慢 `--delay`

## 输出 JSON 格式

两个脚本输出**同一套字段**（差异字段会留空 / null），方便 LLM 统一处理：

```json
[
  {
    "source_api": "semantic_scholar",
    "source_query": "distant viewing multimodal",
    "title": "...",
    "authors": ["...", "..."],
    "year": 2024,
    "venue": "Digital Scholarship in the Humanities",
    "doi": "10.1093/llc/...",
    "arxiv_id": null,
    "s2_paper_id": "...",
    "citation_count": 12,
    "influential_citation_count": 3,
    "abstract": "...",
    "open_pdf_url": "https://...",
    "url": "https://www.semanticscholar.org/..."
  }
]
```

arXiv 输出多两个字段：`primary_category` 和 `published`。

## 把 JSON 喂给 LLM 做筛选

跑完检索拿到 `candidates.json`，把它贴给 LLM 用这个 prompt：

```text
下面是我刚从 Semantic Scholar / arXiv 拉到的候选文献 JSON。
请按 evil-thesis/阅读/06_Semantic_Scholar_arXiv_检索协议.md 的评分维度，
帮我把它们筛成一张候选表：

| # | 标题 | 作者-年 | DOI/arXiv | 引用数 | 开放 PDF | 相关性(0-3) | 来源质量(0-3) | 引用密度(0-3) | 新近性(0-3) | 一句话相关度判断 |

不要：
- 不要凭记忆补不在 JSON 里的字段
- 不要伪造引用数 / 摘要
- 不要直接说"已读过这篇"——还没读

JSON 如下:
[paste candidates.json]
```

LLM 只做评分和语义判断，不调 API、不补文献——这是分工的核心。

## 与 evilread 原 skill 的差异

[juliye2025/evil-read-arxiv](https://github.com/juliye2025/evil-read-arxiv) 的 `start-my-day` 脚本默认每日推荐，把检索 / 评分 / 笔记生成全部串成一个自动流水线。

这两个脚本只做**最薄的一层**——拉 JSON，剩下交给 LLM + 你判断：

- 不做自动每日推荐（用户说不需要）
- 不做综合评分加权（让 LLM 给每维度独立打分，最终次序由你决定）
- 不直接生成笔记（笔记生成走 `04_单篇reading_note_5星4星3星_prompt.md`）
- 不写 Obsidian 文件（脚本只输出 JSON / stdout，不动 Vault）

这样设计是为了把"调 API"和"判断 / 写作"分开，每段都可以单独审查。

## 故障速查

| 问题 | 检查 |
|---|---|
| `ModuleNotFoundError: requests` | `pip install -r requirements.txt` |
| `[warn] PyYAML not installed` | `pip install PyYAML`（如果要用 --config） |
| 大量 429 | 申请 S2_API_KEY；或加大 `--pause` |
| arXiv 返回空 | 检查 query 语法：用 `ti:`/`abs:`/`au:`/`cat:` 前缀；中文标题不支持 |
| 中文 query 报错 | 确保终端编码为 UTF-8；Windows PowerShell 用 `chcp 65001` |

## 不做什么

明确**不实现**的功能（按需绕开 LLM 幻觉风险）：

- ❌ 自动下载 PDF —— 你自己决定哪些下载
- ❌ 自动写 reading note —— 走 prompt 04
- ❌ 自动更新 Obsidian 笔记 —— 走 prompt 07
- ❌ 综合推荐评分（一行得到 Top N）—— 评分维度交给 LLM + 你
- ❌ Google Scholar 抓取 —— 违反 ToS，且 LLM 容易把抓取结果当成 API 结果

如果你需要其中某个功能，参考 `D:/evilread/` 或 [juliye2025/evil-read-arxiv](https://github.com/juliye2025/evil-read-arxiv) 的原版 skill。
