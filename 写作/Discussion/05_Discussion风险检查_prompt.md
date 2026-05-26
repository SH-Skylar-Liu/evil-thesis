---
status: prompt
type: prompt
task: discussion_risk_check
use_when: "已有 Discussion 草稿，要检查 over-interpretation / 重复 Results / 伪对话 / limitation 处理"
do_not_use_when: "还没有草稿"
input_required:
  - "Discussion 草稿"
  - "Results 草稿（用于核查重复）"
  - "Discussion Evidence Pack"
output: "Discussion Risk Register + revision priorities"
stop_points:
  - "风险输出后停下，等用户确认修订范围"
quality_gates:
  - "read-only：只诊断不重写"
related_prompts:
  - "06_修订执行_prompt"
  - "../../审阅/05_Discussion审阅_prompt"
  - "../../审阅/07_论点压力测试_prompt"
---

# Discussion 风险检查 prompt

## 复制给 LLM 的 prompt

```text
请检查 Discussion 草稿的风险。不要直接重写。

## 检查维度

### A. 与 Results 的关系
- 是否有段落实际上是 Results 的复读（同样数字 / 同样描述）？
- 是否有应在 Results 但写在 Discussion 的内容（描述性细节）？
- 是否有应在 Discussion 但写在 Results 的内容（解读 / 文献对话）？

### B. 与文献的对话
- 每个 citation 是否带具体 stance（支持 / 延伸 / 修正 / 反驳 / 桥接 / 揭示 gap）？
- 是否有 "see also Smith 2021" 类型的 vague reference 占位？
- 是否回避了反驳自己 findings 的文献？
- 引用是否真存在（如果对照 reading notes 找不到，标 [来自记忆，需核实]）？

### C. Over-interpretation
- 因果动词（causes / leads to / explains / determines）是否在没有因果识别的
  地方出现？
- 局部 finding 是否被升级为 broad theoretical claim？
- 是否声称 generalisability 但研究设计本不支持？
- 是否使用 prove / demonstrate / establish 这类一锤定音词？

### D. Rival interpretations
- 每个主要解读是否考虑过 reasonable rival？
- counter-evidence 是否被认真处理？
- 如果只有一种解读，是真的没有 rival 还是没认真想？

### E. Limitations
- limitations 是否存在？还是被略掉？
- 每条 limitation 是否说明它影响了什么 claim？
- 是否区分 "design choice with trade-offs" 和 "real shortcoming"？
- 是否把 limitation 写成 generic 套话（"future research could explore..." 
  没说原因）？

### F. Implications
- theoretical / methodological / practical / policy 是否分清？
- "implications for practice" 一节是不是实际上是 future work？
- implication 是否撑得起 finding 的强度，还是过度延伸？

### G. 评审追问预判
- 一个外部审稿人最可能先问哪三个问题？
- 哪段语言模糊到给追问留切入口？

## 输出

## Discussion Risk Register

| Issue | Type | Severity | Sentence / location | Why it matters | Recommended action |
|---|---|---|---|---|---|
| ... | restatement / vague citation / over-interpretation / missing rival / limitation gap / writing | high / medium / low | ... | ... | revise / add caveat / engage rival / move to Results or Conclusion |

## Revision Priority

1. [最高]
2. ...

## Items to Move

| From Discussion to ... | Sentence | Reason |
|---|---|---|

## Do Not Revise Yet

- [需要新读文献 / 重新分析才能改]

输出后停下，问我确认哪些进入修订执行。

## 输入

Discussion 草稿：
[粘贴或路径]

Results 草稿（用于核查重复）：
[粘贴或路径]

Discussion Evidence Pack：
[粘贴]
```
