---
status: prompt
type: prompt
task: results_chapter_review
use_when: "审阅 Results / Analysis 章节"
do_not_use_when: "审通用稿件 → 01；审 Methodology → 03；审 Discussion → 05"
input_required:
  - "Results 草稿"
  - "可选：Methodology 草稿（核对方法-结果一致性）"
output: "默认：诊断报告 + 优先级清单（read-only）；opt-in：逐节修订"
quality_gates:
  - "默认 read-only"
  - "区分 observation / interpretation slip"
  - "区分 over-claim / under-claim"
  - "不虚构数字"
related_prompts:
  - "03_Methodology审阅_prompt"
  - "05_Discussion审阅_prompt"
  - "09_再审与回归追踪_prompt"
---

# Results 章节审阅 prompt

## 复制给 LLM 的 prompt

```text
# Task: Results / Analysis Chapter Review

## 模式选择

- **Mode A · 纯诊断（默认）**：只诊断、不改写。
- **Mode B · 诊断 + 修订**：仅当用户明确说"进入修订模式"时才用。

## Quality Standard

Results chapter must satisfy:

1. **Observation / Interpretation boundary**: findings are reported as 
   observations, with interpretation reserved for Discussion. No causal slips 
   unless the design supports them.
2. **Data-narrative alignment**: every number in the text appears in a table or 
   figure; every column in a table is discussed or explicitly noted as background.
3. **Disclosure of uncertainty**: CI / p / SE / sample size / coder reliability / 
   model confidence are reported where applicable, not hidden in an appendix.
4. **Sample / Theme integrity**: quantitative samples are reported with N and 
   subgroup breakdowns; qualitative themes are reported with exemplar quotes, 
   participant identifiers, and counter-evidence.
5. **No over-claim**: "majority" matches actual proportions; "significant" is 
   used in its statistical sense; "robust" requires a robustness check; 
   "emergent theme" requires coding evidence; "no effect" is distinguished from 
   "underpowered".
6. **Reproducibility footprint**: the reader can trace each finding back to a 
   specific data location.

## 评级与盲评预承诺

1. **盲评预承诺**：读正文前先针对上面 6 条 Quality Standard 各写一句标尺。
2. **逐条评级**：达标 / 部分达标 / 不达标。
3. **决策映射**：全部达标 → 小修；部分达标无不达标 → 大修；任一不达标 → 重构。
4. **反谄媚**。

## Workflow

### Step 1: Diagnosis

逐节诊断：
- (a) what the section is doing
- (b) what it does well
- (c) where the argument is weak / unclear / inconsistent

特别检查：
- **Observation / Interpretation slips**：列出每一处把 finding 解读成因果 / 
  文化 / 政策含义的句子，标记 "MOVE TO DISCUSSION"。
- **Over-claim sentences**：列出 majority / significant / robust / emergent /
  causal 等关键词使用是否匹配证据。
- **Disclosure gaps**：哪里应该报告 CI / p / N / reliability 但没有？
- **Table-text mismatch**：正文提到的数字在表里能找到吗？表里的列在正文都讨论了吗？
- **Caption self-sufficiency**：每个 table / figure caption 是否能自含？

End with priority list.

### Step 2 (Mode B only): Section-by-section revision

按优先级逐节修订。每节给：英文修订 + 中文 gloss + 修订理由（解决什么具体风险）。
风格规则同 Methodology 审阅。

### Step 3: Structural review

- Section order 是否服务 RQ 而非 data dump？
- 是否有应在 Methodology 但写在 Results 的内容？
- 是否有应在 Discussion 但写在 Results 的内容？

### Step 4: Reproducibility check

- 每个 finding 是否能定位到具体的数据文件 / 表 / 时间戳 / 编码节点？
- 是否给出复现所需的全部信息？

## Constraints

- 默认 read-only。
- Do not invent numbers, p values, or sample sizes.
- Do not smooth over interpretation slips with diplomatic prose.
- Preserve bilingual structure.

## 待审章节

[路径或内容]

## 关注点

[可选：例如某节 over-claim 严重；或 qual coder reliability 不清]
```
