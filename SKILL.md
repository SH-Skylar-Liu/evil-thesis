---
name: thesis-skills
description: |
  研究生毕业论文 / 学位论文支持工具包：文献阅读、研究规划、章节写作
  （Introduction / Literature Review / Methodology / Results / Discussion /
  Conclusion）、与结构化学术审阅。当用户提到「硕士论文 / 毕业论文 / thesis
  写作 / 学位论文 / 文献综述 / methodology / results 章节 / discussion /
  conclusion / 审稿 / 引用核查 / 学术英文润色 / 论文压力测试」等场景时调用。
  也适用于 taught postgraduate dissertation 与 research master 论文。
  不要在用户只是问一般写作问题（如「这段话怎么改」）时主动触发——只在涉及
  thesis 工作流的具体阶段（规划、读、写章节、审章节、改稿）时激活。
metadata:
  type: skill
  audience: graduate / master's / research postgraduate students
  language: 中文（交互）+ 英文（学术输出）双语
---

# Thesis Skills — 研究生毕业论文工作流工具包

这是一个**按真实任务分区**的 prompt 库，不是单个一次性 prompt。每个分区里的文件都是一份可复制给 LLM 的完整 prompt，配合 frontmatter 里的 `use_when` / `do_not_use_when` / `stop_points` / `quality_gates` 使用。

## 一分钟上手

1. 不知道用哪个？看 [使用指南.md](使用指南.md)。
2. 找具体 prompt？看分区里的 `00_*_INDEX.md`。
3. 开始任何写作前，先用 [项目背景/快速上下文加载器_prompt.md](项目背景/快速上下文加载器_prompt.md) 把研究背景给 LLM。
4. 大部分 prompt 在关键节点会**停下来等你确认**——这是设计，不是卡壳。
5. 默认不写盘：规划、搜索、候选筛选先在对话里输出，确认后再存。

## 一条研究流水线

```text
模糊想法 / 导师反馈 / 课程任务
      ↓  研究规划（这个问题值不值得做？怎么变成可研究问题？）
   研究方向 + Research Planning Brief
      ↓  阅读（读什么、找什么、写 reading note）
   reading notes + Reading Handoff
      ↓  写作（证据 → 结构 → 段落）
   章节草稿（Intro / LitReview / Methodology / Results / Discussion / Conclusion）
      ↓  审阅（诊断 / 压力测试 / 引用 / 一致性）
   审阅报告
      ↓  修订（只改确认范围）→ 审阅/再审追踪
   下一稿
```

不确定自己在哪一段、为什么读/写这些时，**回上游一段**——多半是规划没做够。

## 分区一览

| 分区 | 任务 | 入口 |
|---|---|---|
| 项目背景 | 给 LLM 加载你的研究上下文 | [项目背景/00_项目背景_INDEX.md](项目背景/00_项目背景_INDEX.md) |
| 研究规划 | 把模糊想法变成可研究子问题；规划小论文/会议投稿 | [研究规划/00_研究规划_INDEX.md](研究规划/00_研究规划_INDEX.md) |
| 阅读 | 读 PDF、按相关度（5★/4★/3★）分模板、关键词组合生成、Semantic Scholar / arXiv 检索、批次整理、笔记内检索、多笔记关系归纳 | [阅读/00_阅读_INDEX.md](阅读/00_阅读_INDEX.md) |
| · 阅读模板 | 5★/4★ 增强版 + 3★ 轻量版 reading note 模板 | [阅读/模板/](阅读/模板/) |
| · 阅读脚本 | Python 检索脚本（Semantic Scholar / arXiv） | [阅读/脚本/](阅读/脚本/) |
| · Vault 起步包 | 给 fork 用户的最小可用 Obsidian Vault（含 2 篇示范笔记） | [阅读/Obsidian_Vault_起步包/](阅读/Obsidian_Vault_起步包/) |
| 写作 | 章节起草、润色、引用格式、章节拼装 | [写作/00_写作_INDEX.md](写作/00_写作_INDEX.md) |
| · Methodology | 方法论章节的完整六步 workflow | [写作/Methodology/00_Methodology_INDEX.md](写作/Methodology/00_Methodology_INDEX.md) |
| · Results | 结果/分析章节的叙事化写作 | [写作/Results/00_Results_INDEX.md](写作/Results/00_Results_INDEX.md) |
| · Discussion | 讨论章节：与文献对话 + 解释发现 + 限制 | [写作/Discussion/00_Discussion_INDEX.md](写作/Discussion/00_Discussion_INDEX.md) |
| · Conclusion | 结论章节：回应研究问题 + 综合贡献 | [写作/Conclusion/00_Conclusion_INDEX.md](写作/Conclusion/00_Conclusion_INDEX.md) |
| 审阅 | 通用审阅、文献综述/Methodology/Results/Discussion/Conclusion 专项审阅、引用核查、压力测试、再审 | [审阅/00_审阅_INDEX.md](审阅/00_审阅_INDEX.md) |
| 工作流 | Prompt 标准与实验/数据记录 | [工作流/00_工作流_INDEX.md](工作流/00_工作流_INDEX.md) |

## 全系统共享的纪律层

这套 prompt 之所以可信，靠的是几条贯穿各区的机制：

| 机制 | 作用 | 主要在哪 |
|---|---|---|
| 材料 / 知识隔离 | 只用你给的真实材料和眼前文本，不用模型记忆补全 | 全区 |
| 反谄媚 | 不达标就说不达标，不为取悦你抬高评价 | 规划 / 审阅 / 写作 |
| 停下点（checkpoint） | 改变方向 / 文件 / 优先级前必停，等你确认 | 全区 |
| Socratic 引导 + FINER | 想法太模糊时先提问引导；候选用 FINER 评分 | 研究规划 |
| Devil's Advocate + 让步阈值 | 选定方向 / 论点后先攻击；不被你一辩解就软化 | 规划、审阅压力测试 |
| 分级量表 + 盲评预承诺 | 读稿前先定标尺，再按达标/部分/不达标评级 | 审阅 |
| Claim 出处级锚定 | 每个 claim 标来源，区分"文献说的"vs"我的解读" | 写作、Methodology 链路 |
| 存在性核验（三库） | 候选 / 引用须在 SemanticScholar/OpenAlex/Crossref 核到 | 阅读、引用核查 |
| 回归追踪 | 对比上一轮，专抓"改出来的退步" | 审阅再审 |

## 标记约定

prompt 输出里出现这些方括号标记时，是 LLM 在**主动暴露不确定**：

| 标记 | 含义 | 你该做什么 |
|---|---|---|
| `[需核实]` | 模型推测，不是你确认的事实 | 自己核一下再用 |
| `[来自记忆，需核实]` | 来自训练记忆，而非眼前文本 | 回原文核对 |
| `[CITATION NEEDED]` / `[DETAIL NEEDED]` | 缺证据 / 缺细节 | 补来源或材料 |
| `[未核实，可能不存在]` | 引用没在三库核到 | 怀疑是假引用，核实或删 |
| `[推断]` / `[我的推断]` | 这是解读，不是文献原话 | 决定是否接受这个解读 |
| `[ADVISOR CONFIRMATION NEEDED]` | 需导师确认 | 开会时问 |
| `[缺：字段名]` | 引用格式转换缺字段 | 补字段，别让它编 |

**原则**：这些标记是功能，不是 bug。LLM 宁可标不确定也不编造——你的工作是把它们一个个清掉。

## 双语输出

国际研究生论文常需要中英对照来核对意思与导师反馈。本工具包默认：

- **学术正文**：英文为主，紧接 `**中文：**` 精准转述（不是泛泛翻译）。
- **对话与解释**：中文为主。
- **可调整**：如果你只写中文论文，复制 prompt 时把"双语"改成"中文"即可；纯英文论文同理。

## 安装与上传

这是一个 prompt 库，不是可执行代码——你可以：

- 直接当成文件夹引用（在 Claude / ChatGPT / Cursor 里粘贴对应 prompt）；
- 推到 GitHub 作为公开仓库给其他研究生用；
- 在 Claude Code 里把它注册成 Skill（参考 [claude-code-skills](https://docs.anthropic.com/claude-code) 文档）。
