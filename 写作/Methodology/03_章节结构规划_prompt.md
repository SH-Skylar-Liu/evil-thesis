---
status: prompt
type: prompt
task: methodology_section_structure
use_when: "已有目标 section 和证据包，需要规划 Methodology 结构、section order 或段落顺序"
do_not_use_when: "还没有 evidence pack；或只是语言润色"
input_required:
  - "Methodology Writing Configuration"
  - "Methodology Evidence Pack 或现有草稿"
output: "Section Plan + paragraph sequence + claim/evidence placement"
stop_points:
  - "结构方案输出后停下，等用户确认再起草"
quality_gates:
  - "结构必须解释为什么这样组织，而不是章节目录散文化"
  - "方法步骤间的转换必须有逻辑理由"
  - "不能把缺证据的 claim 放进核心段落"
failure_modes:
  - "如果证据包不足，回到 02_证据包生成_prompt"
related_prompts:
  - "../../审阅/03_Methodology审阅_prompt"
---

# Methodology 章节结构规划 prompt

## 复制给 LLM 的 prompt

```text
请为 Methodology 章节的目标 section 规划结构。不要起草完整正文。
你可以写 topic sentences 和段落功能，但不要展开成长段落。

## 输出

## Methodology Section Plan

- target section:
- section function:
- reader problem this section must solve:
- relation to previous section:
- relation to next section:

## Paragraph Sequence

| Paragraph | Function | Topic sentence draft | Evidence to use | Risk to avoid |
|---|---|---|---|---|

## Transition Logic

- previous -> this section:
- inside this section:
- this section -> next:

## Claims Deferred

| Deferred claim | Reason | Where to handle instead |
|---|---|---|

## 特别检查（Methodology 通用）

- **Research design coherence**：研究范式 → 研究问题 → 方法选择 → 数据类型，
  这条链是否能从范式被"推出来"，而不只是被"允许"。
- **Sampling / Case selection**：抽样或选案逻辑是否说清楚？是否有 inclusion / 
  exclusion criteria？还是只说了"我选了这些"？
- **Data collection**：工具 / 程序 / 时间 / 地点 / 知情同意是否齐全？
- **Analysis procedure**：分析步骤是否可被另一位研究者复现？编码 / 模型 / 
  统计方法是否带名字、版本、参数？
- **Validity / Trustworthiness**：依研究范式选合适的判据（内部 / 外部效度；
  trustworthiness / credibility / dependability；rigor / reproducibility）。
- **Ethical procedures**：伦理审查、数据保护、匿名化是否独立成节或明确交代？
- **Limitations**：是否预告，并区分 "design choice" vs "real limitation"？

输出后停下，问我是否按这个结构进入段落起草。

## 输入

Methodology Writing Configuration：
[粘贴]

Methodology Evidence Pack：
[粘贴]

目标 section：
[填]
```
