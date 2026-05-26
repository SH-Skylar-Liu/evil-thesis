---
status: active
type: prompt_index
---

# 写作 Prompt 索引

写作分区有两类：

1. **章节专用 workflow**（按论文结构组织）；
2. **通用工具**（润色、引用格式、章节拼装、摘要 & Introduction 起草）。

## 章节专用 workflow

| 章节 | 入口 | 何时用 |
|---|---|---|
| **Methodology** | [Methodology/00_Methodology_INDEX.md](Methodology/00_Methodology_INDEX.md) | 写 / 改方法论章节 |
| **Results / Analysis** | [Results/00_Results_INDEX.md](Results/00_Results_INDEX.md) | 写 / 改结果或分析章节 |
| **Discussion** | [Discussion/00_Discussion_INDEX.md](Discussion/00_Discussion_INDEX.md) | 写 / 改讨论章节 |
| **Conclusion** | [Conclusion/00_Conclusion_INDEX.md](Conclusion/00_Conclusion_INDEX.md) | 写 / 改结论章节 |

每个章节 workflow 都遵循同样的六步：

```text
写作配置 → 证据包 → 结构规划 → 段落起草 → 风险检查 → 修订执行
```

不同章节有不同的"风险检查"重点（例如 Methodology 检查可复现性，Discussion 检查 over-claiming）。

## 通用工具

| 场景 | 文件 | 何时用 |
|---|---|---|
| 起草摘要 / 章节 Introduction | [通用工具/02_摘要与Introduction起草_prompt.md](通用工具/02_摘要与Introduction起草_prompt.md) | thesis / chapter abstract、Introduction 节 |
| 学术英文润色 | [通用工具/01_学术英文润色_prompt.md](通用工具/01_学术英文润色_prompt.md) | 已有内容，要把语言提升到学术水准 |
| 引用格式互转（APA / Chicago / MLA / Harvard…） | [通用工具/03_引用格式转换_prompt.md](通用工具/03_引用格式转换_prompt.md) | 投稿换 venue / 统一全文格式 |
| 把多段拼成一节 | [通用工具/04_章节拼装_prompt.md](通用工具/04_章节拼装_prompt.md) | 已有段落草稿，要拼成连贯节段 |

## 写作链路

无论哪个章节，推荐链路：

```text
Reading notes / data notes / 已有材料
        ↓
Evidence Pack（claim-evidence 映射）
        ↓
Section Plan
        ↓
Paragraph Draft
        ↓
Risk Check
        ↓
Revision
```

## 全局写作规范

- **双语**：英文正文 + `**中文：**` 转述。如只写中文论文，复制 prompt 时改为纯中文。
- **避免 banned words**：significant / crucial / robust / leverage / nuanced / delve / foundational / definitive / most cutting-edge / it is worth noting / importantly；以及中文"值得注意的是 / 显著 / 至关重要 / 不可忽视的是"。
- **不用机械序列词**：firstly / secondly / thirdly，"首先 / 其次 / 再次"。
- **不用破折号** em dash 作为论证连接；用句号或冒号。
- **每句有明确主语**。
- **长短句交替**。
- **claim 必须有出处**：缺则标 `[CITATION NEEDED]` / `[DETAIL NEEDED]`，不要凭记忆写。
