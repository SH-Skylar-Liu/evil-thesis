---
status: prompt
type: prompt
task: keyword_combination_generation
use_when: "你只知道一个研究问题 / 章节 gap / 导师反馈，需要让 LLM 帮你把它转换成可直接喂检索 API 的关键词组合"
do_not_use_when: "已经有明确文献清单（用 01）；只想检索已有笔记（用 paper-search 工具）；想直接生成 reading note（用 04）"
input_required:
  - "一个具体的研究问题、章节 gap、或导师反馈"
  - "你的领域 / 学科范围（影响关键词的学术语境）"
  - "可选：已知作者或核心概念"
output: "一份分组的关键词组合表 + 对应的检索路径建议（Semantic Scholar / arXiv / Crossref / Google Scholar）"
stop_points:
  - "关键词组合表生成后，必须停下让用户挑哪些组合优先检索"
  - "不要直接拿任何一组关键词去搜——挑选权在用户"
quality_gates:
  - "每组关键词必须说明它假设要找什么；不要堆砌看起来'相关'的词"
  - "区分概念组合（A AND B）和扩展组合（A AND (B OR C OR D)）"
  - "对每组指出可能的检索失败方式（太宽 / 太窄 / 术语错位）"
  - "不要凭记忆补'这个领域常用术语'；不确定的术语标 [需核实]"
failure_modes:
  - "用户只给了模糊方向时，先反问 3 个问题缩小范围，再生成关键词"
  - "如果某个领域 LLM 不熟悉，明确说'我对这个子领域术语不熟悉，以下关键词来自一般推断，建议你核对'"
related_prompts:
  - "02_关键词检索下载评分阅读_prompt"
  - "03_根据反馈找Gap并补文献_prompt"
  - "06_Semantic_Scholar_arXiv_检索协议"
---

# 关键词组合自动生成 prompt

这份 prompt 解决一个被低估的工作：**把一个模糊的研究需求拆成可以直接喂检索 API 的关键词组合**。

它不替你检索，它只是帮你把"我想找补这个 gap 的文献"翻译成 5-10 组可执行的检索 query。然后由你判断哪一组先跑。

## 为什么这一步要单独做

- LLM 直接帮你"搜文献"时容易凭记忆瞎报，看似命中实则编造（hallucinated citations）
- 把"生成关键词"和"执行检索"拆开，可以让你先审关键词是否对路，再走真实 API
- 实际经验：一个 gap 至少要 3-5 组不同切面的关键词组合才不会漏文献；让 LLM 一次性给齐比一边搜一边补省得多

## 复制给 LLM 的 prompt

```text
请帮我把下面这个研究需求拆成可直接执行的关键词组合表。

## 任务边界

你只负责：
- 把我的需求拆成 5-10 组关键词组合
- 对每组说明它假设要找什么
- 建议每组适合走哪个检索 API
- 指出每组的潜在失败方式

你不要：
- 不要直接告诉我"这个领域有这些经典文献"——那是凭记忆补全
- 不要直接调用搜索工具（如果你有 web tool 也先不要用）
- 不要把生成的关键词当成 query 直接跑出结果

## 我的需求

[在这里写你的研究问题 / 章节 gap / 导师反馈]

我的领域 / 学科范围：
[例如：digital humanities + computer vision；qualitative methods；media studies]

已知的核心概念（可选）：
[例如：distant viewing, abductive analysis；如果你已经知道一些核心术语，写在这里]

已知作者（可选）：
[例如：Arnold & Tilton, Wevers & Smits]

## 输出格式

请输出一份 Markdown 表格 + 简短说明：

| # | 关键词组合 | 假设要找什么 | 推荐检索 API | 潜在失败方式 |
|---|---|---|---|---|
| 1 | "distant viewing" AND "vision-language model" | 直接讨论 VLM 在 distant viewing 框架下的应用 | Semantic Scholar / arXiv | 可能太新，文献稀少 |
| 2 | "distant viewing" AND ("multimodal" OR "CLIP") | 退一步：找多模态/CLIP 在 distant viewing 下的应用 | Semantic Scholar | 可能命中过多 CV-only 文献 |
| ... | | | | |

然后在表格下方说明：

### 检索切面 (search facets)
- Facet A — 概念-方法对：直接搜 [核心概念] AND [核心方法]
- Facet B — 概念-应用对：搜 [核心概念] AND [应用领域]
- Facet C — 已知作者：搜 [作者名] [关键词]
- Facet D — 替代术语：用同义词 / 邻近术语扩展
- Facet E — 反向检索：搜 [对立概念] 来找批评 / 限制讨论

### 优先级建议
按"信号强度"给一个推荐次序：先跑哪组、如果不命中再跑哪组。

### 我对术语的把握度
- 高把握：[术语1, 术语2]
- 中等把握：[术语3]
- 低把握（你建议我核对）：[术语4]

如果整个领域的术语我不熟悉，明确说："我对 [子领域] 术语不熟悉，以上关键词来自一般推断，建议先用 1-2 篇核心文献验证术语后再扩大检索。"

## 停下点

生成完关键词表后停下，问我：
"你想先用哪一组检索？我可以为它生成对应 API 的 query string（Semantic Scholar / arXiv）。"
等我回复后再继续。
```

## 配套：什么时候自己拆，什么时候让 LLM 拆

| 场景 | 是否需要本 prompt |
|---|---|
| 你已经知道核心术语，只是想多几个角度 | 可以；让 LLM 帮你扩展同义词和反向检索 |
| 你对子领域完全陌生 | 强烈建议；先用本 prompt 拆，再先读 1-2 篇核心文献验证术语 |
| 你已经有 4-10 篇文献，正在写综述 | 不需要；该转去写作系统 |
| 你只有导师一句"这部分文献不够" | 强烈建议；先用 `03_根据反馈找Gap并补文献_prompt.md` 把 gap 拆出来，再用本 prompt 把 gap 转成关键词 |

## 关键词组合的五个切面 (search facets)

每次让 LLM 生成关键词组合，至少要覆盖这五类（不全都做，但要意识到自己只覆盖了哪几类）：

1. **概念-方法对**：核心概念 × 核心方法（如 `"distant viewing" AND "vision-language model"`）
2. **概念-应用对**：核心概念 × 应用领域（如 `"distant viewing" AND "television archives"`）
3. **已知作者**：从已读文献的作者名扩展（如 `"Wevers Smits" AND "computer vision"`）
4. **替代术语**：同义词 / 邻近术语 / 上位词（如 `"computational humanities" OR "digital humanities"`）
5. **反向检索**：对立概念 / 限制讨论（如 `"computer vision" "limitations" "humanities"`）

如果你只覆盖了 1-2 个切面，多半会漏掉相邻领域的关键文献。

## 与下游 prompt 的关系

- 关键词组合表 →（用户挑选）→ `06_Semantic_Scholar_arXiv_检索协议.md` 执行真实检索
- 检索结果 → `02_关键词检索下载评分阅读_prompt.md` 做候选筛选和评分
- 选定 1-2 篇 → `04_单篇reading_note_5星4星3星_prompt.md` 生成 reading note

不要试图一个 prompt 跑完整条链。每段有自己的 stop point。
