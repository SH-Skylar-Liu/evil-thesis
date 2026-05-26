---
status: active
type: prompt_index
---

# Results / Analysis 章节写作 Workflow Index

Results（量化为主）/ Analysis（质性或混合方法常用）章节最难的不是写出数字，而是**让数字 / 案例 / 引述被安放到正确的认识论位置**——它们是观察 / 发现，不是 interpretation。Interpretation 留给 Discussion。

## 核心链路

```text
data / coded transcripts / model outputs / tables / figures
        ↓
01 Results 写作配置
        ↓
02 Results 证据包生成
        ↓
03 Results 章节结构规划
        ↓
04 Results 叙事化与段落起草
        ↓
05 Results 风险检查（over-claim / 数据-叙事对齐 / 边界）
        ↓
06 Results 修订执行
```

## 怎么选

| 场景 | 用哪个 prompt |
|---|---|
| 开始一轮 Results 写作或重写前 | [01_写作配置_prompt.md](01_写作配置_prompt.md) |
| 把原始数据 / 编码 / 输出整理成可写素材 | [02_证据包生成_prompt.md](02_证据包生成_prompt.md) |
| 规划 Results 节序与段落结构 | [03_章节结构规划_prompt.md](03_章节结构规划_prompt.md) |
| 把数字 / 引述 / 案例叙事化成段落 | [04_结果叙事化_prompt.md](04_结果叙事化_prompt.md) |
| 检查 over-claim、causal slip、数据-叙事对齐 | [05_Results风险检查_prompt.md](05_Results风险检查_prompt.md) |
| 执行已确认修订 | [06_修订执行_prompt.md](06_修订执行_prompt.md) |

## Results 的认识论铁律

1. **观察 ≠ 解释**：报告 frequencies / themes / patterns / model outputs 是观察；
   把它们解读成因果 / 文化意涵 / 政策含义是 interpretation——后者属于 Discussion。
2. **不声称因果**，除非研究设计支持（实验 / quasi-experimental / 严格因果识别）。
3. **量化 + 语境化**：每个数字紧跟一句"这意味着什么模式 / 范围"，但不跳到解释。
4. **质性引述要带上下文**：参与者编号、访谈时间、问题情境；不要孤立地"参与者说"。
5. **不压缩不确定性**：CI / p / 样本量 / 编码一致性 / 模型置信度——属于结果一部分，
   不藏附录。
6. **数据-叙事对齐**：figure / table 里没有的东西不要在正文里写出来；反之亦然。
