---
status: prompt
type: prompt
task: abstract_and_introduction_drafting
use_when: "需要起草或修订 thesis abstract、chapter introduction、conference abstract"
do_not_use_when: "正文段落起草 → 用对应章节 workflow；英文润色 → 用 01"
input_required:
  - "目标类型（thesis abstract / chapter intro / conference abstract / 自查）"
  - "已加载的项目背景（项目背景/快速上下文加载器_prompt）"
  - "可选：现有草稿"
output: "对应类型的英文正文 + 中文转述"
quality_gates:
  - "不声称还未完成的研究结果"
  - "不编造具体数字或引用"
  - "符合双语对照"
related_prompts:
  - "01_学术英文润色_prompt"
  - "../../审阅/01_通用学术审阅_prompt"
---

# 摘要与 Introduction 起草 prompt

不同场景使用不同版本。先选择对应版本再复制。

---

## 版本 A：Thesis Abstract

用于：硕士论文整体摘要（250-400 词）。

```text
请帮我起草或修订论文摘要（thesis abstract）。

## 任务类型

[选择：
- A. 全新起草（我没有任何草稿）
- B. 修订现有草稿（草稿见下方）
- C. 从我的章节摘要拼合成整体摘要]

## 摘要目标读者

[例如：thesis examiners / 课程教师 / 投稿评审]

## 摘要结构要求

请按以下逻辑结构输出，不要写成流水线介绍：

1. **Research problem & gap**（1-2 句）
   说明现有研究遗留了什么问题，为什么这个问题值得一篇论文。

2. **Research question**（1 句）
   精准表述核心研究问题。

3. **Data / Material / Case**（1-2 句）
   说明数据来源和范围，谨慎用词（"limited sample"、"exploratory" 等表述视情况保留）。

4. **Methodology**（2-3 句）
   说明研究设计的逻辑，区分方法步骤的认识论层级（如有）。

5. **Theoretical framework / 概念框架**（1-2 句）
   不要单独列出所有理论名称——只点最重要的支柱。

6. **Findings / Contribution**（1-2 句）
   说明本研究的发现或贡献；使用谨慎表达，不声称已证明什么。

## 写作约束

- 目标字数：[填，通常 250-400 词]
- 语言：英文正文 + **中文：** 完整中文对照
- 不要使用：foundational / definitive / robust / crucial / significant / 
  most cutting-edge / it is worth noting / importantly
- 不要声称已完成的研究结果。如果数据还在收集中，用 "aims to" / "proposes to" 表述
- 不要编造具体数字或引用
- 句式：长短交替，每句有明确主语

## 现有草稿（如有）

[粘贴现有摘要或章节摘要]

## 特别关注

[例如：评审关注 reproducibility；或需要强调跨学科贡献]
```

---

## 版本 B：章节 Introduction 起草

用于：Lit Review / Methodology / Results / Discussion / Conclusion 的开头 Introduction 节（500-800 词）。

```text
请帮我起草第 [章节号 / 名称] 章的 Introduction 节。

## 这个 Introduction 需要完成的功能

Chapter Introduction 不是摘要，不是目录，而是论证的开场。它需要：

1. **建立问题**：这一章为什么在这个位置？它解决什么问题？
2. **预告论证逻辑**：读者读完 Introduction 后应该知道这章"为什么这样组织"，
   而不只是"有什么内容"。
3. **连接上下文**：连接上一章结尾留下的问题；预告下一章。

## 任务

请为这个章节起草一个 Introduction 节：

- 500-700 词英文正文
- 紧接 **中文：** 完整中文对照
- 结构建议：
  1. 开头：直接进入问题（不要从"本章将会..."开始）
  2. 中间：说明论证路线，让读者知道为什么这样组织
  3. 结尾：1-2 句过渡到第一节

## 约束

- 不要写成章节目录的散文版（"Section 3.1 discusses... Section 3.2 then..."）
- 不要使用机械序列词（firstly / secondly / thirdly）
- 不要假设还没有完成的研究已经有结果
- 所有引用必须真实可核查；如果需要引用，标 [CITATION NEEDED: 描述]

## 特别说明

[填：目前 Introduction 存在什么问题，或有什么需要特别强调的论证节点]
```

---

## 版本 C：会议论文 / 投稿 Abstract

用于：学术会议、journal article、workshop submission。通常 250-350 词有硬限制。

```text
请帮我为以下会议起草投稿摘要。

## 目标会议

[填名称、年份]

## 会议要求

字数限制：[填]
是否需要关键词：[是 / 否]
格式要求：[例如 Word plain text / 无格式要求]

## 这篇摘要的定位

[从以下选择：
- 汇报方法进展（方法论为主）
- 汇报初步分析发现（结果为主）
- 理论贡献：[填什么贡献]
- 其他：填写]

## 摘要内容

请基于项目背景（已加载）起草，不要声称未完成的结果。

已有结果（如可以报告的初步发现）：
[填，或写"暂无可报告结果，以方法论贡献为主"]

## 结构

1. 背景与缺口（1-2 句）
2. 研究问题（1 句）
3. 数据与方法（2-3 句）
4. 贡献或初步发现（1-2 句）

## 约束

- 严格控制字数在 [字数] 以内；
- 不声称还未完成的研究结果；
- 英文为主；如果会议需要中文摘要，紧接输出；
- 允许 hedging，不堆砌技术术语。
```

---

## 版本 D：Abstract 对照自查（已有草稿时用）

把草稿发给 LLM 做快速检查，不要求重写。

```text
请对我的现有摘要做一次快速自查，不要重写，只指出需要修改的地方。

检查维度：
1. 研究问题是否清晰（能用一句话说出来）
2. 是否声称了还未完成的结果（用 aims to / proposes / demonstrates 区分）
3. 是否有夸大词汇（foundational / definitive / most / crucial）
4. 方法论描述是否精准（不要模糊"我用了什么"）
5. 字数是否在合理范围
6. 是否符合双语要求（英文 + 中文对照）

每个维度只输出：✓ 通过 / ✗ 问题：[一句话说明]

草稿：
[粘贴]
```
