---
status: prompt
type: prompt
task: conclusion_writing_configuration
use_when: "开始一轮 Conclusion 写作 / 重写"
do_not_use_when: "Discussion 还没稳定；或只是润色"
input_required:
  - "本轮目标"
  - "Discussion 草稿"
  - "RQ list"
output: "Conclusion Writing Configuration + 下一步 prompt"
stop_points:
  - "配置输出后停下"
quality_gates:
  - "Discussion 未稳定不建议开始 Conclusion 大改"
related_prompts:
  - "02_综合骨架_prompt"
---

# Conclusion 写作配置 prompt

## 复制给 LLM 的 prompt

```text
请按照 Conclusion 写作配置流程执行。现在不要起草正文。

## 前置检查

- Discussion 是否已经稳定？如果 Discussion 还会大改，建议先稳定再来 Conclusion。
- RQ list 是否最终版？Conclusion 必须严格对应最终版 RQ。
- limitations 已经在 Discussion 处理了吗？如果没有，Conclusion 要给一节。
- target word count（硕士论文 conclusion 通常 1500-3000 词）：[填]

## 输出

## Conclusion Writing Configuration

- task type: configuration / framework / drafting / risk check / revision
- target word count:
- RQs to respond to（按编号 + 一句话提示）:
- limitations location: in Discussion / to be in Conclusion / split
- contribution claims to make (preliminary list):
  - theoretical:
  - methodological:
  - empirical:
  - practical / policy（如有）:
- future work themes (preliminary list):
- temporary requirements:
- out of scope for this round:
- next prompt to use:

## 规则

- 如果还没整理出 RQ-contribution 对应关系 → next: 02_综合骨架
- 如果骨架已确认 → next: 03_段落起草
- 如果已有草稿要查风险 → next: 04_Conclusion风险检查
- 如果已有修改清单 → next: 05_修订执行

配置输出后停下，问我是否确认本轮范围。

## 输入

本轮目标：
[填]

Discussion 草稿路径：
[填]

RQ list：
[填或路径]
```
