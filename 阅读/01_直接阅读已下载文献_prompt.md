---
status: prompt
type: prompt
task: reading_workflow
use_when: "需要让 LLM 阅读一篇文献并生成正式 reading note"
do_not_use_when: "需要审稿、补文献搜索、批量维护链接或更新索引"
input_required:
  - "PDF 路径 / Zotero key / DOI / 文献题名"
  - "可选：特别关注点，如 methodology / theory / specific concept"
output: "一篇正式 reading note + 本次阅读报告 + 后续升级建议"
stop_points:
  - "相关度判断后，如果低于 3★ 且用户期待精读，应先说明是否值得继续"
  - "每读完一篇后停下，不自动读下一篇"
quality_gates:
  - "只写实际读到的内容"
  - "不虚构 DOI、页码、引用或作者观点"
  - "知识隔离：只依据眼前 PDF 文本，不用训练记忆补全；凭记忆得出的内容标 [来自记忆，需核实]"
  - "核心发现尽量带出处位置（section/页），区分'论文明确说的'与'我的概括'"
  - "不把 annotation 当成 interpretation"
failure_modes:
  - "如果 PDF 无法读取，先要求用户提供可读文件或 Zotero 路径"
  - "如果只读了部分章节，必须记录 sections_read"
related_prompts:
  - "02_关键词检索下载评分阅读_prompt"
  - "03_根据反馈找Gap并补文献_prompt"
---

# 直接阅读已下载文献 prompt

这份 prompt 只做一件事：**让 LLM 读一篇文献，并生成一篇正式 reading note**。

它不负责审稿，不负责找新文献，不负责更新 index，也不负责维护笔记库链接。这样可以避免 LLM 一边读文献一边乱改库结构。

## 复制给 LLM 的 prompt

```text
请按照我的阅读工作流，阅读这一篇文献，并生成正式 reading note。

## 任务边界

你只负责：
- 阅读这一篇文献；
- 生成一份正式 reading note；
- 判断它和哪些已读文献对话；
- 给出一个轻量的后续升级建议。

你不要：
- 不要更新 reading index；
- 不要补任何已有文件的链接；
- 不要自动连续读下一篇；
- 不要写没有实际读到的内容。

## 保存位置

请把 reading note 保存到我指定的目录：
[填，例如 D:/Notes/Reading_Notes/，或粘到对话即可]

## 读前判断

请先判断这篇文献对我的论文有多相关：

- 5★：核心文献，直接支撑理论、方法或材料论证；
- 4★：高相关，可以进入核心论证或方法框架；
- 3★：中等相关，可作为背景、对话或脚注级引用；
- 2★ 以下：只做简短说明，除非我要求，不写长笔记。

判断后选择对应模板。

## 4★ / 5★ 高相关模板

---
note_type: reading_note
paper_id:
authors:
year:
title:
journal_or_publisher:
doi:
url:
local_pdf:
relevance: 4★/5★
status: read
created: YYYY-MM-DD
tags:
---

# [论文标题]

## 基本信息

作者、年份、题名、期刊/出版社、DOI、PDF 路径。

## 为什么与我的研究相关

不要只说"相关"。请具体说明它服务于：
- 哪个理论问题；
- 哪个方法问题；
- 哪个材料 / 数据 / 案例问题；
- 或哪个文献综述缺口。

## 摘要

### English

### 中文

## 核心观点

## 方法或论证结构

如果是技术或方法论文，请保留 workflow、pipeline、数据、模型、评估方式、限制条件。
不要压缩成普通摘要卡。

## 关键发现

## 可引用原文

只引用实际读到的原文。尽量带页码；没有页码时说明来源位置。

## 可以怎样用于我的论文

必须说明：
1. 它可以用于论文的哪个章节；
2. 它提供什么论证功能；
3. 它不适合用在哪里，避免过度引用；
4. 是否需要进一步核查 citation。

## 与已有文献的对话

列出它和哪些已有 reading notes 对话，用一句话说明关系；尤其标出分歧 / 张力，
不要只写一致之处。

## 局限

## 我的简评

- relevance:
- value:
- revisit:

## 本次阅读报告

completed: [[文件名]]
dialogue: [[文献A]], [[文献B]]
unsure:

## 后续升级建议

candidate_type: stay / argument / concept / method / core_source / background
confidence: low / medium / high
reason:

## 3★ 中等相关模板

如果这篇文献只是 3★，请压缩为：

- 基本信息
- 为什么相关
- 摘要
- 核心观点
- 方法或论证结构
- 我可能怎样使用它
- 局限
- 我的简评
- 本次阅读报告
- 后续升级建议

## 写作规范

- 默认中文说明；
- 重要学术概念可以英文在前，随后中文解释；
- 不要为了显得学术而写得晦涩；
- 不要虚构 DOI、页码、引用、作者观点；
- 知识隔离：只依据眼前文本，不用记忆里"这篇大概讲什么"补全；
  凭记忆而非文本得出的，标 [来自记忆，需核实]；
- 核心发现尽量标注出处位置（section / 页），并区分"论文明确说的"与"我的概括"；
- 不确定时明确写"不确定"；
- 如果只读了部分章节，必须说明实际阅读范围。

## 输入

文献路径 / Zotero key / PDF：
[在这里填]

特别关注：
[可选：例如 methodology / theory / specific concept]
```
