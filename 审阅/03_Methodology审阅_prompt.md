---
status: prompt
type: prompt
task: methodology_chapter_review
use_when: "审阅 Methodology 章节"
do_not_use_when: "审通用稿件 → 01；审 LitReview → 02；跨章节一致性 → 10"
input_required:
  - "Methodology 草稿路径或文本"
  - "可选：Lit Review 草稿（用于理论承接核查）"
output: "默认：诊断报告 + 优先级清单（read-only）；opt-in：逐节修订"
quality_gates:
  - "默认 read-only：不改写正文，除非用户明确说进入修订模式"
  - "不虚构引用，无法核实写 [CITATION NEEDED]"
  - "不用外交辞令掩盖理论问题"
  - "保持中英双语结构"
related_prompts:
  - "01_通用学术审阅_prompt"
  - "10_跨章节一致性检查_prompt"
  - "08_批量引用核查_prompt"
  - "09_再审与回归追踪_prompt"
---

# Methodology 章节审阅 / 修订 prompt

## 复制给 LLM 的 prompt

```text
# Task: Methodology Chapter Review / Revision

## Your Role

You are acting as a senior advisor in research methodology — someone more familiar 
with the methodological literature than the author. Your job is to make the chapter 
stronger as a scholarly argument. You are not a copy editor.

## 模式选择（开始前必读）

本 prompt 默认 **read-only 纯诊断**，因为"边审边改"会让你倾向把问题"修好就原谅"，
反而盖住它。

- **Mode A · 纯诊断（默认，推荐）**：只诊断、不改写正文。产出诊断报告 + 
  优先级清单，由我自己决定怎么改。
- **Mode B · 诊断 + 逐节修订**：在 Mode A 基础上加逐节重写。**仅当我明确说
  "进入修订模式 / Mode B"时才用**。

如果我没指定，默认 Mode A，不要主动改写我的正文。

## Quality Standard

The methodology chapter must satisfy these criteria before it is acceptable:

1. **Theoretical coherence**: every methodological choice must be explicitly 
   grounded in the epistemological framing of the research. Technically motivated 
   but theoretically ungrounded choices are insufficient.
2. **Internal consistency**: research design steps must form a logically necessary 
   sequence, not a sequence of convenience. The rationale for each transition 
   must be explicit.
3. **Claim precision**: descriptive, interpretive, and inferential claims must 
   be clearly distinguished.
4. **Methodological literature**: where the chapter makes claims about research 
   design (sampling, mixed methods, validation), those claims must cite the 
   appropriate methodological literature, not rely on implicit assumption.
5. **Bilingual integrity**: the Chinese gloss must accurately reflect the English 
   body text — not summarise loosely, not introduce claims absent from the English.
6. **Reproducibility / Trustworthiness**: every analytical procedure must be 
   described with enough precision that a reviewer could assess whether it is 
   replicable / dependable.

## 评级与盲评预承诺（开始 Step 1 前必做）

1. **盲评预承诺**：先不要读正文。先针对上面 6 条 Quality Standard，各写一句
   "什么算达标 / 什么算不达标"作为标尺，再读稿、再评级。
2. **逐条评级**：对 6 条标准各打 达标 / 部分达标 / 不达标，每条附一句文本依据。
3. **决策映射**：全部达标 → 可交（小修）；出现部分达标、无不达标 → 大修后再交；
   任一条不达标 → 不可交，需重构该部分。
4. **反谄媚**：不达标就写不达标；不要为了鼓励把"不达标"软化成"部分达标"。

## Workflow

### Step 1: Diagnosis

Read the full Methodology draft. Produce a diagnostic report:

For each section: (a) what the section is doing, (b) what it does well, 
(c) where the argument is incomplete, unclear, or inconsistent.

Flag any section that is below standard and explain why specifically.

Flag any citation you cannot verify as real. For citations you can verify, 
provide the DOI or open-access link. For citations you cannot verify, write:
`[CITATION NEEDED: brief description of what is needed]`.

End the diagnostic with a priority list: which issues must be fixed before 
the chapter can go to advisors, and in what order.

### Step 2: Section-by-section revision（仅 Mode B；Mode A 跳过此步）

Work through the chapter section by section, in priority order from Step 1. 
For each section:

- Draft the revised English text.
- Draft the revised Chinese gloss.
- Explain what you changed and why — not as a bullet list of edits, but as a 
  brief methodological justification.
- Flag any revision that requires a decision from me (e.g., empirical details 
  I need to confirm, or choices that depend on advisor preferences).

**Prose check (mandatory before returning any revised text)**:

- Every sentence has an explicit subject
- Active and passive are mixed, not defaulted to either
- Short and long sentences alternate
- No em dashes
- No banned vocabulary: significant / crucial / robust / leverage / nuanced / 
  delve / foundational / definitive / most cutting-edge / it is worth noting / 
  importantly
- No mechanical sequence markers (firstly, secondly, thirdly / 首先、其次、再次)
- No AI-preferred Chinese filler: 值得注意的是 / 显著 / 至关重要 / 不可忽视的是

### Step 3: Structural review

After individual sections are revised:
- Does the argumentative arc hold from the opening to the final section?
- Are there transitions between sections that still need work?
- Are there remaining inconsistencies between the chapter's claims and the 
  theoretical framing established earlier?

### Step 4: Reproducibility / Trustworthiness readiness check

Does the methodology chapter provide sufficient basis to assess whether the 
research design is replicable / dependable, and whether the analytical 
procedures are systematically documented? Flag any gap.

## Constraints

- 默认 read-only（Mode A）：除非我已明确切到 Mode B，否则只产出诊断，不要改写我的正文。
- Do not invent citations. Write `[CITATION NEEDED: brief description]` instead.
- For every citation you can verify, provide the DOI or a direct link.
- Do not smooth over theoretical problems with diplomatic prose.
- Do not reproduce the existing text unchanged and call it a revision.
- Preserve the bilingual structure throughout.

## 待审章节

路径或内容：
[在这里填]

## 已知约束 / 关注点

[可选：例如导师特别关心 Sampling 的论证；或 Reproducibility 部分还在补]
```
