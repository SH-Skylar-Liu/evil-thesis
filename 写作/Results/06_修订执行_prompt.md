---
status: prompt
type: prompt
task: results_revision_execution
use_when: "已有确认的 Results 修订范围"
do_not_use_when: "还没确认范围"
input_required:
  - "用户确认的 revision scope"
  - "原始 Results 草稿"
  - "Risk Register 或修改清单"
  - "Evidence Pack"
output: "修订后文本 + 修改说明 + unresolved items"
stop_points:
  - "只完成确认范围，完成后停下"
quality_gates:
  - "不修改未确认范围"
  - "不删除 unresolved markers，除非已解决"
  - "保留双语结构"
related_prompts:
  - "05_Results风险检查_prompt"
  - "../../审阅/09_再审与回归追踪_prompt"
---

# Results 修订执行 prompt

## 复制给 LLM 的 prompt

```text
请根据我确认的 revision scope 执行 Results 局部修订。不要扩大范围，
不要重写整章。

## 输入材料

1. 原始草稿：[粘贴或路径]
2. 已确认 revision scope：[粘贴]
3. Risk Register / 修改清单：[粘贴]
4. Evidence Pack：[粘贴]

## 执行规则

- 只修改确认范围；
- 把"应挪到 Discussion"的 interpretation 切出来，标 [MOVE TO DISCUSSION] 
  并保留原文供我决定如何整合，不要直接删；
- 如果一个修改需要重新跑数据 / 重新编码，不要替我做，标 [DATA NEEDED]；
- 如果 citation 不足，保留 [CITATION NEEDED]；
- 保留中英双语结构。

## 输出

## Revised Text

[English revised text]

**中文：**
[中文 gloss]

## What Changed

| Change | Reason | Risk addressed |
|---|---|---|

## Moved to Discussion

| Original sentence | Where to handle in Discussion |
|---|---|

## Remaining Issues

- [CITATION NEEDED / DETAIL NEEDED / DATA NEEDED]

输出后停下，建议是否回到 05_Results风险检查_prompt 做一次复查；
如果这是对上一轮审阅意见的修订，也可以用 审阅/09_再审与回归追踪_prompt 查回归。
```
