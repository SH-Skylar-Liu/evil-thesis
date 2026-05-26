---
status: prompt
type: prompt
task: conclusion_risk_check
use_when: "已有 Conclusion 草稿，要检查过度收束 / vague future work / contribution claim 失配"
do_not_use_when: "还没草稿"
input_required:
  - "Conclusion 草稿"
  - "Conclusion Synthesis Framework"
  - "可选：Discussion 草稿（用于核对 contribution / limitation 一致性）"
output: "Conclusion Risk Register + revision priorities"
stop_points:
  - "风险输出后停下，等用户确认"
quality_gates:
  - "read-only：只诊断不重写"
related_prompts:
  - "05_修订执行_prompt"
  - "../../审阅/06_Conclusion审阅_prompt"
---

# Conclusion 风险检查 prompt

## 复制给 LLM 的 prompt

```text
请检查 Conclusion 草稿的风险。不要直接重写。

## 检查维度

### A. RQ 回应直接性
- 每个 RQ 是否被直接回答（一句话能定位答案）？
- 回应是否使用了与 finding strength 匹配的 hedge？
- 是否绕开 RQ 谈泛泛 implications？

### B. 新增内容偷渡
- 是否有 finding 在 Results / Discussion 没出现过？
- 是否有 citation 在前文没出现过？
- 是否有新的解读没在 Discussion 里铺垫过？

### C. Contribution claim 失配
- theoretical / methodological / empirical 是否分清？
- 每条 contribution 是否能指回前文段落？
- 是否有 over-claim（example: "first study to demonstrate" 但其实只是 first 
  in narrow corpus）？
- 是否有 under-claim（你做了一件难事但没提出来）？

### D. Limitations 处理
- 关键 limitations 是否都被覆盖（即使在 Discussion 已处理）？
- 是否被写成 "future research could..." 套话？
- 是否说明每条 limitation 影响了哪个 claim？

### E. Future work 具体性
- 每条 future direction 是否能用一句话说出"做什么 + 用什么数据 + 期望解决什么"？
- 是否有 "more research is needed" / "could explore" 这种空话？
- future direction 是否与本研究的 limitation / gap / 意外发现真实相连？

### F. 结构与气质
- Conclusion 是否被写成长版 Abstract？
- 是否抄写 Methodology 段落？
- 收笔是否给读者一个 "so what" 而不是 "thank you for reading"？
- 整章是否在合理字数（硕士论文 1500-3000 词）？

### G. 评审追问预判
- 一个外部审稿人最可能先问哪两个 contribution claim 是否撑得起？
- 哪段 future work 让人觉得"你其实没想清楚下一步"？

## 输出

## Conclusion Risk Register

| Issue | Type | Severity | Sentence / location | Why it matters | Recommended action |
|---|---|---|---|---|---|
| ... | RQ-evasion / new-content / contribution-overclaim / vague-future / restatement | high / medium / low | ... | ... | revise / cut / specify / soften |

## Revision Priority

1. [最高]
2. ...

## Do Not Revise Yet

- [需要回 Discussion 补内容 / 重新评估 contribution 才能改]

输出后停下，问我确认哪些进入修订执行。

## 输入

Conclusion 草稿：
[粘贴或路径]

Conclusion Synthesis Framework：
[粘贴]

Discussion 草稿（可选）：
[路径]
```
