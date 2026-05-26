---
status: prompt
type: prompt
task: conclusion_synthesis_framework
use_when: "已有 Discussion 草稿，需要把 RQ × contribution × limitation × future 整理成 Conclusion 骨架"
do_not_use_when: "还没 Discussion；或只是润色"
input_required:
  - "Conclusion Writing Configuration"
  - "Discussion 草稿"
  - "RQ list"
output: "Conclusion Synthesis Framework：RQ 回应 + contribution × evidence map + limitation + future work"
stop_points:
  - "骨架输出后停下，等用户确认"
quality_gates:
  - "每个 contribution 必须能指回前文段落"
  - "不引入新 finding 或新 citation"
related_prompts:
  - "03_段落起草_prompt"
---

# Conclusion 综合骨架 prompt

## 复制给 LLM 的 prompt

```text
请为 Conclusion 章节生成综合骨架。不要起草正文。任务是把 RQ × contribution ×
limitation × future 在论文范围内对齐。

## 知识隔离

- 只用论文已有的 findings 和 claims；
- 不引入新 citation；
- 不引入 Discussion 没出现过的新解读；
- 任何看似自然但论文里其实没说过的句子，标 [新增 claim，需核实]。

## 输出

## Conclusion Synthesis Framework

### A. RQ 回应矩阵

对每个 RQ：

| RQ # | RQ wording | One-sentence answer | Evidence location（chapter / section）| Strength（strong / qualified / partial / unable）| Hedge to use |
|---|---|---|---|---|---|

Strength 取值：
- **strong**：findings + Discussion 都明确支持；
- **qualified**：明确支持但有重要 boundary；
- **partial**：只回答了 RQ 的一部分；
- **unable**：研究未能回答（如样本不足）——必须诚实承认。

Hedge 取值：suggests / points to / is consistent with / indicates / 
demonstrates within X scope / does not allow conclusion about ...

### B. Contribution × Evidence Map

对每条 contribution，必须能指回前文：

| Contribution | Type（theoretical / methodological / empirical / practical / policy）| Evidence in thesis | What it is NOT a contribution to |
|---|---|---|---|

最后一列特别重要：明确不声称什么，可以预先回应审稿人的潜在 over-claim 质疑。

### C. Limitation Slate

| Limitation | Affects which claim | Mitigation tried | Residual impact |
|---|---|---|---|

如 limitations 已经在 Discussion 处理，Conclusion 只列 2-3 个 most consequential。
如完全在 Conclusion 处理，列全。

### D. Future Work Slate

| Future direction | Why（来自哪个 limitation / gap / 意外发现）| Specificity check |
|---|---|---|

Specificity check：必须能用一句话说出"下一篇论文 / 下一步研究做什么 + 用什么数据 / 
方法 + 期望解决什么"。**不接受** "future research could explore X" 这种空话。

### E. Opening 与 Closing 候选

Conclusion 通常以"重申研究问题与重要性"开篇，以"研究贡献与意义"收笔。
请提供 2 个 opening 候选 + 2 个 closing 候选（各 2-3 句），让用户选。

## Conflict / Inconsistency Check

如果 RQ 回应矩阵显示某个 RQ 实际上没被 findings 充分回答，但你打算
claim contribution——这是个 red flag。明确标出来，让用户决定怎么处理。

输出后停下，问我是否按这个骨架进入段落起草。

## 输入

Conclusion Writing Configuration：
[粘贴]

Discussion 草稿：
[粘贴或路径]

RQ list（最终版）：
[填]
```
