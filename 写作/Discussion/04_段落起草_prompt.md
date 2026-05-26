---
status: prompt
type: prompt
task: discussion_paragraph_drafting
use_when: "结构和证据已确认，要起草 Discussion 的一个 section 或 2-3 段"
do_not_use_when: "还没 section plan；或只是润色"
input_required:
  - "Discussion Section Plan"
  - "Discussion Evidence Pack"
  - "目标段落范围"
output: "英文段落 + 中文 gloss + evidence-stance 核查 + unresolved items"
stop_points:
  - "每次只起草一个 section 或 2-3 段，完成后停下"
quality_gates:
  - "每个 citation 必须有明确 stance（不允许 vague background reference）"
  - "不重述 Results；只 briefly remind"
  - "解释要带 epistemic hedge：one possible reading / consistent with X / suggests"
  - "不滑到因果，除非研究设计支持"
related_prompts:
  - "05_Discussion风险检查_prompt"
---

# Discussion 段落起草 prompt

## 复制给 LLM 的 prompt

```text
请根据已确认的 Discussion Section Plan 和 Evidence Pack 起草目标段落。
每次只写指定的 section 或 2-3 段。

## Discussion 段落的四个基本动作

每段或每节通常组合下面 2-3 个动作（不是机械顺序）：

1. **Briefly remind finding**（≤1 句）：用一句话提示要讨论的 finding，
   不要复制 Results 的整段。例："The finding that 65% of teachers reported
   X under condition Y..."
2. **Engage with literature**：说明这个 finding 和已有研究的具体关系——
   confirms / extends / refines / contradicts / bridges / reveals gap。
   每个引用都要带 stance。
3. **Offer interpretation**：提出对 finding 的解读，带 epistemic hedge：
   - "One possible reading is..."
   - "This is consistent with X explanation..."
   - "An alternative interpretation is..."
   - 不要 "this proves" / "this demonstrates that society Y"。
4. **Caveat or boundary**：解读适用范围、需谨慎之处、reasonable rival 解释。

## 写作铁律

- **不重述 Results**：briefly remind 不等于把 Results 段落复制过来。
- **不堆 citation**：每个引用要说明 stance（"Smith (2021) makes a similar
  argument about X" 而不是 "(see Smith 2021)" 单独出现）。
- **不滑到因果**：除非研究设计支持。可以 "is associated with" / 
  "co-occurs with" / "may contribute to"——不可 "causes" / "leads to" /
  "explains why"。
- **不一锤定音**：避免 "this study proves / demonstrates / definitively
  establishes"。用 "suggests / points to / is consistent with"。
- **不堆隐喻**：Discussion 不需要文学修辞；clarity > elegance。
- 不要使用 banned words: significant（除非统计意义）/ crucial / robust /
  leverage / nuanced / delve / foundational / definitive / most cutting-edge /
  it is worth noting / importantly。
- 不要 firstly / secondly / thirdly。

## 输出

## Drafted Section

[English text]

**中文：**
[中文 gloss]

## Evidence-Stance Check

| Sentence with citation | Citation | Stance from Evidence Pack | Match? |
|---|---|---|---|

任何 mismatch 或 vague reference 必须改写。

## Interpretation Inventory

| Interpretation made | Hedge used | Rival considered? | Confidence |
|---|---|---|---|

## Unresolved Items

- [CITATION NEEDED / DETAIL NEEDED / NEW READING NEEDED]

输出后停下，问我是否进入 Discussion 风险检查。

## 输入

Discussion Section Plan：
[粘贴]

Discussion Evidence Pack：
[粘贴]

目标段落范围：
[填]
```
