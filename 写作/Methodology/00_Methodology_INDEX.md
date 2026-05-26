---
status: active
type: prompt_index
---

# Methodology 写作 Workflow Index

这个分区用于 Methodology 章节的结构化协作写作。它把章节起草拆成六步，每步有自己的 stop point，避免 LLM 一口气写完一章导致幻觉、跑偏、过度承诺。

## 核心链路

```text
研究规划 / reading notes / data / pipeline notes / existing draft
        ↓
01 Methodology 写作配置
        ↓
02 Methodology 证据包生成
        ↓
03 Methodology 章节结构规划
        ↓
04 Methodology 段落起草
        ↓
05 Methodology 风险检查
        ↓
06 Methodology 修订执行
```

## 怎么选

| 场景 | 用哪个 prompt | 说明 |
|---|---|---|
| 开始一轮 Methodology 写作或重写前 | [01_写作配置_prompt.md](01_写作配置_prompt.md) | 先确定目标、材料、边界和 stop points |
| 要从 reading notes / data notes 抽证据 | [02_证据包生成_prompt.md](02_证据包生成_prompt.md) | 生成 Evidence Pack，不写正文 |
| 要重排结构或规划某一节 | [03_章节结构规划_prompt.md](03_章节结构规划_prompt.md) | 先出结构和 section plan，不直接写段落 |
| 要起草或重写具体段落 | [04_段落起草_prompt.md](04_段落起草_prompt.md) | 每次只写一个 section 或 2-3 段 |
| 要检查方法论风险 | [05_方法论风险检查_prompt.md](05_方法论风险检查_prompt.md) | 对照证据和审阅风险 |
| 要根据已确认反馈执行修订 | [06_修订执行_prompt.md](06_修订执行_prompt.md) | 只改确认范围，不自动扩展 |

## 证据来源优先级

1. 用户提供的最新 Methodology draft 或 section draft。
2. 方法笔记 / pipeline docs / SOP（如有）。
3. 已经完成的 reading notes。
4. 已确认的项目事实（导师确认 / 已发表 / 已注册等）。
5. 仍未确认的内容必须标为 `[DETAIL NEEDED]` 或 `[ADVISOR CONFIRMATION NEEDED]`。

## 与其他分区的关系

- **审阅**：写完一轮后用 [审阅/03_Methodology审阅_prompt.md](../../审阅/03_Methodology审阅_prompt.md) 做诊断。
- **再审追踪**：改完用 [审阅/09_再审与回归追踪_prompt.md](../../审阅/09_再审与回归追踪_prompt.md) 抓退步。
- **跨章节一致性**：Methodology 改大后用 [审阅/10_跨章节一致性检查_prompt.md](../../审阅/10_跨章节一致性检查_prompt.md) 检查与 Lit Review / Results 的一致性。
