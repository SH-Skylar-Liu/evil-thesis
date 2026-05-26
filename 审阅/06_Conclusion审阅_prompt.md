---
status: prompt
type: prompt
task: conclusion_chapter_review
use_when: "审阅 Conclusion 章节"
do_not_use_when: "审 Discussion → 05；通用稿件 → 01"
input_required:
  - "Conclusion 草稿"
  - "RQ list（最终版）"
  - "可选：Discussion 草稿"
output: "默认：诊断报告 + 优先级清单（read-only）；opt-in：逐节修订"
quality_gates:
  - "默认 read-only"
  - "RQ 回应直接性"
  - "Contribution claim 撑得起前文"
  - "future work 具体性"
related_prompts:
  - "05_Discussion审阅_prompt"
  - "09_再审与回归追踪_prompt"
---

# Conclusion 章节审阅 prompt

## 复制给 LLM 的 prompt

```text
# Task: Conclusion Chapter Review

## 模式选择

- **Mode A · 纯诊断（默认）**
- **Mode B · 诊断 + 修订**：仅明确要求时才用

## Quality Standard

Conclusion chapter must satisfy:

1. **Direct RQ response**: each RQ is answered in 1-2 sentences with a hedge 
   matched to finding strength.
2. **No new findings**: nothing in Conclusion is a finding or interpretation 
   that did not appear in Results / Discussion.
3. **No new citations** (default): if citations appear, they are pre-existing 
   references used to position the contribution, not new literature engagement.
4. **Contribution claims are layered and supported**: theoretical / 
   methodological / empirical / practical contributions are distinguished; each 
   can be traced to a section in the thesis.
5. **Limitations are addressed**: either in Discussion or in Conclusion, the 
   key limitations are stated with the claims they affect.
6. **Future work is specific**: each future direction names the next study / RQ / 
   dataset / method. "More research is needed" is not acceptable.

## 评级与盲评预承诺

读正文前对上面 6 条各写一句标尺。逐条评级。决策映射。反谄媚。

## Workflow

### Step 1: Diagnosis

逐节诊断 + 特别检查：

- **RQ-response matrix**：对每个 RQ，列出：
  - 在 Conclusion 哪一段被回答；
  - 回应的 hedge 是否与 finding strength 匹配；
  - 是否绕开 RQ 谈泛泛 implications。
- **New-content sweep**：列出 Conclusion 里在 Results / Discussion 找不到出处的
  finding / interpretation / citation。
- **Contribution audit**：对每条 contribution，标 type + traceable evidence + 
  over/under-claim 判断。
- **Limitation coverage**：关键 limitations 是否在 Discussion 或 Conclusion 
  覆盖到？
- **Future work specificity check**：每条 future direction 标"够具体 / 套话 /
  与前文 limitation/gap 失联"。
- **Structural integrity**：是否变成长版 Abstract？是否抄写 Methodology？
  收笔是否给读者 "so what"？

End with priority list.

### Step 2 (Mode B only): 逐节修订

特别要求：
- 不要把 vague future work 改成另一种 vague future work；不具体就标 
  [SPECIFICITY NEEDED]。
- 不要把 over-claim 改成稍弱的 over-claim；必须 drop 或回到 Discussion 补证据。
- contribution 修订要提供 2-3 个 softened phrasing 让用户选。

### Step 3: Coherence with Discussion

- Conclusion 的 contribution 是否在 Discussion 已经铺垫？
- Conclusion 的 limitation 是否与 Discussion 一致？
- Discussion 留了什么"so what"，Conclusion 是否承接？

## Constraints

- 默认 read-only。
- 不虚构 findings 或 citations。
- 保留双语结构。

## 待审章节

[路径或内容]

## RQ list（最终版）

[填]

## Discussion 草稿（可选）

[路径]
```
