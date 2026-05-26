---
status: prompt
type: prompt
task: batch_organization_after_reading
use_when: "你已经攒了一批 Claude 写好的 reading note，要让 Codex / 另一个 LLM 统一整理 source 状态 / 补 links / 更新 index"
do_not_use_when: "还没有 reading note；要继续读新论文；要做综述写作"
input_required:
  - "一批 Single Reading Report + Upgrade Candidate 输出"
  - "你的 Obsidian Vault 路径或对应的 source / reading 笔记目录"
output: "一份批次整理清单：source status 更新 / links 补全 / index 更新 / Upgrade 候选分类"
stop_points:
  - "整理前先列出本批次涉及多少篇笔记，让用户确认范围"
  - "对于 Upgrade Candidate 中 confidence: high 的，先报告给用户，不自动升级"
quality_gates:
  - "不替用户提前决定 argument block / concept / method 的命名 / 边界"
  - "不删除 reading note 中的内容，只补 / 改 metadata 和 links"
  - "不发明 wikilinks 指向不存在的笔记"
related_prompts:
  - "04_单篇reading_note_5星4星3星_prompt"
  - "01_直接阅读已下载文献_prompt"
---

# 批次整理 prompt · Claude → Codex 交接

这份 prompt 配合 reading workflow 的分工设计：

- **Claude / 主 LLM 端**：负责阅读 + 写正式 reading note + 输出 Single Reading Report
- **Codex / 整理 LLM 端**：负责批量整理 source status、补 links、更新 index、把 Upgrade Candidate 分类
- **你**：在两端之间审稿，决定什么时候交接

这种分工的理由：让 Claude 一边读一边维护整个笔记库，结果常常是 Claude 同时改太多文件，越改越乱。把"阅读"和"整理"拆开，可以保持每次 LLM 调用的边界清晰。

## 复制给 Codex / 整理 LLM 的 prompt

```text
请整理下面这批 Claude 刚读完的文献。

## 任务边界

你只负责：
- 把 source note 的 read_status 从 unread 改为 read
- 在 source note 和 reading note 之间补必要的双向 wikilinks
- 更新 reading index / project map（如果存在）
- 把每条 Upgrade Candidate 按四类整理

你不要：
- 不要替我决定 argument block / concept / method 的最终命名
- 不要修改 reading note 的正文内容（只能加 metadata 和 links）
- 不要发明指向不存在笔记的 wikilinks
- 不要为了"看起来更完整"补造关系

## 工作目录

[你的 Obsidian Vault 根路径，例如 D:/MyVault]
├── 01_Sources/          ← 这里是 source note（轻量来源卡）
├── 02_Reading_Notes/    ← 这里是 reading note（精读笔记）
├── 03_Argument_Blocks/  ← 论证块（可能不存在，存在才更新）
├── 07_Project_Maps/     ← 项目地图（可能不存在）
└── 02_Reading_Notes/00_Reading_Notes_Reference_Index.md  ← reading index（如果你有）

## 输入：本批次的 Reading Reports

[把多条 Single Reading Report + Upgrade Candidate 贴在这里]

例如：

## Single Reading Report
completed: [[Smith_2024_Some_Paper]]
dialogue: [[Jones_2023_Other_Paper]], [[Brown_2022_Third_Paper]]
unsure: none

## Upgrade Candidate
candidate_type: method
confidence: high
reason: 这篇提供了一个可以直接用在我方法论章节的具体 pipeline

---

## Single Reading Report
completed: [[...]]
...

## 输出格式

请输出一份批次整理清单：

### A. Source Status 更新

| Source Note 文件名 | 旧状态 | 新状态 | 操作 |
|---|---|---|---|
| Smith_2024_Some_Paper.md | unread | read | 改 frontmatter read_status |

### B. Links 补全

| 文件 | 在哪里 | 补什么 link | 理由 |
|---|---|---|---|
| Smith_2024_Some_Paper.md (source) | frontmatter 或 Links Out | [[Smith_2024_Some_Paper]] (reading note) | source→reading 反向链 |
| Smith_2024_Some_Paper.md (reading) | "与既有文献对话" 区 | [[Jones_2023]], [[Brown_2022]] | dialogue 已在 report 中列出 |

如果某个 wikilink 指向的笔记**不存在**，必须标 [target not found]，不要补造。

### C. Reading Index 更新

如果存在 reading index，列出要新增的条目；按它的现有格式（不要重新设计格式）。

如果不存在 reading index，建议但不创建——除非用户明确要求。

### D. Upgrade Candidate 分类

按四类整理：

#### 1. Stay in reading note（保持在 reading 层，暂不升级）
- [[Smith_2024]] — reason

#### 2. Possible argument block 候选
- [[Smith_2024]] + [[Jones_2023]] + [[Brown_2022]] — 共同 question space: [一句话]
- 建议下一步：先让我看是否构成 block，不要直接建文件

#### 3. Possible concept 候选
- [[Smith_2024]] 引出概念："abductive analysis"
- 建议下一步：等再有 2-3 篇相关文献后再开 concept note

#### 4. Possible method 候选
- [[Smith_2024]] 提供方法 pipeline："X-aware pre-processing"
- 建议下一步：值得开 method note；先报给我确认

### E. 待用户决策

把 confidence: high 的 Upgrade Candidate 单独列出，等我决定：
- [[Smith_2024]] → method note? — high confidence
- ...

## 停下点

整理前先停下问：
1. 本批次涉及 N 篇 reading note，是否全部纳入整理？
2. 是否已经存在 reading index / project map 文件？路径是？
3. 是否需要我同时维护 03_Argument_Blocks / 05_Concepts / 06_Methods 目录？

确认后再开始整理。

## 输出原则

- 只整理 metadata 和 links，不改 reading note 正文
- 不发明不存在的 link target
- 不替用户提前决定 argument block / concept / method 的边界
- 高 confidence 的 Upgrade Candidate 单独报告，由用户决定
- 中低 confidence 的默认归入 "stay in reading note"
```

## 配套：Claude / Codex 分工速查

| 任务 | 谁来做 | 何时做 |
|---|---|---|
| 读 PDF | Claude / 主 LLM | 每篇都做 |
| 写 reading note | Claude / 主 LLM | 每篇都做 |
| 输出 Single Reading Report | Claude / 主 LLM | 每篇都做 |
| 输出 Upgrade Candidate | Claude / 主 LLM | 每篇都做 |
| 改 source read_status | Codex / 整理 LLM | 攒够一批后 |
| 补 wikilinks | Codex / 整理 LLM | 攒够一批后 |
| 更新 reading index | Codex / 整理 LLM | 攒够一批后 |
| 升级到 argument / concept / method | **用户决定**，Codex 只列候选 | 攒够 4-10 篇后 |
| 写 argument block | Claude / 主 LLM | 用户确认 block 成立后 |

## 为什么不让 Claude 一并整理

经验性总结：

- Claude 在写 reading note 的同时如果还要维护整个 vault 的状态，会出现：
  - 改链接时改坏其他笔记的 wikilink
  - 自己给概念命名（"abductive turn"）然后建一个浮空的 concept note
  - 把"暂未明确"的 Upgrade Candidate 强行升级为 argument block
- 分工后，Claude 专注阅读，Codex 专注整理，结构变化都经过用户确认

这条经验是 evil-thesis 阅读子模块的基础设计假设，不要为了"简化"撤掉这层分工。

## 频率建议

- 攒 5-10 篇 reading note 后跑一次本 prompt
- 或者一周整理一次
- 不要每篇读完就跑整理——会破坏 Claude / Codex 的工作节奏，也容易让你在没有足够 reading note 时被迫提前决定 argument block 的边界

## 与下游写作的关系

整理完一批后，如果某些 reading notes 在 "Possible argument block 候选" 里聚成了一组，下一步是去 `写作/` 分区找 argument block 起草 prompt（如果 evil-thesis 主仓库已有）或继续读补足。
