---
status: active
type: prompt_index
---

# 阅读 Prompt 索引

阅读子模块覆盖 **从找文献到写正式 reading note 到批次整理** 的完整链路。

## 任务路由表

| 你的状态 | 用哪个 prompt | 说明 |
|---|---|---|
| 我有模糊方向 / 章节困惑 / 导师反馈，但还不知道该读什么 | [../研究规划/01_子问题与章节方向规划_prompt.md](../研究规划/01_子问题与章节方向规划_prompt.md) | 先做研究规划，再决定阅读路线 |
| 我已经有 PDF / Zotero 文献，只要 LLM 读 | [01_直接阅读已下载文献_prompt.md](01_直接阅读已下载文献_prompt.md) | 最普通的单篇阅读 |
| 我只有关键词 / 主题，要先找文献再读 | [02_关键词检索下载评分阅读_prompt.md](02_关键词检索下载评分阅读_prompt.md) | 先搜索，再筛选，再读 |
| 我有审稿意见 / 导师反馈，要从反馈反推 gap 再补文献 | [03_根据反馈找Gap并补文献_prompt.md](03_根据反馈找Gap并补文献_prompt.md) | 反馈驱动的补文献流程 |
| 我有 PDF，要让 LLM 按相关度 5★/4★/3★ 选模板写 reading note | [04_单篇reading_note_5星4星3星_prompt.md](04_单篇reading_note_5星4星3星_prompt.md) | 防止所有论文都被压成同款短卡 |
| 我有一个 gap，要让 LLM 把它拆成可执行的关键词组合 | [05_关键词组合自动生成_prompt.md](05_关键词组合自动生成_prompt.md) | 把模糊需求翻译成 query |
| 我要用真实 API（Semantic Scholar / arXiv）检索文献 | [06_Semantic_Scholar_arXiv_检索协议.md](06_Semantic_Scholar_arXiv_检索协议.md) | 操作规范 + prompt 框架 |
| 我攒了一批 reading note，要让另一个 LLM 整理状态和 links | [07_批次整理_Codex_prompt.md](07_批次整理_Codex_prompt.md) | Claude → Codex 交接 |
| 我想问"我读过哪些笔记讨论了 X" | [08_笔记内检索_prompt.md](08_笔记内检索_prompt.md) | 在已有 Vault 笔记内检索（不是去外网找新文献） |
| 我有 4-10 篇笔记，想知道它们之间的共识 / 分歧 / gap | [09_多笔记关系归纳与分歧_prompt.md](09_多笔记关系归纳与分歧_prompt.md) | 问题空间式归纳 + argument block 候选 |

## 三条典型链路

### 链路 A · 我已经有 PDF，只想读

```text
01_直接阅读已下载文献_prompt.md     ← 入口
（如果想按相关度分模板）
04_单篇reading_note_5星4星3星_prompt.md
（攒够一批后）
07_批次整理_Codex_prompt.md
```

### 链路 B · 我只有主题，要先找再读

```text
05_关键词组合自动生成_prompt.md     ← 入口
06_Semantic_Scholar_arXiv_检索协议.md
02_关键词检索下载评分阅读_prompt.md
04_单篇reading_note_5星4星3星_prompt.md
07_批次整理_Codex_prompt.md
```

### 链路 C · 我有审稿反馈，要补 gap

```text
03_根据反馈找Gap并补文献_prompt.md   ← 入口（先拆 gap）
05_关键词组合自动生成_prompt.md      （把 gap 转成关键词）
06_Semantic_Scholar_arXiv_检索协议.md
02_关键词检索下载评分阅读_prompt.md
04_单篇reading_note_5星4星3星_prompt.md
07_批次整理_Codex_prompt.md
```

### 链路 D · 我已经读过一批，要从已有笔记里挖结构

```text
08_笔记内检索_prompt.md              ← 入口（在已有笔记中找）
09_多笔记关系归纳与分歧_prompt.md     （把找到的 4-10 篇做归纳）
（如归纳出 argument block 候选）→ 写作/ 或主仓库的论证起草 prompt
```

这条链路不去外网，全部在你的 Vault 内运行。适合：
- 写作前梳理"我手上有什么"
- 回应导师"X 部分的文献你读过哪些？立场是什么？"
- 跨章节查"哪些笔记可以同时支持 ch3 和 ch5"

## Routing discipline

- 还说不清"为什么读这些文献"？先去 [../研究规划/01_子问题与章节方向规划_prompt.md](../研究规划/01_子问题与章节方向规划_prompt.md)。
- 已经有 4-10 篇 reading notes？不要继续搜索 / 继续读，转去写作系统。
- LLM 直接帮你搜文献容易凭记忆造假——任何检索都要走 06 协议或 `脚本/`，不允许 LLM 凭记忆补 citations。

## 配套资产

阅读子模块除了 prompt 之外还提供：

### 模板 — `模板/`
- `TPL_Reading_Note_5星4星.md` — 增强版精读笔记模板
- `TPL_Reading_Note_3星.md` — 轻量版精读笔记模板
- `TPL_Source_Note.md` — 来源卡模板
- `README.md` — 怎么挂到 Obsidian Templater

### 脚本 — `脚本/`
- `search_semantic_scholar.py` — Semantic Scholar API 检索（带速率退避）
- `search_arxiv.py` — arXiv API 检索
- `requirements.txt`
- `config.example.yaml`
- `README.md` — 如何运行 + 关键词配置 + 环境变量

### Obsidian Vault 起步包 — `Obsidian_Vault_起步包/`
- 一个可以直接用 Obsidian 打开的最小 vault
- 含目录结构 / 4 个模板 / 1 个 4-5★ 示范笔记 / 1 个 3★ 示范笔记 / 给 Claude 的全局指令模板

## 防幻觉护栏（所有 prompt 通用）

1. **知识隔离**：只依据用户提供的眼前材料；凭记忆得出的内容必须标 `[来自记忆，需核实]`
2. **引用存在性核验**（02 / 03 / 05 / 06）：候选文献须在 Semantic Scholar / OpenAlex / Crossref 至少一库核到才入表，核不到标 `[未核实，可能不存在]`
3. **来源质量分级**（02 / 03）：候选表用「来源·核验」列把来源质量与相关度分开
4. **核心发现带出处**（01 / 04）：reading note 中的关键判断必须标 section / 页码
5. **不替用户决策**（07）：批次整理只列候选，不替用户提前决定 argument block / concept / method 的边界

## Reading Handoff（交接格式）

研究规划或候选筛选完成后，建议用这个格式交接到具体阅读 prompt：

```markdown
## Reading Handoff

- source task:
- confirmed direction:
- confirmed papers:
- reading order:
- PDF / Zotero status:
- special focus:
- stop after:
```

## 标记约定

阅读 prompt 输出里出现这些方括号标记是 LLM 在**主动暴露不确定**：

| 标记 | 含义 | 你该做什么 |
|---|---|---|
| `[需核实]` | 模型推测 | 自己核一下再用 |
| `[来自记忆，需核实]` | 来自训练记忆而非眼前文本 | 回原文核对 |
| `[未核实，可能不存在]` | 引用没在三库核到 | 怀疑是假引用，核实或删 |
| `[推断]` | LLM 解读，不是文献原话 | 决定是否接受这个解读 |
| `[CITATION NEEDED]` | 缺证据 | 补来源 |
| `[ADVISOR CONFIRMATION NEEDED]` | 需导师确认 | 开会时问 |

## 与 evilread 原 skill 的关系

阅读子模块整合自 [juliye2025/evil-read-arxiv](https://github.com/juliye2025/evil-read-arxiv) 的 Claude Code skills（`paper-analyze` / `paper-search` / `start-my-day` / `conf-papers` / `extract-paper-images`），但只保留了 reading note 工作流真正用得到的功能：

- ✅ 保留：用 Semantic Scholar / arXiv API 主动检索新文献（脚本 + prompt 双版）；按相关度分级写 reading note；关键词组合生成；**在已有笔记内检索**（paper-search 脱敏版 → `08`）
- ✅ 简化：剥离了"每日自动推荐"和"知识图谱可视化"——这些功能放大了 LLM 幻觉风险，且大部分用户用不到
- ✅ 新增：5★/4★/3★ 分层模板；Claude / Codex 分工；批次整理 prompt；**多笔记关系归纳**（`09`，从"读完了"到"能写"之间的关键一步）
- ❌ 不再依赖：硬编码的 Vault 路径——全部走环境变量 / 占位符
