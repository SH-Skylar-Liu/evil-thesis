---
status: prompt
type: prompt
task: conclusion_paragraph_drafting
use_when: "骨架已确认，要起草 Conclusion 段落"
do_not_use_when: "还没骨架；或只是润色"
input_required:
  - "Conclusion Synthesis Framework"
  - "目标段落范围"
output: "英文段落 + 中文 gloss + claim-evidence 核查"
stop_points:
  - "每次只起草一节，完成后停下"
quality_gates:
  - "不引入新 finding 或新 citation"
  - "每个 contribution claim 撑得起前文证据"
  - "future work 必须 specific"
related_prompts:
  - "04_Conclusion风险检查_prompt"
---

# Conclusion 段落起草 prompt

## 复制给 LLM 的 prompt

```text
请根据已确认的 Conclusion Synthesis Framework 起草目标段落。
每次只写一节，完成后停下。

## Conclusion 段落的典型流程

通常 Conclusion 章节由这几节组成（按论文长度可合并 / 拆分）：

1. **Opening**（1 段）：重申研究问题、研究为何重要、本章会做什么；
2. **Responses to RQs**（每个 RQ 一段或一小节）：每段开头直接答 RQ，
   后面用 1-2 句指回 finding 与 Discussion 的关键解读；
3. **Contribution**（1-2 段或独立节）：theoretical / methodological / empirical 
   分清楚；每条 contribution 用一句话说清"做了什么 + 对学术共同体意味着什么"；
4. **Limitations**（如未在 Discussion 处理）：每条带 affect-which-claim 说明；
5. **Future work**（1 段）：必须 specific——下一步要做什么、为什么、怎么做；
6. **Closing**（1-2 句）：回到论文最初提出的关切，给一个有重量但不夸大的收笔。

## 写作铁律

- **不重述 Methodology**：不要在 Conclusion 里再讲方法步骤——一句"using a 
  mixed-methods design combining X and Y" 足够；
- **不引入新 finding**：发现都在 Results / Discussion 里；Conclusion 只综合；
- **不引入新 citation**（原则上）：如必须引用，是为了定位贡献，且已在前文出现；
- **不写 vague future work**："more research is needed" / "future studies could 
  further explore X" 这类句子要拒绝。具体写：下一篇论文要做什么 / 下一个 RQ / 
  下一个数据集 / 下一个对照组；
- **不夸大 contribution**：用 "this study contributes by..." 而非 "this study 
  proves / establishes for the first time"；
- **不抄 Abstract**：Conclusion 比 Abstract 更具体、更长、更可论证。

禁用词同前。

## 输出

## Drafted Section

[English text]

**中文：**
[中文 gloss]

## Claim-Evidence Check

| Claim in this section | Evidence in earlier chapter / section | Status |
|---|---|---|

任何 claim 在前文找不到证据的，标 [新增 claim，需核实]，必须回到 02_综合骨架
或 Discussion 解决。

## Future Work Specificity Check

| Future direction | Specific enough? | If not, what to add |
|---|---|---|

## Unresolved Items

- [DETAIL NEEDED / ADVISOR CONFIRMATION NEEDED]

输出后停下，问我是否进入 Conclusion 风险检查。

## 输入

Conclusion Synthesis Framework：
[粘贴]

目标段落范围：
[填]
```
