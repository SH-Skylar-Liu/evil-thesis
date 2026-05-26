---
status: prompt
type: prompt
task: conclusion_revision_execution
use_when: "已有确认的 Conclusion 修订范围"
do_not_use_when: "还没确认范围"
input_required:
  - "用户确认的 revision scope"
  - "原始 Conclusion 草稿"
  - "Risk Register"
  - "Synthesis Framework"
output: "修订后文本 + 修改说明 + unresolved items"
stop_points:
  - "只完成确认范围，完成后停下"
quality_gates:
  - "不修改未确认范围"
  - "不引入新 finding 或新 citation"
related_prompts:
  - "04_Conclusion风险检查_prompt"
  - "../../审阅/09_再审与回归追踪_prompt"
---

# Conclusion 修订执行 prompt

## 复制给 LLM 的 prompt

```text
请根据我确认的 revision scope 执行 Conclusion 局部修订。不要扩大范围。

## 输入材料

1. 原始草稿：[粘贴或路径]
2. 已确认 revision scope：[粘贴]
3. Risk Register：[粘贴]
4. Synthesis Framework：[粘贴]

## 执行规则

- 只修改确认范围；
- 如修改需要回到 Discussion 加内容（例如某 contribution 在 Discussion 没铺垫），
  不要替我补 Discussion，标 [BACK TO DISCUSSION] 并保留原文；
- 如修改需要重新评估 contribution（例如风险检查说 over-claim），
  请提供 2-3 个 softened phrasing 选项让我选；
- 不要把空话 future work 改成另一种空话；具体不出来就保留 [SPECIFICITY NEEDED]；
- 保留中英双语结构。

## 输出

## Revised Text

[English revised text]

**中文：**
[中文 gloss]

## What Changed

| Change | Reason | Risk addressed |
|---|---|---|

## Phrasing Options

如对某 contribution 提供了多个 softened phrasing：

| Option | Phrasing | Strength |
|---|---|---|

## Remaining Issues

- [BACK TO DISCUSSION / SPECIFICITY NEEDED / DETAIL NEEDED]

输出后停下，建议是否回到 04_Conclusion风险检查_prompt；
对修订前后用 审阅/09_再审与回归追踪_prompt 查回归。
```
