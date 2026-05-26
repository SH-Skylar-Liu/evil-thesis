---
status: active
type: prompt_index
---

# Discussion 章节写作 Workflow Index

Discussion 章节做四件事：

1. **解释发现**（不是重述 Results）；
2. **与文献对话**（自己的发现支持 / 修正 / 挑战已有研究的什么）；
3. **承认限制**（不是 self-flagellation，是 epistemic honesty）；
4. **指出 implications**（理论 / 方法 / 实践层面，分清楚）。

最容易写糟的地方是：
- 重复 Results（"as shown in Chapter 4, ..."）；
- over-interpretation（数据撑不起的解读）；
- 假装与文献对话（其实只是堆 citation）。

## 核心链路

```text
Results draft + reading notes + RQ
        ↓
01 Discussion 写作配置
        ↓
02 Discussion 证据包生成（findings ↔ literature 映射）
        ↓
03 Discussion 章节结构规划
        ↓
04 Discussion 段落起草（与文献对话 / 解释 / 限制 / implications）
        ↓
05 Discussion 风险检查（over-interpretation / 重复 Results / 伪对话）
        ↓
06 Discussion 修订执行
```

## 怎么选

| 场景 | 用哪个 |
|---|---|
| 开始一轮 Discussion 写作 | [01_写作配置_prompt.md](01_写作配置_prompt.md) |
| 把 findings 和文献建立映射 | [02_证据包生成_prompt.md](02_证据包生成_prompt.md) |
| 规划 Discussion 节序 | [03_章节结构规划_prompt.md](03_章节结构规划_prompt.md) |
| 起草段落（与文献对话 / 解释 / 限制） | [04_段落起草_prompt.md](04_段落起草_prompt.md) |
| 检查 over-interpretation / 伪对话 | [05_Discussion风险检查_prompt.md](05_Discussion风险检查_prompt.md) |
| 执行修订 | [06_修订执行_prompt.md](06_修订执行_prompt.md) |

## Discussion 铁律

1. **不重复 Results**：可以 briefly remind ("the finding that X..."），但不能把 Results 段落复制过来。
2. **真对话，不堆 citation**：每个引用必须说出"和我的发现什么关系"——支持 / 部分支持 / 修正 / 反驳 / 揭示 gap。
3. **解释要带因果界限**：可以说 "this is consistent with X explanation" 或 "one possible reading is Y"，
   但不能滑到 "this proves Y"。
4. **限制 ≠ 自责**：limitation 要说明影响了什么 claim，以及如何 future work 可以 mitigate。
5. **implications 分层**：theoretical / methodological / practical / policy 不要混在一起。
