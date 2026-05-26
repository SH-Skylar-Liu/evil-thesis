---
status: active
type: prompt_index
---

# 审阅 Prompt 索引

审阅类 prompt 不应该合成一个，因为你需要多种审阅尺度。全区共享一个"评级纪律层"：**盲评预承诺**（读稿前先定标尺）+ **分级量表**（达标 / 部分达标 / 不达标）+ **决策阈值**（小修 / 大修 / 重构）+ **反谄媚**。

## 怎么选

| 场景 | 用哪个 prompt | 说明 |
|---|---|---|
| 审普通论文、章节、proposal、meeting draft | [01_通用学术审阅_prompt.md](01_通用学术审阅_prompt.md) | 通用严格审阅 + 分级量表 |
| 专门审文献综述 | [02_文献综述审阅_prompt.md](02_文献综述审阅_prompt.md) | 文献综述专门标准 + 分级量表 |
| 审 Methodology chapter | [03_Methodology审阅_prompt.md](03_Methodology审阅_prompt.md) | 默认 read-only 纯诊断；明确要求才修订 |
| 审 Results / Analysis chapter | [04_Results审阅_prompt.md](04_Results审阅_prompt.md) | over-claim、数据-叙事对齐、不确定性披露 |
| 审 Discussion chapter | [05_Discussion审阅_prompt.md](05_Discussion审阅_prompt.md) | over-interpretation、伪对话、limitation 真假 |
| 审 Conclusion chapter | [06_Conclusion审阅_prompt.md](06_Conclusion审阅_prompt.md) | RQ 回应、contribution、future work 具体性 |
| 让人专门攻击我的论点 | [07_论点压力测试_prompt.md](07_论点压力测试_prompt.md) | 对抗式红队 + 让步阈值协议 |
| 章节大修后批量核查引用 | [08_批量引用核查_prompt.md](08_批量引用核查_prompt.md) | 三库存在性 + 声明匹配核查 |
| 改完一稿，想知道比上版好了还是退了 | [09_再审与回归追踪_prompt.md](09_再审与回归追踪_prompt.md) | 对比上一轮报告，专抓退步 |
| 检查跨章节是否自洽 | [10_跨章节一致性检查_prompt.md](10_跨章节一致性检查_prompt.md) | 概念 / 理论 / 声明强度一致性 |
| 写历史材料，查时间错位（可选） | [11_时间性核查_prompt.md](11_时间性核查_prompt.md) | 时代错位 / 因果倒置 / 把历史写成当下 |

## 审阅之后怎么办

如果审阅报告指出"需要补文献"，不要直接乱读。下一步应该去：

- [../阅读/03_根据反馈找Gap并补文献_prompt.md](../阅读/03_根据反馈找Gap并补文献_prompt.md)

它会把审阅意见转成 gap，再找文献，再评分，再读。

## 全区共享的纪律层

所有审阅 prompt 都共享：

1. **盲评预承诺**：读正文前先定标尺；读完才定标准会让你被稿子自己的 framing 带走。
2. **分级量表**：达标 / 部分达标 / 不达标，每项附文本依据。
3. **决策阈值**：全部达标 → 小修；出现部分达标无不达标 → 大修；任一不达标 → 重构。
4. **反谄媚**：不达标就写不达标；不为礼貌淡化。
5. **优先结构性 / 概念性问题**：不先纠结语言。
6. **批评带文本依据**：所有判断必须可追溯。
