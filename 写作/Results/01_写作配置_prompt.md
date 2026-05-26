---
status: prompt
type: prompt
task: results_writing_configuration
use_when: "开始一轮 Results / Analysis 写作、重写、局部修订前"
do_not_use_when: "数据 / 分析还未完成；或只是润色"
input_required:
  - "本轮目标"
  - "数据 / 编码 / 模型输出的位置"
  - "可选：导师反馈"
output: "Results Writing Configuration + 本轮边界 + 下一步 prompt"
stop_points:
  - "配置输出后停下，等用户确认本轮范围"
quality_gates:
  - "必须区分 confirmed result / preliminary result / pending result"
related_prompts:
  - "02_证据包生成_prompt"
---

# Results 写作配置 prompt

## 复制给 LLM 的 prompt

```text
请按照 Results 写作配置流程执行。现在不要起草正文。你的任务是先确定本轮目标、
材料、范围、风险和下一步。

## 输出

## Results Writing Configuration

- task type: configuration / evidence pack / structure / drafting / risk check / revision
- target section / RQ this section answers:
- target reader: examiner / advisor / journal reviewer
- analysis approach: quantitative / qualitative / mixed
- data sources（路径 / 表 / 文件）:
- confirmed results: [我已经完成且复核过的]
- preliminary results: [跑出来但未复核 / 还需 sensitivity check 的]
- pending results: [还没跑或还没编码完的]
- key tables / figures planned:
- temporary requirements:
- out of scope for this round:
- next prompt to use:

## 规则

- 如果证据还没整理，next: 02_证据包生成
- 如果证据已整理但结构不清楚，next: 03_章节结构规划
- 如果结构已确认，next: 04_结果叙事化
- 如果已有草稿要检查风险，next: 05_Results风险检查
- 如果已有修改清单，next: 06_修订执行

配置输出后停下，问我是否确认本轮范围。

## 输入

本轮目标：
[填]

数据 / 编码 / 模型输出位置：
[填路径或简述]

已有反馈：
[可选]
```
