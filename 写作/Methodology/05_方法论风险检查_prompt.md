---
status: prompt
type: prompt
task: methodology_risk_check
use_when: "已有 Methodology section 草稿，需要检查方法论风险、证据风险和评审追问风险"
do_not_use_when: "还没有草稿；或只需要普通语法润色"
input_required:
  - "Methodology 草稿或目标 section"
  - "Methodology Evidence Pack"
output: "Risk Register + revision priorities + confirmed fixes"
stop_points:
  - "输出风险和修改优先级后停下，等用户确认哪些要修"
quality_gates:
  - "必须区分 writing issue / evidence issue / method design issue"
  - "不能直接重写，除非用户确认修订范围"
failure_modes:
  - "如果证据包缺失，先要求补 evidence pack"
related_prompts:
  - "06_修订执行_prompt"
  - "../../审阅/07_论点压力测试_prompt"
  - "../../审阅/09_再审与回归追踪_prompt"
---

# Methodology 方法论风险检查 prompt

## 复制给 LLM 的 prompt

```text
请检查这段 Methodology 草稿的方法论风险。不要直接重写。你的任务是找出
哪些地方需要修、为什么、优先级如何。

## 检查维度（Methodology 通用）

### Research design coherence
- 范式 → RQ → 方法 → 数据，这条链是否一以贯之？
- 有没有方法选择技术上合理但理论上脱节？
- 是否存在"研究范式说 A，但分析步骤其实是 B"的矛盾？

### Sampling / Case selection
- 抽样 / 选案逻辑是否说清楚？
- 是否区分 sampling frame / sample / case / population？
- 是否有 inclusion / exclusion criteria？
- 样本量 / 案例数的合理性是否得到说明？

### Data collection
- 工具版本、协议、时间、地点、设备、提示词（如适用）是否齐全？
- 知情同意 / 招募 / 补偿 / 退出机制是否说明？
- 是否存在 self-reporting bias / observer effect 但未承认？

### Analysis procedure
- 步骤是否可被另一研究者复现？
- 编码 / 模型 / 统计方法是否带名字、版本、参数？
- coder reliability / inter-rater agreement / robustness check 是否需要？
- 如有 AI / LLM 辅助：prompt、模型版本、温度、抽查规则是否透明？

### Validity / Trustworthiness
- 对应研究范式的判据是否齐全（quantitative: validity / reliability；
  qualitative: credibility / transferability / dependability / confirmability；
  mixed: integration logic）？
- 是否声称了无法支撑的判据（例如纯小样本质性研究声称 generalisability）？

### Ethics
- 伦理审查是否提到？
- 数据保护 / 匿名化 / 存储 / 删除是否说明？
- 涉及弱势群体 / 敏感主题时，是否有额外保护？

### Limitations preview
- 是否预告关键限制？还是把它们藏到 Conclusion？
- limitation 是否被错误地写成 design choice（或反之）？

### Claim 与证据匹配
- 每个 claim 是否能追溯到 reading notes、data notes、pipeline docs 或确认事实？
- 是否有 over-claim？是否 under-claim（你做了但没说）？

### 评审追问预判
- 一个外部审稿人最可能先问哪三个问题？
- 哪些段落的语言模糊到给追问留了切入口？

## 输出

## Methodology Risk Register

| Issue | Type | Severity | Evidence | Why it matters | Recommended action |
|---|---|---|---|---|---|
| ... | writing / evidence / method design / advisor confirmation | high / medium / low | sentence / source | ... | revise / cite / ask / defer |

## Revision Priority

1. [最高优先级]
2. [...]

## Do Not Revise Yet

- [列出需要导师确认后才能改的内容]

输出后停下，问我确认哪些问题进入修订执行。

## 输入

待检查草稿：
[粘贴或路径]

Methodology Evidence Pack：
[粘贴或路径]
```
