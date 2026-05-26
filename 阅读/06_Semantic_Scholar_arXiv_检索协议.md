---
status: protocol
type: api_protocol
task: literature_search_via_api
use_when: "需要用真实 API（Semantic Scholar / arXiv / Crossref）检索文献，避免让 LLM 凭记忆瞎报文献"
do_not_use_when: "已经有 PDF 想直接读（用 01 或 04）；只想拆关键词（用 05）"
input_required:
  - "一组具体的关键词组合（建议先用 05 生成）"
  - "可选：Semantic Scholar API key（无 key 也可用，但速率限制更严）"
output: "一份候选文献表，每条带 DOI / arXiv ID / 开放 PDF 链接 / 引用数 / 摘要"
stop_points:
  - "候选表生成后必须停下，由用户挑哪些下载并精读"
quality_gates:
  - "每条候选必须在 Semantic Scholar / arXiv / Crossref 至少一个库实际命中；命中不到的标 [未核实，可能不存在]"
  - "不要把搜索结果当成已经阅读过的文献"
  - "不要补不存在的 DOI 或 PDF 链接"
  - "不要绕过 paywall 下载 PDF；非开放访问就只记录 DOI / 出版社链接"
failure_modes:
  - "API 速率限制：429 错误时退避重试，不要换关键词假装继续"
  - "网络失败：直接告诉用户，不要伪造结果"
  - "命中数过大（>200）：先停下问用户要不要加更窄的 filter"
related_prompts:
  - "05_关键词组合自动生成_prompt"
  - "02_关键词检索下载评分阅读_prompt"
---

# Semantic Scholar / arXiv 检索协议

这份文件是一份**操作规范**而不是 prompt——它定义了在 `evil-thesis/阅读/` 工作流里，怎么用真实 API 检索文献，以及怎么把检索结果交还给 LLM 做后续筛选。

它有两种用法：

1. **作为 prompt 引用**：把本文件粘给 LLM，让 LLM 按协议直接调 web tool / API（如果你的 LLM 有联网工具）
2. **作为 Python 脚本依据**：照本文件的字段定义跑 `脚本/search_semantic_scholar.py` 和 `脚本/search_arxiv.py`，得到 JSON 后交给 LLM

两种用法都不允许 LLM 凭记忆"补文献"。

## 三个主要 API 的分工

| API | 主要用途 | 不适合 |
|---|---|---|
| **Semantic Scholar Graph API** | 跨学科主检索：人文 / 社会科学 / 跨领域；引用关系；开放 PDF 链接 | 太新的论文（< 30 天） |
| **arXiv API** | 计算机 / 物理 / 数学 / 统计的预印本；CV / NLP / ML 论文 | 人文社科为主的论文 |
| **Crossref API** | DOI / 期刊 / 卷期页码核查；不做主检索 | 主题检索（噪音大） |

辅助：

- **WebSearch / WebFetch**（如果 LLM 有联网工具）：用于找开放 PDF、出版社页面、Google Scholar 风格线索
- **OpenAlex**：Semantic Scholar 的替代，社科覆盖更全

## Semantic Scholar Graph API · 核心调用

### Endpoint

```
GET https://api.semanticscholar.org/graph/v1/paper/search
```

### 推荐参数

```
query: "你的关键词组合"
fields: title,authors,year,venue,abstract,citationCount,influentialCitationCount,externalIds,openAccessPdf,url
limit: 10  # 默认 10，最大 100
offset: 0
```

### 字段说明

| 字段 | 含义 | 用途 |
|---|---|---|
| `title` | 标题 | 候选表必备 |
| `authors` | 作者列表 | 候选表必备 |
| `year` | 出版年 | 评分维度 |
| `venue` | 期刊 / 会议 | 来源质量分级 |
| `abstract` | 摘要 | 相关度判断 |
| `citationCount` | 总引用数 | 热门度评分 |
| `influentialCitationCount` | 高影响引用数 | 质量评分（比 citationCount 更稳） |
| `externalIds` | DOI / arXiv ID 等外部 ID | 下载入口 |
| `openAccessPdf` | 开放 PDF 链接 | 下载入口 |
| `url` | Semantic Scholar 页面 | 跳转入口 |

### 速率限制

- 无 API key：约 1 req/s，容易 429
- 有 API key：5000 req / 5 分钟，足够个人研究使用
- 申请：https://www.semanticscholar.org/product/api#api-key （免费，邮件审核）

### 注意

- 不要在 URL 里直接传未编码的中文 / 特殊字符；用 `urllib.parse.quote_plus`
- `externalIds` 里的 `arXiv` 字段才是 arXiv ID，`DOI` 才是 DOI——不要把 Semantic Scholar 的 `paperId` 当 DOI

## arXiv API · 核心调用

### Endpoint

```
GET http://export.arxiv.org/api/query
```

### 推荐参数

```
search_query: ti:"keyword1" AND abs:"keyword2"   # 标题 + 摘要
sortBy: submittedDate
sortOrder: descending
max_results: 20
```

### 字段
返回 Atom XML（不是 JSON），需要解析 `<entry>` 节点：

- `title` — 论文标题
- `summary` — 摘要
- `author/name` — 作者
- `published` — 提交日期
- `link[@type="application/pdf"]/@href` — PDF 链接
- `arxiv:primary_category` — 主分类（如 `cs.CV`）

### 注意

- arXiv API 速率限制：建议 3 秒 / 请求，不要密集查询
- 用 `--` 当作日期范围分隔符：`submittedDate:[202401010000+TO+202412312359]`
- 主分类速查：cs.AI / cs.LG / cs.CL / cs.CV / cs.MM / cs.MA / cs.RO

## Crossref API · 核对 DOI

### 用途

只用于核查 DOI / 卷期页码，不做主检索。

### Endpoint

```
GET https://api.crossref.org/works/{DOI}
GET https://api.crossref.org/works?query.bibliographic={fuzzy_title}
```

### 注意

- Crossref 的 `query.bibliographic` 适合校核 DOI（"我有题目，DOI 对不对得上"），不适合主题检索
- User-Agent 必须设置（如 `User-Agent: evilread/1.0 (mailto:you@example.com)`），否则可能限速

## 一次完整检索的 prompt 框架

如果你要把这个协议作为 prompt 给 LLM 用（让它直接调 web tool），可以套这个框架：

```text
请按 evil-thesis/阅读/06_Semantic_Scholar_arXiv_检索协议.md 的规范检索文献。

## 输入
关键词组合：
[从 05 得到的关键词表里挑出来]

## 检索路径
按下列顺序执行：

1. Semantic Scholar Graph API：用关键词组合的前 5 组
   - endpoint: https://api.semanticscholar.org/graph/v1/paper/search
   - fields: title,authors,year,venue,abstract,citationCount,influentialCitationCount,externalIds,openAccessPdf,url
   - limit: 10 / 组

2. arXiv API（如果有 CV / NLP / ML 相关关键词）
   - endpoint: http://export.arxiv.org/api/query
   - sortBy: submittedDate, descending
   - max_results: 10

3. WebSearch 补充：每组关键词 + "filetype:pdf" 找开放 PDF

## 输出

一份候选表，最多 20 条：

| # | 来源 API | 标题 | 作者-年 | venue | DOI/arXiv ID | 引用数 | 开放 PDF | 关键词组合 | 一句话相关度判断 |

每条必须满足：
- DOI 或 arXiv ID 至少有一个（否则标 [未核实，可能不存在]）
- 摘要直接来自 API（不要 paraphrase）
- 不要补不存在的链接

## 停下点

候选表生成后停下，等我挑选：
- 哪些值得下载 PDF
- 哪些直接进入 reading（用 04 prompt）
- 哪些只记录 DOI / link 暂不读
```

## 评分维度（候选筛选时用）

参考 `02_关键词检索下载评分阅读_prompt.md` 的评分体系，但核心维度：

| 维度 | 权重 | 说明 |
|---|---|---|
| 相关性 | 40% | 标题 + 摘要与关键词的匹配；与你具体 gap 的契合度 |
| 来源质量 | 20% | venue / publisher 学术地位；预印本 < 期刊 < 顶级期刊 |
| 引用密度 | 20% | influentialCitationCount 优于 citationCount |
| 新近性 | 10% | 看具体领域；理论文献新旧无关，方法文献近 3 年更稳 |
| 可获取性 | 10% | 有开放 PDF > 仅 DOI > 仅 landing page |

不要让 LLM 自己加权——让它给每条候选打四个维度分数（0-3），由你决定最终顺序。

## 三种"假命中"的识别

LLM 在帮你做检索时常出现三种假命中，要警惕：

1. **凭记忆补文献**：LLM 直接告诉你"这个领域有 Foucault 1972、Said 1978..."却没真去查 API
   - 反制：要求每条候选必须带 Semantic Scholar URL 或 DOI；没有就标 [未核实，可能不存在]

2. **paraphrase 摘要**：LLM 重写了摘要伪装成原文
   - 反制：要求 abstract 字段直接来自 API 返回，不允许改写

3. **混淆作者 / 年份**：LLM 把两位同名作者或两年混在一起
   - 反制：开放 PDF 链接 + Crossref 反查双重确认

## 与脚本层的关系

如果你不想让 LLM 自己调 API（怕速率限制 / 怕幻觉），可以走脚本层：

1. 跑 `脚本/search_semantic_scholar.py --query "..." --out candidates.json`
2. 把 `candidates.json` 贴给 LLM
3. LLM 只负责筛选 / 评分 / 写候选表

脚本层把"调 API"这一步固定下来，LLM 只做语义判断。详细见 `脚本/README.md`。
