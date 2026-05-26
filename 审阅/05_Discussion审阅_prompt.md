---
status: prompt
type: prompt
task: discussion_chapter_review
use_when: "审阅 Discussion 章节"
do_not_use_when: "审 Results → 04；审 Conclusion → 06"
input_required:
  - "Discussion 草稿"
  - "可选：Results 草稿 + reading notes（核对文献对话真假）"
output: "默认：诊断报告 + 优先级清单（read-only）；opt-in：逐节修订"
quality_gates:
  - "默认 read-only"
  - "区分 over-interpretation / under-interpretation"
  - "区分 vague reference / real engagement"
  - "不虚构文献观点"
related_prompts:
  - "04_Results审阅_prompt"
  - "07_论点压力测试_prompt"
  - "09_再审与回归追踪_prompt"
---

# Discussion 章节审阅 prompt

## 复制给 LLM 的 prompt

```text
# Task: Discussion Chapter Review

## 模式选择

- **Mode A · 纯诊断（默认）**
- **Mode B · 诊断 + 修订**：仅明确要求时才用

## Quality Standard

Discussion chapter must satisfy:

1. **Not a Results restatement**: each section briefly reminds the relevant 
   finding (≤1 sentence) and then does interpretive / dialogic work.
2. **Real literature engagement**: every citation carries a specific stance —
   confirms / extends / refines / contradicts / bridges / reveals gap.
   No vague "see also" references.
3. **Interpretation hedging**: interpretations are framed with epistemic markers 
   (suggests / is consistent with / one possible reading) rather than 
   "proves / demonstrates / definitively".
4. **Rival interpretations**: for each major finding, at least one reasonable 
   rival reading is acknowledged or actively engaged.
5. **Limitations are real**: each stated limitation specifies which claim it 
   affects and what it does not affect. Limitations are not used as a 
   self-deprecating gesture or as a future-work disclaimer.
6. **Implications are layered**: theoretical / methodological / practical / 
   policy implications are distinguished, not collapsed.

## 评级与盲评预承诺

读正文前对上面 6 条各写一句标尺。逐条评级。决策映射。反谄媚。

## Workflow

### Step 1: Diagnosis

逐节诊断 + 特别检查：

- **Restatement detection**：列出每段中"实际上是 Results 复读"的句子。
- **Vague reference detection**：列出每个没有明确 stance 的 citation。
- **Over-interpretation map**：列出使用 prove / cause / demonstrate / shape 
  等强动词、但研究设计不支持的句子。
- **Missing rival**：哪些 finding 只给出一种解释而没考虑 reasonable rival？
- **Limitation truth check**：每条 limitation 是否真的影响了 claim，还是套话？
- **Implication category check**：theoretical / methodological / practical / 
  policy 是否分清？

End with priority list.

### Step 2 (Mode B only): 逐节修订

特别要求：
- 不要把 over-interpretation 改成更含蓄的 over-interpretation——结构上必须
  drop 或挪到 future work。
- 不要凭训练记忆给 citation；只用我提供的 reading notes 里出现过的文献。

### Step 3: Structural review

- 整章是否真的回答了 "so what" 而不只是 "what we found"？
- Discussion 与 Conclusion 的分工是否清楚？
- limitations 位置是否合理？

## Constraints

- 默认 read-only。
- 不虚构文献观点。
- 引用必须能在我的 reading notes 里找到出处，否则标 [来自记忆，需核实]。
- 保留双语结构。

## 待审章节

[路径或内容]

## 我提供的 reading notes（用于核对文献对话）

[路径或粘贴 keys 列表]

## 关注点

[可选]
```
