---
status: prompt
type: prompt
task: methodology_paragraph_drafting
use_when: "结构和证据已经确认，需要起草或重写 Methodology 的一个 section 或 2-3 个段落"
do_not_use_when: "还没有 section plan；或只是抽证据；或只是最终润色"
input_required:
  - "Methodology Section Plan"
  - "Methodology Evidence Pack"
  - "目标段落范围"
output: "英文段落 + 中文 gloss + evidence notes + unresolved items"
stop_points:
  - "每次只起草一个 section 或 2-3 段，完成后停下"
quality_gates:
  - "英文正文后紧接中文 gloss"
  - "不使用 banned words 和机械序列词"
  - "不声称未完成或未确认的结果"
  - "每个方法论 claim 都要能追溯到 evidence pack"
failure_modes:
  - "如果证据不足，用 [CITATION NEEDED] / [DETAIL NEEDED]，不要补写"
related_prompts:
  - "../通用工具/01_学术英文润色_prompt"
  - "../../审阅/03_Methodology审阅_prompt"
---

# Methodology 段落起草 prompt

## 复制给 LLM 的 prompt

```text
请根据已确认的 Methodology Section Plan 和 Evidence Pack 起草目标段落。
不要扩大范围；每次只写我指定的 section 或 2-3 个段落。

## 写作要求

- 英文段落在前，紧接 **中文：** 对照。
- 学术 precision 优先，不追求华丽表达。
- 不要使用：significant / crucial / robust / leverage / nuanced / delve /
  foundational / definitive / most cutting-edge / it is worth noting / importantly。
- 不要使用 firstly / secondly / thirdly，也不要用"首先、其次、再次"。
- 不要把工具能力 (tool capability) 写成已完成的结果 (completed analysis)。
- 不要把小样本 / pilot 写成 representative。

知识隔离：只依据 Evidence Pack 写。不要用你训练记忆里"这个领域 / 这篇文献
大概怎么说"来补全句子或加引用；一旦你想写的内容不在 Evidence Pack 里，
就停下标 [CITATION NEEDED] / [DETAIL NEEDED]，不要凭记忆写。

没有证据的地方写 [CITATION NEEDED] 或 [DETAIL NEEDED]。

## Methodology 写作微规则

- 描述过程用过去时（"I conducted X" / "data were coded using Y"），
  描述设计决策可以用现在时（"the framework assumes Z"）。
- 区分 "what I did" 和 "why I did it"——读者两者都需要。
- 工具名要带版本：例如 "NVivo 14" 而不是 "NVivo"；"GPT-4 (gpt-4-0125-preview)" 
  而不是 "GPT-4"。
- 参数要给值：阈值、学习率、抽样比例都要给具体数字。
- 时间要给范围：数据收集发生在什么时间窗内。
- 第三方决定要标主体：是研究者 / 参与者 / 工具自动？

## 输出

## Drafted Section

[English text]

**中文：**
[中文 gloss]

## Evidence Notes

| Sentence / claim | Evidence source | Status |
|---|---|---|

## Unresolved Items

- [CITATION NEEDED / DETAIL NEEDED / ADVISOR CONFIRMATION NEEDED]

输出后停下，问我是否进入方法论风险检查。

## 输入

Methodology Section Plan：
[粘贴]

Methodology Evidence Pack：
[粘贴]

目标段落范围：
[填]
```
