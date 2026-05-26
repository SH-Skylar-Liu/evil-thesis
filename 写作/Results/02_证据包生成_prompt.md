---
status: prompt
type: prompt
task: results_evidence_pack
use_when: "把已有数据 / 编码 / 模型输出整理成可用于 Results 写作的素材"
do_not_use_when: "数据还没分析完；或只是润色"
input_required:
  - "Results Writing Configuration"
  - "数据 / 编码表 / 模型输出"
output: "Results Evidence Pack：finding-evidence 映射 + 表 / 图候选 + 限制清单"
stop_points:
  - "证据包输出后停下，等用户确认哪些发现进入结构规划"
quality_gates:
  - "不报告还没跑出来的结果"
  - "每条 finding 必须有数据出处"
  - "区分 finding / interpretation / speculation"
failure_modes:
  - "证据不足就停下要求补；不要编造数字"
related_prompts:
  - "03_章节结构规划_prompt"
---

# Results 证据包生成 prompt

## 复制给 LLM 的 prompt

```text
请为 Results 章节生成证据包。不要起草正文。你的任务是把数据 / 编码 /
模型输出整理成可写作的 finding-evidence 映射。

## 通用原则

- 每条 finding 必须能指回数据出处（表 / 文件 / 行 / 时间戳 / 编码节点）；
- 区分：
  - finding：数据里直接观察到的；
  - interpretation：对 finding 的解读（这里只标注，不展开，留给 Discussion）；
  - speculation：你的猜测，需要明确标 [需核实]。

## 按 analysis approach 选格式

### A. 量化 / 计算结果

| Finding | Data source | Effect size / 数值 | CI / SE / p | Sample / N | Confidence | Risk | How to use |
|---|---|---|---|---|---|---|---|

附加：
- robustness check（如做了）：
- 主要 control / specification 列表：
- 已知 bias / limitation：

### B. 质性 / 主题分析

| Theme | Sub-theme | Exemplar quotes（带参与者编号 / 时间 / 情境）| Coder agreement | Counter-evidence | Risk | How to use |
|---|---|---|---|---|---|---|

附加：
- coding scheme 版本：
- inter-coder reliability（如适用）：
- negative case / 反例处理：

### C. 混合方法

- quant findings 表（同 A）：
- qual findings 表（同 B）：
- integration map：哪些 quant 发现被 qual 解释 / 反过来？哪些不对应？

## Evidence Gaps

| Gap | Why it matters | What needs to happen |
|---|---|---|

## Do Not Overclaim

- 典型 over-claim 模式：
  - 把 association 说成 causation
  - 把 frequency 说成 representativeness
  - 把 single-coder theme 说成 emergent / robust
  - 把模型输出说成 ground truth
- 标出本节最容易越界的句子模板。

输出后停下，问我确认哪些 finding 可以进入结构规划。

## 输入

Results Writing Configuration：
[粘贴]

数据 / 编码 / 输出（路径或贴片段）：
[粘贴或填路径]
```
