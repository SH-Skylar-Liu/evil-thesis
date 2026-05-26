---
status: prompt
type: prompt
task: search_within_existing_notes
use_when: "在已有 Obsidian reading notes / source notes 里搜索：'我读过哪些笔记讨论了 X？''哪几篇引用了 Y 作者？''哪些笔记被标为 4-5 星且属于 methodology 领域？'"
do_not_use_when: "要在外网找新文献（用 02 / 06 / 脚本/）；要写新的 reading note（用 04）；要归纳找到的笔记之间的分歧（用 09）"
input_required:
  - "搜索查询（关键词 / 作者 / 标签 / 领域名）"
  - "搜索类型（按关键词 / 按作者 / 按标签 / 按相关度 / 按领域 / 混合）"
  - "你的 Obsidian Vault 中要搜索的目录（如 02_Reading_Notes/，可多个）"
output: "按相关性排序的笔记列表，含文件名 wikilink + 命中行 + 元信息（作者/年份/相关度/领域）"
stop_points:
  - "搜索完成后停下，不要自动去读找到的笔记 — 等用户挑出要进一步处理的"
  - "命中数 > 30 时，先停下问用户要不要加更窄的 filter"
quality_gates:
  - "只搜用户指定目录，不擅自扩到整个 Vault"
  - "不读笔记正文细节（只取 frontmatter + 命中行）— 这是检索不是精读"
  - "wikilink 必须基于实际文件名生成，不发明不存在的笔记"
  - "frontmatter 字段缺失时直接显示 '—'，不要补造"
failure_modes:
  - "命中数 = 0 时给出搜索建议（同义词、放宽查询、扩大目录），不要假装找到"
  - "目录不存在时直接报错，不要换目录假装继续"
  - "如果 grep 工具不可用，明确说'我没有文件系统访问权限，请把笔记内容贴给我或导出文件名列表'"
related_prompts:
  - "09_多笔记关系归纳与分歧_prompt"
  - "07_批次整理_Codex_prompt"
  - "04_单篇reading_note_5星4星3星_prompt"
---

# 笔记内检索 prompt

这份 prompt 解决一个具体问题：**你已经有几十上百篇 reading notes，想问"我读过哪些笔记讨论了 X？"** —— 不是要找新文献（那是 02 / 06 / 脚本/），而是回到自己的库里查。

它是 evilread 原 `paper-search` skill 的脱敏 + 泛化版本：

- 原版写死了 `20_Research/Papers/` 路径
- 本版让你每次告诉 LLM 在哪个目录搜，支持任何 Vault 结构

## 复制给 LLM 的 prompt

```text
请在我的 Obsidian Vault 里搜索 reading notes / source notes，按相关性排序输出结果。

## 任务边界

你只负责：
- 在我指定的目录里 grep / glob 找匹配笔记
- 提取每篇命中笔记的 frontmatter 元信息
- 提取命中行（关键词上下文）
- 按相关性评分排序输出

你不要：
- 不要读笔记正文细节（这是检索不是精读）
- 不要去外网找新文献
- 不要自动去深入分析找到的笔记
- 不要发明不存在的笔记文件名
- 不要扩到我指定范围之外的目录

## 输入

### 搜索查询
[你的关键词 / 作者名 / 标签 / 概念，例如："abductive analysis" 或 "Foucault" 或 "#multimodal"]

### 搜索类型（可多选）
- [ ] 按关键词（在标题 + 正文内容中搜）
- [ ] 按作者（在 frontmatter authors / 文件名中搜）
- [ ] 按标签（在 frontmatter tags 中搜）
- [ ] 按相关度（如 `relevance: 5★` 或 `relevance: 4★`）
- [ ] 按领域（在 frontmatter field 中搜）
- [ ] 按状态（如 `status: read` / `status: unread`）

### 搜索目录（必填，可多个）
[绝对路径或相对于 Vault 根的路径，例如：
- D:/MyVault/02_Reading_Notes/
- D:/MyVault/01_Sources/
不要默认目录——让我告诉你搜哪里]

### 可选过滤
- 排除关键词（命中标题或正文则跳过）：[]
- 只看相关度 ≥：[3★ / 4★ / 5★]
- 只看 status：[read / unread / all]
- 时间范围（按 created 字段）：[YYYY-MM-DD ~ YYYY-MM-DD]

## 搜索策略

1. **按关键词搜**：用 grep -i 在指定目录下 `*.md` 文件里搜词；同时搜文件名
2. **按作者搜**：grep frontmatter 的 `authors:` 字段 + 文件名（很多笔记文件名以作者命名）
3. **按标签搜**：grep frontmatter 的 `tags:` 字段 + 正文中的 `#tag`
4. **按相关度搜**：grep frontmatter 的 `relevance:` 字段
5. **按领域搜**：grep frontmatter 的 `field:` 字段

混合搜索时，每条结果至少要命中一个搜索维度，命中越多维度排名越前。

## 相关性评分（用于排序）

| 命中位置 | 加分 |
|---|---|
| 标题（文件名）匹配 | +10 |
| frontmatter authors 匹配 | +8 |
| frontmatter title 匹配 | +7 |
| frontmatter tags 匹配 | +5 |
| frontmatter field 匹配 | +4 |
| 正文匹配（每行 +1，最多 +6） | +1 ~ +6 |
| frontmatter relevance ≥ 4★ | +2（已是关键文献的优先） |

## 输出格式

按"领域"或"相关度"分组（你选一个），每组内按总分降序：

```markdown
## 笔记内检索结果

**搜索查询**: [关键词]
**搜索类型**: [按关键词 / 按作者 / ...]
**搜索目录**: [...]
**命中笔记总数**: N

### 分组 A · [领域名 / 相关度] (N 篇)

#### 1. [[文件名]] — score: X
- **作者**: ... 
- **年份**: 2024
- **相关度**: 4★
- **领域**: Digital Humanities
- **标签**: [tag1, tag2]
- **命中位置**:
  - 标题中: 关键词出现
  - 正文 L12: "...the abductive analysis approach..."
  - 正文 L48: "...as Timmermans and Tavory argue..."

#### 2. [[文件名]] — score: X
- ...

### 分组 B · [...] (N 篇)
...

## 搜索覆盖说明

- 实际搜索的目录: [...]
- 跳过的文件 (例如非 reading note): [...]
- 没有 frontmatter 元信息的笔记: N 篇（已用 '—' 占位）

## 下一步建议

如果命中数很多 (> 10)，建议：
- 缩窄关键词
- 加 relevance ≥ 4★ 过滤
- 或选其中 4-10 篇用 09_多笔记关系归纳与分歧_prompt 做下一步分析

如果命中数 = 0，建议：
- 试 [同义词1] / [同义词2]
- 扩大目录到 [...]
- 检查你的笔记里是否真的有这个概念（也许你以为读过其实没写到笔记里）
```

## 边界

- 不要读命中笔记的完整正文 — 那是 `09_多笔记关系归纳与分歧_prompt.md` 的事
- 不要去外网查这些笔记的原始文献 — 这是检索不是补全
- 不要给找到的笔记打"我的简评" — 那应该已经在笔记的 `## 我的简评` 段落里

## 输出后的停下点

输出搜索结果后停下，问我：
"找到 N 篇命中笔记。下一步：(a) 把哪几篇用 09 prompt 做关系归纳？(b) 还是只是查询，不做下一步？"
等我回复再继续。

## 输入

[在这里填上面的搜索查询、类型、目录、过滤条件]
```

## 与下游 prompt 的关系

- 命中结果 →（选 4-10 篇）→ `09_多笔记关系归纳与分歧_prompt.md` 做归纳
- 命中某一篇值得复读 → `01_直接阅读已下载文献_prompt.md`（如果只读过摘要级）或 `04_单篇reading_note_5星4星3星_prompt.md`（重写笔记）
- 命中结果发现某一篇 source note 还未读 → 把它加进 `_Tools/reading-workflow-progress.md` 队列

## 与 evilread 原 paper-search skill 的差异

| 维度 | 原版 paper-search skill | 本 prompt 版 |
|---|---|---|
| 搜索目录 | 写死 `20_Research/Papers/` | 用户每次指定 |
| 触发方式 | Claude Code skill 调用 | 任何 LLM 复制 prompt |
| 输出位置 | 写死格式 | 可调（按领域 / 按相关度分组） |
| 评分维度 | 5 维（标题/内容/作者/领域/标签） | 7 维（加 frontmatter title / relevance ≥ 4★） |
| 停下点 | 无（直接输出全部） | 命中 > 30 先停下确认 |

如果你已经把 paper-search skill 装到 Claude Code 里且 Vault 结构与原版一致，**直接用 skill 更省事**；本 prompt 是给跨工具 / 跨 vault 结构用户的便携版本。
