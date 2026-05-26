# 模板 · Reading Note Templates

这个目录里的 3 个模板对应 reading workflow 的三种文件：

| 文件 | 何时用 |
|---|---|
| `TPL_Reading_Note_5星4星.md` | 高相关核心文献的增强版精读笔记 |
| `TPL_Reading_Note_3星.md` | 中等相关文献的轻量版精读笔记 |
| `TPL_Source_Note.md` | 来源卡（轻量登记，未精读时用） |

## 两种 reading note 模板的区别

| 维度 | 5★/4★ 增强版 | 3★ 轻量版 |
|---|---|---|
| 用途 | 以后反复调用、会进主论证 / 方法框架的文献 | 背景 / 对话 / 脚注级引用的文献 |
| Methodology 部分 | 必保留 workflow + key design + 图示 | 一句话三点：数据 / 方法 / 关键设计 |
| Quotable Lines | 保留 | 可省略 |
| Thesis Use | 详细写章节归属 + citation caution | 用一行 "我怎么用它" 代替 |
| Personal Notes | 详细 + 评分矩阵 | 一行简评 |

## 5★/4★ 模板的硬规则（来自 evil-thesis 阅读子模块）

如果一篇论文同时满足：

- 是 5★ / 4★ 高相关
- 偏技术 / 方法 / 模型 / pipeline
- 你以后会把它当方法支撑反复调用

那么必须保留：

- 整体流程（不只是笼统写 method）
- 关键设计（说明为什么这个方法成立）
- 原文重要图表位置
- Quotable Lines（实际原文，不是 paraphrase）
- Thesis Use

不要为了"显得学术"把这类笔记重写成更难懂的摘要卡。

## 怎么挂到 Obsidian Templater

### 方法 A · 直接放进 Vault

1. 把这三个模板复制到你的 Obsidian Vault 的 `99_Templates/`（或你常用的模板目录）
2. 在新建 reading note 时用 Obsidian 自带的 Insert template 命令插入对应模板
3. 替换 `{{title}}` 占位符

### 方法 B · 用 Templater 插件

1. 安装 [Templater](https://github.com/SilentVoid13/Templater) 插件
2. 在 Templater 设置里把这个模板目录指为 Template folder
3. 模板里可以加 Templater 语法：
   - `<% tp.file.title %>` 替换 `{{title}}`
   - `<% tp.date.now() %>` 自动填日期
   - `<% tp.system.prompt("Authors") %>` 弹窗问作者

### 方法 C · 让 LLM 用

把模板内容贴到 `04_单篇reading_note_5星4星3星_prompt.md` 的 prompt 里，让 LLM 按模板结构生成。LLM 不需要装 Obsidian Templater 也能照着写。

## 命名约定

| 笔记类型 | 文件名格式 | 示例 |
|---|---|---|
| Source Note | bibliographic 文件名（不强制前缀） | `Smith_2024_Some_Paper.md` |
| Reading Note | 同上 | `Smith_2024_Some_Paper.md` |
| Argument Block | `AB_Topic_Name.md` | `AB_TV_Advertising_As_Cultural_Record.md` |
| Concept Note | `CONCEPT_Term_Name.md` | `CONCEPT_Distant_Viewing.md` |
| Method Note | `METHOD_Term_Name.md` | `METHOD_Abductive_Case_Selection.md` |
| Project Map | `MAP_Project_Name.md` | `MAP_PhD_Methodology_Chapter.md` |

注意 Source Note 和 Reading Note **共用同一个文件名**——它们的区别在 `note_type` frontmatter 字段。Obsidian wikilink 会同时指向同一个文件名的两个 note 类型，所以你要么让 reading note 覆盖 source note（推荐），要么用 `01_Sources/` 和 `02_Reading_Notes/` 两个目录隔离同名文件。

## YAML 字段约定

所有模板的 frontmatter 留空字段都可以由 LLM 自动填充（除了 `project`，因为这是用户决定的）。

`relevance` 字段强烈建议用星标符号 `5★ / 4★ / 3★ / 2★ / 1★` 而不是数字——避免和 priority / rating 等字段混淆。

`citation_verified: false` 默认值为 false，等你用 Crossref / Semantic Scholar 核对过后改为 true。

## 与示范笔记对照

`Obsidian_Vault_起步包/02_Reading_Notes/` 下有两篇真实示范笔记：

- `Example_5star_Smits_Wevers_2023.md` — 用 `TPL_Reading_Note_5星4星.md` 模板的实际效果
- `Example_3star_Morgan_2007.md` — 用 `TPL_Reading_Note_3星.md` 模板的实际效果

如果你不确定模板填到什么程度算"做到位"，对照示范笔记的密度。
