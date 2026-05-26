---
status: prompt
type: prompt
task: results_narration
use_when: "证据和结构已确认，需要把数据 / 引述 / 案例叙事化成 Results 段落"
do_not_use_when: "还没 evidence pack；或要做 interpretation（属于 Discussion）"
input_required:
  - "Results Section Plan"
  - "Results Evidence Pack"
  - "目标段落范围"
output: "英文段落 + 中文 gloss + 数据-叙事对齐核查 + unresolved items"
stop_points:
  - "每次只起草一个 section 或 2-3 段，完成后停下"
quality_gates:
  - "observation ≠ interpretation：不越界做文化 / 因果解释"
  - "每个数字 / 引述都能追溯到数据源"
  - "不报告未跑出来的结果"
related_prompts:
  - "05_Results风险检查_prompt"
  - "../Discussion/00_Discussion_INDEX"
---

# Results 结果叙事化 prompt

## 复制给 LLM 的 prompt

```text
请根据已确认的 Results Section Plan 和 Evidence Pack 起草目标段落。
不要扩大范围；每次只写我指定的 section 或 2-3 个段落。

## 你的角色

你的任务不是帮我解释数据，而是把数据安放到正确的认识论位置上——它们是
观察 (observations / findings)，不是 interpretation。

## 铁律

1. **observation ≠ interpretation**：报告 frequency / theme / pattern / 
   model output 是观察；不要跳到 "this means X for Y" 类型的解读，
   那留给 Discussion。可以指出 "this pattern was particularly visible 
   among X"，但不要 "this pattern reveals that society is Y"。

2. **不声称因果**，除非研究设计支持（实验 / quasi-experimental / 
   严格因果识别）。只能描述 association / co-occurrence / pattern。

3. **量化 + 语境化**：每个数字紧跟一句"这意味着什么模式 / 范围"，
   但不跳到解释。例如："65% (n=130) reported X" 后面跟
   "a majority but not uniformly distributed across [subgroup]"——
   不跟 "suggesting that society has shifted toward Y"。

4. **质性引述要带上下文**：参与者编号、访谈时间、问题情境。
   例："P12, a postgraduate teacher with five years' experience, 
   described their workflow as ..."——不要孤立的 "one participant said"。

5. **不压缩不确定性**：CI / p / 样本量 / 编码一致性 / 模型置信度——
   写进正文或紧接表格，不藏附录。

6. **数据-叙事对齐**：figure / table 里没有的东西不要在正文里写出来；
   反之亦然。table 里有 robustness check 而正文没提，要么删 table，
   要么正文加引用。

## 写作规则

- 描述结果用过去时（"55% reported"、"theme X emerged from")。
- 不要使用：significant（口语意义）/ crucial / robust（除非有 robustness check）/
  leverage / nuanced / delve / it is worth noting / importantly。
  允许 "statistically significant" 当且仅当确实有 p value。
- 不要用 firstly / secondly / thirdly；用 paragraph topic 引导即可。
- table / figure 在正文里第一次出现时必须有 caption 编号引用
  （"as Table 2 shows..." 或 "(Table 2)"）。

## 输出

## Drafted Section

[English text]

**中文：**
[中文 gloss]

## Data-Narrative Alignment Check

| Sentence | Evidence source | Type (observation / interpretation slip) | Status |
|---|---|---|---|

任何标为 "interpretation slip" 的句子必须改写或挪去 Discussion。

## Unresolved Items

- [CITATION NEEDED / DETAIL NEEDED / DATA NEEDED]

输出后停下，问我是否进入 Results 风险检查。

## 输入

Results Section Plan：
[粘贴]

Results Evidence Pack：
[粘贴]

目标段落范围：
[填]
```
