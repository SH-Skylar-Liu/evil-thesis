---
status: prompt
type: prompt
task: results_section_structure
use_when: "已有 Results 证据包，需要规划章节结构 / 节序"
do_not_use_when: "还没有 evidence pack；或只是润色"
input_required:
  - "Results Writing Configuration"
  - "Results Evidence Pack"
output: "Section Plan + paragraph sequence + table/figure placement"
stop_points:
  - "结构方案输出后停下，等用户确认再起草"
quality_gates:
  - "结构必须服务 RQ，不是 data dump"
  - "tables / figures 必须有正文引用计划"
related_prompts:
  - "04_结果叙事化_prompt"
---

# Results 章节结构规划 prompt

## 复制给 LLM 的 prompt

```text
请为 Results 章节规划结构。不要起草完整正文。你可以写 topic sentences 和段落功能，
但不要展开成长段落。

## 三种常见组织逻辑（选一个，或我会指定）

1. **By RQ**：每个 RQ / 子问题对应一个 section；最常见。
2. **By data source**：survey results、interview themes、document analysis 各成一节；
   适合数据来源彼此互补的混合方法。
3. **By analytic layer**：descriptive → relational → explanatory（量化）或
   themes → cross-theme patterns → deviant cases（质性）。

每种组织逻辑都必须能说出"为什么这样组织"，不是按数据顺序流水。

## 输出

## Results Section Plan

- target section:
- which RQ(s) this section answers:
- organizing logic:
- reader problem this section must solve:
- relation to previous section:
- relation to next section:

## Paragraph Sequence

| Paragraph | Function | Topic sentence draft | Evidence to use | Table/Fig reference | Risk to avoid |
|---|---|---|---|---|---|

## Tables / Figures Plan

| # | Type | Function | Source data | Caption draft | Discussed in paragraph(s) |
|---|---|---|---|---|---|

## Transition Logic

- previous -> this section:
- inside this section:
- this section -> next:

## Deferred to Discussion

| Claim | Why deferred |
|---|---|
| ... | interpretation / causal claim / 与文献对话 → 属于 Discussion |

输出后停下，问我是否按这个结构进入段落起草。

## 输入

Results Writing Configuration：
[粘贴]

Results Evidence Pack：
[粘贴]

目标 section：
[填]
```
