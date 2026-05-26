---
status: prompt
type: prompt
task: discussion_writing_configuration
use_when: "开始一轮 Discussion 写作、重写、局部修订前"
do_not_use_when: "Results 还没确定；或只是润色"
input_required:
  - "本轮目标"
  - "Results 草稿"
  - "可选：导师反馈"
output: "Discussion Writing Configuration + 下一步 prompt"
stop_points:
  - "配置输出后停下，等用户确认"
quality_gates:
  - "Results 未稳定不应开始 Discussion 大改"
related_prompts:
  - "02_证据包生成_prompt"
---

# Discussion 写作配置 prompt

## 复制给 LLM 的 prompt

```text
请按照 Discussion 写作配置流程执行。现在不要起草正文。

## 输出

## Discussion Writing Configuration

- task type: configuration / evidence pack / structure / drafting / risk check / revision
- target section / RQ this section discusses:
- target reader: examiner / advisor / journal reviewer
- which findings to discuss this round:
- which literature already known to engage with:
- which literature might be missing（需补读时标 [需要新读]）:
- theoretical framing in use:
- temporary requirements:
- out of scope for this round:
- next prompt to use:

## 规则

- 如证据未整理 → next: 02_证据包生成
- 如证据已整理但结构不清 → next: 03_章节结构规划
- 如结构已定 → next: 04_段落起草
- 如已有草稿要查风险 → next: 05_Discussion风险检查
- 如已有修改清单 → next: 06_修订执行

## 前置检查（必做）

- Results 草稿是否已经稳定？如果 Results 还可能大改，建议先稳定 Results 再来。
- 是否已经明确每个 RQ 在 Discussion 里要回答到什么程度？
- 是否清楚要在哪一节处理 limitations、哪一节处理 implications？

配置输出后停下，问我是否确认本轮范围。

## 输入

本轮目标：
[填]

Results 草稿路径：
[填]

已有反馈：
[可选]
```
