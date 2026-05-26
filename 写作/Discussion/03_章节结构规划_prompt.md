---
status: prompt
type: prompt
task: discussion_section_structure
use_when: "已有 Discussion 证据包，要规划章节结构"
do_not_use_when: "还没 evidence pack"
input_required:
  - "Discussion Writing Configuration"
  - "Discussion Evidence Pack"
output: "Section Plan + paragraph sequence"
stop_points:
  - "结构输出后停下，等用户确认"
quality_gates:
  - "Discussion 不能复刻 Results 的 section 排列；必须以解释 / 对话 / 限制为主轴"
related_prompts:
  - "04_段落起草_prompt"
---

# Discussion 章节结构规划 prompt

## 复制给 LLM 的 prompt

```text
请为 Discussion 章节规划结构。不要起草完整正文。

## 三种常见组织逻辑（选一个）

1. **By RQ**：每个 RQ 在 Discussion 里有一节，回应"我找到了什么 + 与文献什么关系 +
   意味着什么"。简单清晰，最适合硕士论文。
2. **By cross-cutting theme**：跨 RQ 提炼出 2-3 个 over-arching themes，
   每个 theme 一节。适合 findings 之间互相说明的研究。
3. **By argument**：每节解决一个核心论证（"我的研究让我们重新理解 X"）。
   更难写，但更有论文气质，适合 strong contribution claim。

不要选 by Results section——那会让 Discussion 变成 Results 的复读。

## 输出

## Discussion Section Plan

- target chapter / section:
- organizing logic:
- core argument of the whole Discussion in one sentence:
- relation to Results / Conclusion:

## Section Sequence

| Section | Function | Core finding(s) discussed | Key literature engagement | Main interpretation |
|---|---|---|---|---|

## Limitations 与 Implications 的位置

Limitations 可以：
- 单独成节（最常见，独立 transparency）；
- 散在各 RQ 节末尾（更整合但读者难追踪）。

Implications 可以：
- 单独成节（最常见）；
- 嵌入各 RQ 节作为"so what"段落。

明确选一个，并说明为什么这么放。

## Paragraph Sequence（每节）

| Paragraph | Function（remind / explain / dialogue / contextualise / caveat）| Topic sentence draft | Evidence from Evidence Pack | Risk to avoid |
|---|---|---|---|---|

## Transition Logic

- previous -> this section:
- inside this section:
- this section -> next:

## 必须避免的结构问题

- ❌ Discussion 第一节是 "summary of findings"——这是 Conclusion 的工作；
- ❌ 把 limitations 藏在最后一段没有节标题——会被审稿人质疑诚意；
- ❌ "Implications for practice" 一节里其实只有 "future research could..."——
  这是 future work，不是 implication。

输出后停下，问我是否按这个结构进入段落起草。

## 输入

Discussion Writing Configuration：
[粘贴]

Discussion Evidence Pack：
[粘贴]

目标 section：
[填]
```
