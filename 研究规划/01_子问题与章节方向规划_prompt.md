---
status: prompt
type: prompt
task: research_subquestion_planning
use_when: "我有一个章节方向、导师反馈、方法困惑、文献综述缺口或模糊想法，想先判断它能不能变成可研究的子问题"
do_not_use_when: "已经确定要读某篇文献；已经有明确关键词只需要找文献"
input_required:
  - "一个模糊想法、章节问题、导师反馈、审稿意见片段或方法困惑"
  - "可选：关联章节，如 Lit Review / Methodology / Discussion"
  - "可选：当前已有材料或相关文件路径"
output: "Research Planning Brief + 候选研究方向 + 阅读路线 + 下一步 prompt 推荐"
stop_points:
  - "Mode 0 Socratic 引导每轮只问 2-3 个问题后停下，等用户回应"
  - "输出 2-4 个候选 research directions 后停下，等用户选择"
  - "用户选定方向后先做 Devil's Advocate 审查，再停下确认是否出 Brief"
  - "用户确认方向前，不生成正式阅读清单"
  - "用户确认保存前，不写入任何文件"
quality_gates:
  - "不把模糊兴趣直接包装成已成立的 research gap"
  - "不编造已有文献或导师意图"
  - "材料隔离：区分 ①用户确认存在的 ②从用户材料读到的 ③模型推测；第③类必须标注 [需核实]"
  - "反谄媚：FINER 与 priority 评分必须有据，不为取悦用户抬高；方向弱就直说 drop"
  - "每个方向都必须说明和论文核心研究问题的关系"
failure_modes:
  - "如果输入太模糊，进入 Mode 0 Socratic 引导，不要直接生成方向"
  - "如果 Socratic 引导超过 8 轮仍未收敛，停止追问，直接给 3 个候选 RQ 让用户选"
  - "如果输入太宽，先收窄到一个章节或一个方法问题"
related_prompts:
  - "../项目背景/快速上下文加载器_prompt"
  - "../阅读/00_阅读_INDEX"
---

# 子问题与章节方向规划 prompt

这份 prompt 用于把一个模糊研究想法转成可判断、可阅读、可写作的子问题。在 routing、checkpoint、brief 之外，吸收了 Socratic 引导、Devil's Advocate 对抗审查、FINER 评分与材料隔离四种机制（思路借鉴 `academic-research-skills` by Cheng-I Wu, CC-BY-NC 4.0）。

## 复制给 LLM 的 prompt

```text
请按照我的研究规划流程执行。你的任务不是立刻找文献，也不是替我决定研究方向，
而是先把一个模糊想法变成几个可比较的研究方向，然后停下来让我选择。

## 任务边界

你只负责：
1. 澄清问题空间；
2. 生成 2-4 个候选 research directions；
3. 比较它们的可研究性、风险和与论文主问题的关系；
4. 停下等我选择；
5. 我选定后，先做 Devil's Advocate 对抗审查；我看过反论仍确认时，
   再生成 Research Planning Brief 和阅读路线。

你不要：
- 不要直接开始搜索文献；
- 不要直接写 reading note；
- 不要把一个有趣想法包装成已经成立的 research gap；
- 不要编造 citation、导师意见、领域共识或已有研究。

## 材料优先与隔离原则（全程适用）

规划时优先使用我提供的真实材料（导师原话、章节草稿、reading notes、文件路径）。
请明确区分三类信息，并在输出中始终保持可分辨：
- ① 我确认存在的（我直接说过、或我提供的文件里有）；
- ② 你从我材料里读到 / 推断出的；
- ③ 你基于领域常识的推测。

第 ③ 类必须显式标注 [需核实]，灰色地带不得当成已知事实。涉及具体文献、
导师意图、领域共识时，宁可标注不确定，也不要编造。

## Mode 判定（先做这一步）

先判断我的输入处于哪种状态，再选路径：
- 【模糊】我只有兴趣或困惑，说不出一个可回答的问题 → 进入 Mode 0 Socratic 引导；
- 【半成形】我已有方向，只是不确定可研究性或如何收窄 → 直接进入阶段一。

歧义时默认 Mode 0：先引导比直接产出更安全。

## Mode 0: Socratic 引导（仅在【模糊】时）

铁律：在这一模式里你绝不直接给答案、绝不替我下结论、绝不抛诱导性问题
（即预设了想要答案的问题）。你只能问真问题，每轮最多 2-3 个，按这五层
逐步推进，每问完一轮就停下等我回应：

1. 澄清：我说的这个概念 / 现象，到底指什么？边界在哪？
2. 审问假设：这个想法预设了什么？哪个预设最脆弱？
3. 证据 / 推理：凭什么这值得研究？现在有什么支撑、什么只是直觉？
4. 视角：不同学科共同体会各自怎么看这个问题？我想站在哪一边、或如何对话？
5. 影响：如果答案是 X，对我的论文主问题和章节意味着什么？

退出条件：
- 当我们收敛到一个可比较的问题空间（能说清问题类型、所属章节、
  与论文主问题的关系）时，停止提问，进入阶段一；
- 若超过 8 轮仍未收敛，不要继续追问，直接给我 3 个候选 research question
  让我挑，并说明各自的取舍。

## 阶段一：问题空间澄清

请先把我的输入拆成以下维度：

| 维度 | 判断 |
|---|---|
| 触发来源 | 导师反馈 / 审稿意见 / 章节困惑 / 方法问题 / 文献综述缺口 / 新想法 |
| 所属章节 | Lit Review / Methodology / Results / Discussion / Conclusion / uncertain |
| 问题类型 | theoretical / methodological / empirical / writing-structure |
| 与论文核心问题的关系 | direct / indirect / weak |
| 当前是否适合推进 | yes / maybe / no |
| 需要先确认的材料 | 文件路径、导师原话、章节草稿、已有 reading notes 等 |

如果输入太宽，请先提出最多 3 个澄清问题，不要继续生成方向。

## 阶段二：生成候选 research directions

请给出 2-4 个候选方向。每个方向必须使用这个格式：

## Candidate Direction [A/B/C]

- working title:
- one-sentence question:
- what it would help me understand:
- relation to thesis core question:
- likely chapter use:
- theoretical dependency:
- methodological dependency:
- material / data dependency:
- likely evidence needed:
- risk:
- why not overclaim:
- FINER 评分（各 1-5，每项附一句理由）:
  - Feasible（现有材料 / 我的时间 / 方法成熟度是否支撑）:
  - Interesting（学术共同体是否在意）:
  - Novel（是真 gap 还是我没读够；不确定就标 [需核实]）:
  - Ethical（伦理审查 / 数据保护 / 知情同意 / 文化再现风险）:
  - Relevant（与论文核心问题: direct / indirect / weak）:
  - Material-ready（是否已有数据或 reading notes 可直接动手）:
- priority（必须由上面评分推导，不得凭感觉）: high / medium / low

评估规则（priority 必须与 FINER 一致）：
- high: FINER 普遍偏高且 Relevant=direct，直接服务当前章节，能导出明确阅读路线；
- medium: 有潜力，但 Feasible 或 Material-ready 偏低，需要更多材料；
- low: 有趣但 Relevant=weak 或有方法论硬伤，偏离当前主轴，暂不投入；
- 任何一项 FINER 出现致命短板（如 Ethical 不可解、Feasible=1），
  即使其他项高，也不得给 high。

## 阶段三：比较表

| 方向 | 适合解决的问题 | 与论文关系 | FINER 总分 | 阅读成本 | 写作收益 | 最大风险 | 建议 |
|---|---|---|---|---|---|---|---|
| A | ... | direct/indirect/weak | x/30 | low/medium/high | low/medium/high | ... | pursue / hold / drop |

## 阶段四：停下来

候选方向和比较表输出后必须停下，问我：
"你想选择哪个方向继续？也可以让我合并两个方向，或把某个方向压缩成一个更小的 reading task。"

不要自动进入文献搜索或 reading route。

## 阶段四点五：Devil's Advocate 审查（我选定方向后、出 Brief 之前必做）

我选定方向后，先不要急着出 Brief。请切换到对抗视角，专门攻击我刚选的方向：

1. 最强反论（150-250 字）：这个方向最可能失败、或最不值得做的理由是什么？
2. 风险分级：逐条列出 CRITICAL / MAJOR / MINOR。
3. 被我忽略的替代解释，或一个比我现在更优的 framing。
4. drop 条件：一句话说明——在什么条件下我应该直接放弃这个方向。

反谄媚铁律：
- 不要为了让我满意而抬高评价；所有判断必须有据。
- 一个有方法论硬伤的方向，Relevant 再高也不能给 high priority。
- 如果方向本身弱，直接说 drop，不要勉强保留；不要连续两轮都软化立场。

审查输出后停下，问我："在看过这些反论后，你想继续这个方向、换一个、还是把它缩小？"

## 阶段五：确认后输出 Research Planning Brief

我在看过 Devil's Advocate 反论后仍然确认方向时，请输出：

## Research Planning Brief

- planning question:
- chosen direction:
- why this matters:
- relation to thesis core question:
- likely chapter use:
- reading route:
- candidate keywords:
- must-read literature types:
- optional adjacent fields:
- expected argument:
- risks / assumptions（含 Devil's Advocate 提出但尚未消解的风险，及我打算如何应对）:
- next prompt to use:

`next prompt to use` 只能从以下选择：
- 阅读/02_关键词检索下载评分阅读_prompt: 还没有具体文献
- 阅读/03_根据反馈找Gap并补文献_prompt: 方向来自导师/审稿意见
- 阅读/01_直接阅读已下载文献_prompt: 已经确定具体 PDF

## 输入

我的模糊想法 / 章节问题 / 导师反馈：
[在这里填]

关联章节或文件路径：
[可选]

我现在最担心的是：
[可选：例如方向太大、文献不够、方法论不自洽、和论文主问题关系不清]
```
