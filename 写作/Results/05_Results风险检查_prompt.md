---
status: prompt
type: prompt
task: results_risk_check
use_when: "已有 Results 草稿，需要检查 over-claim / causal slip / 数据-叙事对齐"
do_not_use_when: "还没有草稿"
input_required:
  - "Results 草稿"
  - "Results Evidence Pack"
output: "Results Risk Register + revision priorities"
stop_points:
  - "风险输出后停下，等用户确认修订范围"
quality_gates:
  - "read-only：只诊断不重写"
  - "区分 writing issue / data issue / interpretation slip"
related_prompts:
  - "06_修订执行_prompt"
  - "../../审阅/04_Results审阅_prompt"
---

# Results 风险检查 prompt

## 复制给 LLM 的 prompt

```text
请检查 Results 草稿的风险。不要直接重写。任务是找出哪里需要改、为什么、
优先级如何。

## 检查维度

### A. Observation / Interpretation 边界
- 是否有 "data shows X means Y" 的 interpretation slip？
- 是否有因果动词（led to / caused / resulted in / explains / shaped）
  在没有因果识别的研究里出现？
- 是否把 association 写成 causation？
- 是否把单一个案 / 单一编码者结论说成 generalised pattern？

### B. 量化 over-claim
- "majority / most" 是否对应足够大的多数（>60%）？
- "significant" 是统计意义还是口语意义？混用了吗？
- effect size 是否报告，还是只报告 p value？
- 是否声称 "no effect" 但其实是 underpowered？

### C. 质性 over-claim
- 单一引述被说成 emergent theme？
- counter-evidence 是否被认真处理？
- 是否声称 saturation 但未说明如何判断？
- 是否暗示 generalisability 但研究本不支持？

### D. 数据-叙事对齐
- 正文提到的数字在 table 里能找到吗？
- table 里的列在正文里都解释了吗？
- figure caption 自含吗（读者不读正文也能看懂）？
- table 编号 / figure 编号顺序是否与正文出现顺序一致？

### E. 不确定性披露
- CI / p / SE / sample size 是否完整？
- missing data 怎么处理？是否说明？
- coder reliability / inter-rater agreement 是否报告（如适用）？
- 模型置信度 / 边界条件是否说明？

### F. 评审追问预判
- 一个外部审稿人最可能先问哪三个问题？
- 哪些段落的语言模糊到给追问留了切入口？

## 输出

## Results Risk Register

| Issue | Type | Severity | Sentence / location | Why it matters | Recommended action |
|---|---|---|---|---|---|
| ... | over-claim / interpretation slip / alignment / disclosure / writing | high / medium / low | ... | ... | revise / move to Discussion / add caveat / delete |

## Revision Priority

1. [最高]
2. ...

## Items to Move to Discussion

| Current location in Results | Reason it belongs in Discussion |
|---|---|

## Do Not Revise Yet

- [需要做额外分析 / 复核数据后才能改]

输出后停下，问我确认哪些进入修订执行。

## 输入

待检查草稿：
[粘贴或路径]

Results Evidence Pack：
[粘贴或路径]
```
