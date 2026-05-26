---
status: prompt
type: prompt
task: paper_conference_topic_planning
use_when: "我有一个小论文、会议摘要、workshop 或 journal article 想法，想判断是否值得发展并规划投稿"
do_not_use_when: "只是 thesis 章节内部子问题（用 01）；已经进入正式摘要写作（用 写作/通用工具/02）；想法太模糊到说不出问题（先用 01 的 Socratic 引导）"
input_required:
  - "一个论文 / 会议 / 期刊 / workshop 想法，或一个初步选题"
  - "可选：目标会议 / 期刊 / CFP 原文或链接"
  - "可选：字数、截止日期、主题范围"
output: "Topic Viability Brief + 2-3 个 framing 比较 + 投稿计划骨架 + 阅读路线"
stop_points:
  - "比较 2-3 个 framing 后停下，等用户选择"
  - "用户选定 framing 后先做 Devil's Advocate 审查"
  - "用户确认前不写入文件"
quality_gates:
  - "不把 thesis 的全部问题塞进一篇小论文"
  - "不承诺投稿适配，除非用户提供 call for papers"
  - "材料隔离：区分 ①用户确认存在的 ②从用户材料读到的 ③模型推测；第③类标注 [需核实]"
  - "反谄媚：framing 评分必须有据；选题弱或挤占 thesis 时间就直说 defer/drop"
related_prompts:
  - "01_子问题与章节方向规划_prompt"
  - "../写作/通用工具/02_摘要与Introduction起草_prompt"
---

# 论文与会议选题规划 prompt

这份 prompt 用于把一个论文项目内部的想法，转成一个可投稿的小论文、会议摘要或 workshop paper：判断它是否值得独立成篇、用哪个 framing、和 thesis 是什么关系、以及如何排投稿计划。

## 复制给 LLM 的 prompt

```text
请帮我判断这个小论文 / 会议选题是否值得发展，并在我确认后给出投稿计划。
不要直接写摘要，先做选题可行性评估。

## 材料优先与隔离原则（全程适用）

规划时优先使用我提供的真实材料（CFP 原文、导师意见、results、reading notes、
文件路径）。请明确区分三类信息：
- ① 我确认存在的；
- ② 你从我材料里读到 / 推断出的；
- ③ 你基于领域常识的推测。

第 ③ 类必须显式标注 [需核实]。涉及 CFP 要求、领域共识、已有研究、
导师意图时，宁可标注不确定，也不要编造。

## 任务边界

你只负责：
1. 澄清选题空间；
2. 生成 2-3 个候选 framing；
3. 比较它们的可投稿性、贡献、与 thesis 的关系、风险；
4. 停下等我选择；
5. 我选定后先做 Devil's Advocate；我看过反论仍确认时，
   再输出投稿计划骨架。

你不要：
- 不要直接起草正式摘要；
- 不要假设某个 venue 适配，除非我贴出 CFP；
- 不要把 thesis 的全部问题塞进一篇小论文；
- 不要编造 CFP 要求、领域共识、已有研究或导师意见。

## Mode 判定

- 如果我的想法已成形（能说出一个大致问题或贡献）→ 进入阶段一；
- 如果我的想法太模糊（只有兴趣、说不出问题）→ 不要硬凑 framing，
  建议我先用 研究规划/01_子问题与章节方向规划_prompt 的 Socratic 引导，
  把问题想清楚再回到这里。

## 阶段一：选题空间澄清

| 维度 | 判断 |
|---|---|
| 产出类型 | conference abstract / workshop paper / journal article / book chapter / 不确定 |
| 目标受众 | [由用户领域决定] |
| 与 thesis 的关系 | feeds a chapter（直接喂养某章）/ spinoff（衍生但不阻塞）/ tangent（偏离主线） |
| 时间约束 | 有明确 deadline / 滚动征稿 / 无 |
| 是否有 CFP | 有（我会贴出）/ 无 |
| 已有材料 | 数据 / 文献 / 草稿 / 无 |

如有 CFP，请先核读 CFP 的：主题范围、字数限制、截止日期、是否双盲、
评审标准。不在 CFP 里看到的，不要假设。

## 阶段二：生成 2-3 个候选 framing

每个 framing 用这个格式：

## Candidate Framing [A/B/C]

- working title:
- one-sentence pitch:
- core contribution claim:
- methods to leverage:
- materials to use:
- relation to thesis: feeds chapter X / spinoff / tangent
- venue fit（如有 CFP，对照其主题范围）:
- estimated effort to first draft（hours / weeks）:
- estimated effort to submission:
- FINER + 投稿专属评分（各 1-5）:
  - Feasible（在 deadline 前能完成）:
  - Interesting（学术共同体是否在意）:
  - Novel（真贡献还是仅有趣）:
  - Ethical（数据 / 知情同意 / 致谢）:
  - Relevant（venue 的匹配度，如无 CFP 标 [需核实]）:
  - Material-ready（材料是否已就位）:
  - Thesis-synergy（与论文进度的协同性）:
- priority: high / medium / low / defer / drop

priority 推导规则：
- high: 多数评分高 + 与 thesis synergy 强；
- defer: Material-ready 低或 Feasible 低，但选题本身有价值，建议下个 venue；
- drop: Thesis-synergy 极低又挤占主线写作时间，或方法论硬伤。

## 阶段三：比较表

| Framing | 核心贡献 | venue fit | 与 thesis 协同 | 最大风险 | 建议 |
|---|---|---|---|---|---|

## 阶段四：停下

输出后必须停下，问我："你想选哪个 framing？也可以让我合并或缩小范围。"
不要自动进入投稿计划。

## 阶段四点五：Devil's Advocate

我选定 framing 后，切换对抗视角：

1. 最强反论（150-250 字）：这个 framing 最可能被拒、被批评、或事后后悔的理由是什么？
2. 风险分级：CRITICAL / MAJOR / MINOR。
3. 替代 framing 或一个更优 angle。
4. drop 条件：什么情况下应直接放弃投这个 venue。

反谄媚：选题挤占 thesis 时间就直说 defer/drop，不为礼貌保留。

## 阶段五：投稿计划骨架（我看过反论仍确认时输出）

## Submission Plan

- chosen framing:
- target venue + deadline:
- word / page limit:
- core claim (one sentence):
- structure outline:
- materials needed (已有 / 缺):
- reading still needed:
- co-author / advisor sign-off needed:
- backup venue（如这次被拒去哪）:
- 倒排时间线（按周）:
  - W -8: ...
  - W -6: ...
  - W -4: ...
  - W -2: ...
  - deadline: 提交
- next prompt to use（写作/通用工具/02 起草摘要 / 阅读/02 找文献）:

## 输入

我的想法或初步选题：
[填]

目标 venue / CFP（如有）：
[粘贴或链接]

时间约束：
[填]
```
