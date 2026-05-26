---
status: prompt
type: prompt
task: methodology_revision_execution
use_when: "已有确认的风险清单或修改清单，需要执行 Methodology 局部修订"
do_not_use_when: "还没有用户确认的修改范围；或风险仍需导师确认"
input_required:
  - "用户确认的 revision scope"
  - "原始草稿"
  - "Risk Register 或修改清单"
  - "Evidence Pack"
output: "修订后文本 + 修改说明 + unresolved items"
stop_points:
  - "只完成确认范围，完成后停下"
quality_gates:
  - "不修改未确认范围"
  - "不删除 unresolved markers，除非已解决"
  - "修订后仍需中英双语"
failure_modes:
  - "如果修改需要未确认事实，保留 [DETAIL NEEDED]"
related_prompts:
  - "05_方法论风险检查_prompt"
  - "../../审阅/09_再审与回归追踪_prompt"
  - "../通用工具/01_学术英文润色_prompt"
---

# Methodology 修订执行 prompt

## 复制给 LLM 的 prompt

```text
请根据我确认的 revision scope 执行 Methodology 局部修订。
不要扩大范围，不要重写整章。

## 输入材料

1. 原始草稿：
[粘贴或路径]

2. 已确认 revision scope：
[粘贴]

3. Risk Register / 修改清单：
[粘贴]

4. Evidence Pack：
[粘贴]

## 执行规则

- 只修改确认范围；
- 如果一个问题需要导师确认，不要替我决定，保留 [ADVISOR CONFIRMATION NEEDED]；
- 如果 citation 不足，保留 [CITATION NEEDED]；
- 不要把草稿改成泛泛的"方法论漂亮话"；每个修改都必须解决一个具体问题；
- 保留中英双语结构。

## 输出

## Revised Text

[English revised text]

**中文：**
[中文 gloss]

## What Changed

| Change | Reason | Evidence / risk addressed |
|---|---|---|

## Remaining Issues

- [列出仍未解决的 citation/detail/advisor confirmation]

输出后停下，建议是否回到 05_方法论风险检查_prompt 做一次复查；
如果这是对上一轮审阅意见的修订，也可以用 审阅/09_再审与回归追踪_prompt
对比上一版、确认没有改出退步。
```
