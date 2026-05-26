---
status: prompt
type: prompt
task: discussion_revision_execution
use_when: "已有确认的 Discussion 修订范围"
do_not_use_when: "还没确认范围"
input_required:
  - "用户确认的 revision scope"
  - "原始 Discussion 草稿"
  - "Risk Register"
  - "Evidence Pack"
output: "修订后文本 + 修改说明 + unresolved items"
stop_points:
  - "只完成确认范围，完成后停下"
quality_gates:
  - "不修改未确认范围"
  - "保留双语结构"
related_prompts:
  - "05_Discussion风险检查_prompt"
  - "../../审阅/09_再审与回归追踪_prompt"
---

# Discussion 修订执行 prompt

## 复制给 LLM 的 prompt

```text
请根据我确认的 revision scope 执行 Discussion 局部修订。不要扩大范围。

## 输入材料

1. 原始草稿：[粘贴或路径]
2. 已确认 revision scope：[粘贴]
3. Risk Register：[粘贴]
4. Evidence Pack：[粘贴]

## 执行规则

- 只修改确认范围；
- 把应挪到 Results 或 Conclusion 的内容切出来，标 [MOVE TO RESULTS] / 
  [MOVE TO CONCLUSION]，不要直接删；
- 如果一个修改需要新读文献，不要替我读，标 [NEW READING NEEDED: 
  描述要读什么类型]；
- 如果 citation 不足，保留 [CITATION NEEDED]；
- 不要把草稿改成"漂亮但空洞"——每个修改都必须解决一个具体问题；
- 保留中英双语结构。

## 输出

## Revised Text

[English revised text]

**中文：**
[中文 gloss]

## What Changed

| Change | Reason | Risk addressed |
|---|---|---|

## Moved to ...

| Original sentence | Destination | Why |
|---|---|---|

## Remaining Issues

- [CITATION NEEDED / NEW READING NEEDED / DETAIL NEEDED]

输出后停下，建议是否回到 05_Discussion风险检查_prompt；
对修订前后用 审阅/09_再审与回归追踪_prompt 查回归。
```
