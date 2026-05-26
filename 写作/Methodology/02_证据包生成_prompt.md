---
status: prompt
type: prompt
task: methodology_evidence_pack
use_when: "要从 reading notes、data notes、pipeline docs 中抽取 Methodology 写作证据"
do_not_use_when: "已经有确认好的 evidence pack；或只是普通文献阅读"
input_required:
  - "Methodology Writing Configuration"
  - "目标 section 或 claim list"
  - "可选：相关 reading notes / data notes 路径"
output: "Methodology Evidence Pack + Claim-Evidence Map + citation/detail risk"
stop_points:
  - "证据包输出后停下，等用户确认哪些证据进入结构规划"
quality_gates:
  - "不把 reading note 中没有的内容写成文献观点"
  - "不把 pipeline docs 中未确认的实现细节写成 thesis fact"
  - "每个 claim 必须有 evidence status"
failure_modes:
  - "如果证据不足，输出 [CITATION NEEDED] / [DETAIL NEEDED]，不要补写"
related_prompts:
  - "03_章节结构规划_prompt"
  - "../../审阅/08_批量引用核查_prompt"
---

# Methodology 证据包生成 prompt

## 复制给 LLM 的 prompt

```text
请为 Methodology 章节生成证据包。不要起草正文。你的任务是把本轮目标 section
需要的 claims 和可用证据对应起来。

## 证据来源优先级

1. 最新 Methodology draft / section draft
2. 方法笔记 / pipeline docs / SOP（如有）
3. 已完成的 reading notes
4. 已确认的项目事实

## 输出

## Methodology Evidence Pack

### Target Section

- section:
- writing goal:
- temporary requirements in scope:

### Claim-Evidence Map

| Claim to make | Evidence source | Evidence type | Status | Risk | How to use |
|---|---|---|---|---|---|
| ... | reading note / data note / pipeline doc / confirmed fact | theory / method / data / project fact | confirmed / inferred / missing | low / medium / high | sentence / paragraph / footnote / avoid |

### Evidence Gaps

| Gap | Needed source | Why it matters | Suggested next action |
|---|---|---|---|

### Do Not Overclaim

- [列出本节不能写成强结论的地方]
- 典型 over-claim 模式：
  - 把 pilot / 小样本结果说成 representative
  - 把"我做了这个步骤"说成"这个步骤是 standard"
  - 把"我选了这个方法"说成"这个方法在领域里被广泛认可"
  - 把"工具能做 X"说成"我已经做了 X"

输出后停下，问我确认哪些 claims 可以进入 section outline。

## 输入

Methodology Writing Configuration：
[粘贴]

目标 section / claim list：
[粘贴或填路径]

相关材料路径：
[可选]
```
