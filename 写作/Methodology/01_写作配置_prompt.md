---
status: prompt
type: prompt
task: methodology_writing_configuration
use_when: "开始一轮 Methodology 写作、重写、局部修订前"
do_not_use_when: "只是润色一个已经确认无方法论风险的段落；或只是阅读文献"
input_required:
  - "本轮目标：诊断 / 结构规划 / 段落起草 / 修订"
  - "最新 Methodology 草稿或目标 section 路径"
  - "可选：导师反馈、审稿意见、Research Planning Brief"
output: "Methodology Writing Configuration + 本轮边界 + 需要读取的材料清单 + 下一步 prompt"
stop_points:
  - "配置输出后停下，等用户确认本轮范围"
  - "用户确认前，不读取大批文件、不起草正文"
quality_gates:
  - "必须区分 confirmed facts / inferred claims / open details"
  - "不能把 Methodology 写作扩大成整篇论文重写"
failure_modes:
  - "如果缺少最新草稿路径，先要求用户提供或改成结构规划任务"
  - "如果目标太宽，收窄到一个 section 或一个 revision pass"
related_prompts:
  - "02_证据包生成_prompt"
  - "03_章节结构规划_prompt"
  - "04_段落起草_prompt"
---

# Methodology 写作配置 prompt

## 复制给 LLM 的 prompt

```text
请按照我的 Methodology 写作配置流程执行。现在不要起草正文，
也不要直接修订文件。你的任务是先确定本轮写作目标、材料、范围、
风险和下一步 prompt。

## 输出 Methodology Writing Configuration

## Methodology Writing Configuration

- task type: diagnosis / evidence pack / structure plan / drafting / revision / risk check
- target section:
- target reader: advisor / examiner / journal reviewer / internal planning
- current source files:
- confirmed facts: [我或导师明确确认的方法选择 / 工具 / 数据]
- inferred claims: [我据已有材料推断但未确认的]
- open details: [还需要补的细节]
- temporary requirements that apply: [如有当前阶段特殊要求]
- out of scope for this round: [本轮不动的部分]
- next prompt to use:

## 规则

- 如果本轮需要先抽证据，next prompt 用 02_证据包生成_prompt。
- 如果证据已经足够但结构不清楚，next prompt 用 03_章节结构规划_prompt。
- 如果结构已经确认，next prompt 用 04_段落起草_prompt。
- 如果已有草稿需要检查风险，next prompt 用 05_方法论风险检查_prompt。
- 如果已有明确修改清单，next prompt 用 06_修订执行_prompt。

配置输出后停下，问我是否确认这个范围。

## 输入

本轮目标：
[填]

目标 section / 文件：
[填]

已有材料或反馈：
[可选]
```
