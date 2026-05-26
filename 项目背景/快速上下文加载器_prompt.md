---
status: prompt
type: prompt
task: context_loader
use_when: "每次开新会话，开始任何研究 / 阅读 / 写作 / 审阅任务之前"
do_not_use_when: "继续已经加载过上下文的同一会话"
input_required:
  - "填写下方所有 [填] 字段；越具体越好"
output: "LLM 用 5 个 bullet point 复述对你研究的理解，等你确认后才开始任务"
stop_points:
  - "复述输出后停下，等你确认理解准确"
quality_gates:
  - "不替你填空白字段；缺字段就标 [需核实]"
  - "不用模型记忆里'这个领域大概怎么样'补全"
related_prompts:
  - "../研究规划/01_子问题与章节方向规划_prompt"
---

# 快速上下文加载器

每次开新会话粘这一份。它的目标不是让 LLM 帮你做事，而是先让它**承认你的研究背景**，避免它用训练记忆填空。

## 复制给 LLM 的 prompt

```text
请先记住我的研究上下文。不要立刻开始任何任务，先按下面的字段读取，
然后用 5 个 bullet point 复述你对我研究的理解，等我确认后再开始。

## 我是谁

- 身份：[填，例如 硕士研究生 / taught postgraduate / research master]
- 学校与系：[填]
- 学科：[填，例如 媒体研究 / 社会学 / 计算机科学 / 教育学 / ...]
- 学位：[填，例如 MA / MSc / MRes]
- 导师：[填，仅称呼，不必真名]

## 我的论文

- 工作题目：[填，可以是 working title]
- 核心研究问题（RQ）：[填，1-2 句]
- 子问题（如有）：[填，每条一句]
- 论文类型：[填：dissertation / thesis / extended essay / capstone project]
- 字数 / 章节数 / 提交日期：[填]

## 方法论承诺

- 研究范式：[填，例如 positivist / interpretivist / critical / pragmatist / mixed]
- 主方法：[填，例如 questionnaire survey / semi-structured interview / 
  participant observation / discourse analysis / case study / 
  computational text analysis / experimental / RCT / systematic review / ...]
- 样本 / 语料 / 数据范围：[填，包括规模和边界]
- 已知限制：[填]

## 学科语境

- 我对话的学术共同体：[填，例如 media studies / educational policy 
  / HCI / cultural sociology / ...]
- 这个共同体关心什么 / 不关心什么：[填，如果你说得清]

## 当前阶段

- 我处于：[填，例如 proposal / 文献综述 / 数据收集 / 数据分析 / Methodology 写作 / 
  Results 写作 / Discussion 写作 / 修订 / 提交前]
- 已完成：[填]
- 卡住的地方：[填]

## 工作习惯

- 工作语言：[填，例如 中文（讨论）+ 英文（论文正文）]
- 我希望你：[填，例如 严苛 / 鼓励 / 直接给方案 / 先问问题]

## 约束

- 不要假设 [我的领域 / 我的方法] 一定是这样；以我说的为准。
- 不要用训练记忆里关于 [我学校 / 我导师 / 我学科] 的内容补全；如果我没说，标 [需核实]。
- 不要把 [我的方法] 写成它实际上不是的东西（例如不要把 thematic analysis 
  写成 quantitative content analysis）。

## 输出

请用 5 个 bullet point 复述：
1. 我的核心研究问题；
2. 我的方法论承诺；
3. 我对话的学术共同体；
4. 我目前处于哪个阶段；
5. 任何你觉得需要我确认才能继续的不确定项。

复述完后停下，等我说"准确"或"补充：xxx"，再开始任何任务。
```

## 使用习惯

- **每次开新会话粘一次**——LLM 没有跨会话记忆。
- **越具体越好**——"我做媒体研究"不如"我做 2010 年代中国短视频平台的用户实践研究，主方法是 60 个半结构化访谈 + 平台数据分析"。
- **不知道怎么填的字段**先空着，让 LLM 用 `[需核实]` 标出来，再去补。
- 把填好的版本存一份在你自己的笔记里，下次复制就行。

## 给纯英文论文用户

如果你只用英文写作，把上面的 prompt 整段翻译成英文也可以。结构不变。

## 给纯中文论文用户

把约束里的"工作语言"改成纯中文，把后续 prompt 里的双语要求改成纯中文即可。
