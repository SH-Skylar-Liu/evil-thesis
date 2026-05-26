---
status: prompt
type: prompt
task: reading_note_by_relevance
use_when: "已经拿到一篇 PDF 或全文，要让 LLM 按相关度（5★/4★/3★）选模板写一篇正式 reading note"
do_not_use_when: "还没读论文、要做检索 / 找新文献 / 批量整理已有笔记"
input_required:
  - "一篇可读全文（PDF / DOI / arXiv ID / 粘贴段落）"
  - "你对这篇文献相对论文的预判：可能高相关 / 中等相关，或让 LLM 自己判"
  - "Obsidian Vault 中 reading note 的保存目录（可选）"
output: "一篇按相关度分层模板生成的正式 reading note + Single Reading Report + Upgrade Candidate"
stop_points:
  - "判读 5★/4★ vs 3★ 后，先说明判定理由再继续写"
  - "如果实际相关度 ≤ 2★，先暂停问用户是否值得继续写长笔记"
  - "完成一篇后停下，不自动连读下一篇"
quality_gates:
  - "高相关（4-5★）方法 / 技术型论文，不允许压缩成短卡片；必须保留 workflow / key design / quotable lines / thesis use"
  - "3★ 论文不要为了显得学术写得晦涩；保留可调用信息即可"
  - "知识隔离：只依据眼前 PDF 文本，凭记忆得出的内容必须标 [来自记忆，需核实]"
  - "不虚构 DOI / 页码 / 引用 / 作者观点；不确定写 [需核实]"
  - "Quotable lines 必须是实际原文摘录，不要 paraphrase 当原文"
failure_modes:
  - "如果 PDF 不可读，先要求用户提供可读文件或文字版"
  - "如果只读了部分章节，必须在 frontmatter 标记 sections_read"
  - "对方法型 5★ 论文，如果省略 workflow / key design，视为不达标，需要重写"
related_prompts:
  - "01_直接阅读已下载文献_prompt"
  - "02_关键词检索下载评分阅读_prompt"
  - "07_批次整理_Codex_prompt"
---

# 单篇 reading note · 5★ / 4★ / 3★ 分层模板 prompt

这份 prompt 解决一个具体问题：**当 LLM 帮你读一篇论文时，不要把所有论文都压成同一种摘要卡**。

核心原则：

- **5★ / 4★ 高相关论文**用增强版精读笔记——可读性高、信息密度大、以后能直接拿来写
- **3★ 中等相关论文**用轻量版笔记——保留核心可调用信息，但不投入同样高的整理成本
- 这样可以避免高价值论文被压缩成无用短卡，也避免次要文献占用过多整理时间

这份 prompt 默认假设你已经有 PDF 或全文。如果你只有关键词，先用 `02_关键词检索下载评分阅读_prompt.md`。

## 复制给 LLM 的 prompt

```text
请按我的阅读工作流，为这篇论文生成一份正式 reading note。

## 任务边界

你只负责：
- 读这一篇论文
- 判断它对我项目的相关度
- 按相关度选对应模板写一份正式 reading note
- 给出 Single Reading Report 和 Upgrade Candidate

你不要：
- 不要更新 reading index
- 不要补任何已有笔记的 wikilinks
- 不要批量改 source note 的 status
- 不要自动连读下一篇
- 不要写没有实际读到的内容

## 保存位置

请把 reading note 保存到：
[你的 Obsidian 路径，例如 D:/MyVault/02_Reading_Notes/，或直接粘到对话即可]

## 第一步：相关度判断（必须先做，不可跳过）

请先用 3-5 行说明你判断这篇为几星，理由要具体：

- 5★：核心文献，直接支撑论文主线（理论 / 方法 / 材料 / 关键论证）
- 4★：高相关，可进入论证或方法框架，但不一定在主线
- 3★：中等相关，作为背景、对话、脚注级引用
- 2★ 及以下：只做简短说明，除非用户要求，不写长笔记

判断后停下一行问我："这个相关度判定是否同意？同意我就用对应模板继续。" 
然后按我的回复继续。

## 第二步：按相关度选模板

### A. 5★ / 4★ 高相关模板

frontmatter:

---
note_type: reading_note
paper_id:
authors:
year:
title:
journal_or_publisher:
volume_issue_pages:
doi:
url:
local_pdf:
field:
relevance: 4★/5★
status: read
sections_read: [实际读到的章节，如 Sections 1, 3-5, 7]
created: YYYY-MM-DD
tags: []
---

正文结构（默认保留这些部分；技术 / 方法型 4-5★ 论文不允许省略 Methodology / Key Design）：

# [论文标题]

## 核心信息 / Core Information
- Paper ID / Authors / Year / Journal / DOI / 本地 PDF 路径 / 字段

## 为什么与我的研究相关 / Why It Matters
用 1-2 段中文说清楚：服务于哪个理论问题、哪个方法问题、哪个材料 / 数据问题，或哪个文献综述缺口。
不要只写"相关"，要具体到能调用的层级。

## Abstract
### 英文原文
### 中文翻译
### 核心要点 / Key Points
- 3-5 条

## Methodology
### 整体流程（必保留）
text 框图或步骤
### 关键设计（必保留）
**设计1** — 解释为什么这样设计成立
**设计2**
### 图示
保留原文重要图表位置（用 ![图1|600](...) 占位）；如果原文有就保留，没有不强求

## 核心发现 / Key Findings
- 带出处位置（section / 页）
- 区分 "论文明确说的" vs "我的概括"

## 对我研究的启示 / Implications
分点写，每点说清楚怎么用

## 可引用原文 / Quotable Lines
> "实际原文摘录"
> 中文解释：

## Thesis Use / 如何用于我的论文
- 更偏：理论支撑 / 方法支撑 / 案例比较 / 局限性参照 / 反面例子
- 最可能进入哪一章 / 哪一节
- 不该被拿来证明什么（防过度引用）

## 与既有文献的对话 / Dialogue
- [[Note A]] —— 一句话说关系（一致 / 张力 / 分歧）
- [[Note B]] ——
（重点标分歧，不要只写一致）

## 局限性 / Limitations

## 相关论文 / Related Papers
### 直接相关
### 方法论相关

## 我的综合评价 / Evaluation
**X/10** — 一句话总结

| 评分维度 | 分数 | 理由 |
|---|---|---|
| 创新性 | | |
| 技术质量 | | |
| 理论价值 | | |
| 可迁移性 | | |

## 我的笔记 / Personal Notes
%% 自己补充 %%

**值得深入的问题：**
- 

## Upgrade Candidate
- candidate_type: stay / argument_block / concept / method
- confidence: low / medium / high
- reason:

---

### B. 3★ 中等相关模板

frontmatter 同上（relevance 改 3★）。

正文压缩为：

# [论文标题]

## 核心信息

## 为什么相关 / Why It Matters
3-5 句中文：相关在哪、相关度大概多少、它更像背景 / 方法参照 / 补充材料中的哪种。

## Abstract
### 英文原文
### 中文翻译
### 核心要点

## Methodology
- 数据：
- 方法：
- 关键设计：

## 核心发现

## 我怎么用它 / How I Might Use It
- 最可能支持：
- 最可能对话到：
- 不要过度引用它来证明：

## 局限

## 我的简评
- relevance: 3★
- value:
- 是否值得 revisit:

## Upgrade Candidate
- candidate_type:
- confidence:
- reason:

3★ 模板可以省略：详细流程图、多张图表、详细评分矩阵、大量 related papers、大量 personal notes、大量 quotable lines。

## 第三步：固定尾部输出（无论几星都要写）

写完笔记后，在对话末尾固定输出：

## Single Reading Report
completed: [[文件名]]
dialogue: [[文献A]], [[文献B]]
unsure: none / [需要我确认的事项]

## Upgrade Candidate
candidate_type: stay / argument_block / concept / method
confidence: low / medium / high
reason: [一句话]

## 写作规范

- 学术实质性内容默认双语：英文段在前，紧接 **中文：** 精准转述（不是泛泛翻译）
- 对话和解释部分可以中文为主
- 不要为了显得"学术"而写晦涩
- 不要把高相关方法论文强行压缩成只有 core claim / method / limitation / relevance 的短卡
- 不虚构 DOI / 页码 / 引用 / 作者观点
- 知识隔离：只依据眼前文本；凭记忆得出的内容标 [来自记忆，需核实]
- 只读了部分章节时，必须在 sections_read 字段记录实际范围
- citation 必须可核查；不确定的用 hedging（"appears to argue", "suggests", "may"）
- 不用夸大评价词（"foundational"、"definitive"、"groundbreaking"）

## 输入

文献路径 / PDF / DOI / arXiv ID：
[在这里填]

我对它的相关度预判（可选）：
[5★ / 4★ / 3★ / 让你判]

特别关注（可选）：
[例如：methodology, theoretical framework, specific concept]
```

## 配套模板

本 prompt 引用的两套结构在：

- `模板/TPL_Reading_Note_5星4星.md` —— 增强版
- `模板/TPL_Reading_Note_3星.md` —— 轻量版

你可以把模板挂到 Obsidian Templater 上，让 LLM 写完后你一键套结构。

## 4-5★ 技术型论文的额外护栏

如果论文同时满足：

- 4★ / 5★ 高相关
- 偏技术 / 方法 / 模型 / pipeline
- 你以后会把它当方法支撑反复调用

那么 **必须** 保留：

- 整体流程（不只是笼统写 method）
- 关键设计（说明为什么这个方法成立）
- 原文重要图表的位置
- Quotable Lines（实际原文，不是 paraphrase）
- Thesis Use

不要为了"更学术"把这类笔记重写成更难懂的摘要卡。这条护栏是为了保证笔记**以后重新打开就能直接用**。
