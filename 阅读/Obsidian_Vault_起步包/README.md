# Obsidian Vault 起步包

这是一个**可以直接用 Obsidian 打开**的最小 Vault 模板，专门服务 reading note 工作流。

适合：第一次想试 evil-thesis 阅读子模块的人；或想要一个干净的 reading-only Vault 跟主 Vault 分开的人。

## 怎么开始

### 1. 复制目录

把 `Obsidian_Vault_起步包/` 整个复制到你想要的位置（不要直接用 GitHub 仓库目录当 Vault，避免 .git / .gitignore 混乱）：

```bash
# Windows PowerShell
Copy-Item -Recurse "D:\GitHub\evil-thesis\阅读\Obsidian_Vault_起步包" "D:\MyReadingVault"

# macOS / Linux
cp -r evil-thesis/阅读/Obsidian_Vault_起步包 ~/MyReadingVault
```

### 2. 用 Obsidian 打开

- 打开 Obsidian
- 左下角 "Open another vault"
- 选择 "Open folder as vault"
- 选你刚才复制出去的目录

Obsidian 会自动建 `.obsidian/` 配置目录。

### 3. 改占位符

打开两篇示范笔记：

- `02_Reading_Notes/Example_5star_Smits_Wevers_2023.md`
- `02_Reading_Notes/Example_3star_Morgan_2007.md`

里面所有 `[YOUR_PROJECT_NAME]` / `[YOUR_CHAPTER]` / `[YOUR_GAP_1]` / `[YOUR_LOCAL_PATH]` 等占位符替换成你自己的术语。这些示范的目的是让你看到模板填到位时的密度，而不是直接用。

### 4. 把模板挂到 Templater（可选）

如果你装了 [Templater](https://github.com/SilentVoid13/Templater) 插件：

- 设置 → Templater → Template folder location → `99_Templates`
- 之后新建 reading note 时按 `Ctrl/Cmd + P` 调出命令面板，输入 "Templater: Open Insert Template Modal"
- 选 `TPL_Reading_Note_5星4星` 或 `TPL_Reading_Note_3星`

不装 Templater 也可以——直接复制粘贴 `99_Templates/*.md` 内容到新文件即可。

### 5. 修改 00_meta/CLAUDE.md.example

这是给 Claude（或其他 LLM）的全局上下文模板。改成你自己的：

- 复制成 `00_meta/CLAUDE.md`
- 替换里面的研究领域、术语、Vault 路径
- 之后在 Claude / Claude Code 里跑 reading prompt 时，对方会自动读取这个文件

---

## 目录结构

```
Obsidian_Vault_起步包/
├── README.md                                     ← 你正在看
├── 00_meta/
│   └── CLAUDE.md.example                         ← 给 Claude/LLM 的全局指令模板
├── 01_Sources/                                   ← 来源卡（轻量登记，未精读）
│   └── .gitkeep
├── 02_Reading_Notes/                             ← 精读笔记（主工作区）
│   ├── Example_5star_Smits_Wevers_2023.md        ← 4-5★ 示范笔记
│   └── Example_3star_Morgan_2007.md              ← 3★ 示范笔记
├── 99_Templates/                                 ← Obsidian Templater 用
│   ├── TPL_Reading_Note_5星4星.md
│   ├── TPL_Reading_Note_3星.md
│   └── TPL_Source_Note.md
└── _Tools/
    └── reading-workflow-progress.md.example      ← 跨会话进度跟踪模板
```

## 流转主线

按 evil-thesis 阅读子模块设计：

```text
00_Inbox（你自己加）
   ↓ 用 SOP A 登记
01_Sources（轻量来源卡）
   ↓ 用 SOP B + reading prompt（01 或 04）
02_Reading_Notes（精读笔记，主工作产物）
   ↓ 攒一批后用 07_批次整理_Codex_prompt.md
分类成 Upgrade Candidate
   ↓ 用户决定是否升级（不自动建）
03_Argument_Blocks / 05_Concepts / 06_Methods（这个起步包默认不建）
```

如果你以后需要 `03_Argument_Blocks / 04_Writing_Projects` 等更完整的目录，参考 evil-thesis 主仓库的 `写作/` 分区。

## 三种典型用法

### 用法 A · 只想试一下 prompt

不动 Vault 文件，直接打开 `evil-thesis/阅读/04_单篇reading_note_5星4星3星_prompt.md`，把 prompt 粘给 Claude，让它在对话里直接生成笔记 — 满意了再保存到 `02_Reading_Notes/`。

### 用法 B · 把这个 Vault 当主工作区

按上面"怎么开始"四步，作为日常 reading note 主 Vault。所有读完的文献都进 `02_Reading_Notes/`。

### 用法 C · 把这个 Vault 当 sandbox

主 Vault 在别处，这个 Vault 用来试验新 prompt / 新模板，验证后再迁回主 Vault。

## 与 evil-thesis 主仓库的关系

这个起步包是 evil-thesis 阅读子模块的**配套示范**，不是独立项目。所有 prompt 和操作说明仍然在主仓库的 `阅读/` 目录下。

如果你想要更完整的论文工作流（不只是阅读，还要写作 / 审阅 / 研究规划），看 evil-thesis 主仓库的 `SKILL.md` 和 `使用指南.md`。

## 不包含什么

明确**不包含**的目录（按需自己加）：

- `00_Inbox/` — 收纳还没登记的文献；建议自己加
- `03_Argument_Blocks/` — 论证块；攒够 4-10 篇相关 reading note 后再建
- `04_Writing_Projects/` — 章节草稿；属于写作系统，不在 reading 范围
- `05_Concepts/` `06_Methods/` `07_Project_Maps/` — 升级层；不要预先建空目录
- `09_Daily_Research_Log/` — 日记；个人选择，建不建都行

evil-thesis 阅读子模块的设计原则是 **"先决策，再写入"** — 等你真有 reading note 要进入 argument block 时再建对应目录，不要先建好空架子诱使自己强行升级。
