---
note_type: reading_note
paper_id: Smits_Wevers2023
authors: Thomas Smits, Melvin Wevers
year: 2023
title: "A multimodal turn in Digital Humanities. Using contrastive machine learning models to explore, enrich, and analyze digital visual historical collections"
journal_or_publisher: Digital Scholarship in the Humanities
volume_issue_pages: "00, pp. 1-14"
doi: 10.1093/llc/fqad008
url: https://doi.org/10.1093/llc/fqad008
local_pdf: ""
field: Digital Humanities, Computer Vision, Visual History, Computational Humanities
relevance: 4★
status: read
sections_read: [全文]
project: "[YOUR_PROJECT_NAME]"
argument_blocks: []
concepts: [semantic_gap, multimodal_models, historical_bias, zero_shot_classification]
methods: [CLIP_zero_shot, prompt_engineering]
citation_verified: true
created: 2026-05-16
updated: 2026-05-16
tags: [CLIP, multimodal, DH, visual-archives, historical-bias, semantic-gap, zero-shot, example-5star]
---

> [!note] 这是一份示范 reading note
> 展示 5★/4★ 模板填到位时的密度和深度。
> 笔记内具体的 thesis use（"Gap 1/Gap 2/Gap 3"、特定章节、研究对象）使用占位符或一般化描述。
> fork 后请替换为你自己的章节结构、gap 分类、方法论术语。
> 论文本身（Smits & Wevers 2023）和引用的 wikilinks 是真实的公开 DH 文献。

# A Multimodal Turn in Digital Humanities

## 核心信息 / Core Information

- **Paper ID**: Smits_Wevers2023
- **Authors**: Thomas Smits (University of Antwerp), Melvin Wevers (University of Amsterdam)
- **Date**: 2023
- **Journal**: *Digital Scholarship in the Humanities*, 00, pp. 1–14
- **DOI**: 10.1093/llc/fqad008
- **Field**: Digital Humanities / Visual History / Computational Humanities
- **Access**: Open Access (CC BY-NC 4.0)
- **Local PDF**: `[YOUR_LOCAL_PATH]`

---

## 为什么与我的研究相关 / Why It Matters

> [!important]
> 这是目前文献池中**最直接将多模态模型应用于历史视觉档案**的方法论论文，也是少数明确讨论 "semantic gap"（语义鸿沟）在 DH 语境中含义的文章之一。对我的论文有三层价值：
>
> **第一层（多模态背景）**：本文证明多模态模型（CLIP 是 VLM 的前身）可以大规模处理历史视觉馆藏，但也揭示了其局限性——semantic gap 并未因为多模态而消失，只是被部分缩小。这是我建立"VLM 并未根本解决 annotation/interpretation gap"时可以援引的实证先例。
>
> **第二层（历史偏见）**：Section 5 对多模态模型"历史偏见"的讨论——训练数据来自 2008–2021 年的互联网，因此将当代西方视角投射到历史材料上——是我在方法论透明度讨论中必须引用的内容。对任何使用 VLM 处理历史档案的研究都同等成立。
>
> **第三层（方法论先例）**：三个案例研究提供了可以与我方法对话的具体实验设计，尤其是"prompt engineering"和"zero-shot 分类"对历史材料的实际效果数据。

---

## Abstract

### 英文原文

Until recently, most research in the Digital Humanities (DH) was monomodal, meaning that the object of analysis was either textual or visual. Seeking to integrate multimodality theory into the DH, this article demonstrates that recently developed multimodal deep learning models, such as Contrastive Language Image Pre-training (CLIP), offer new possibilities to explore and analyze image–text combinations at scale. These models, which are trained on image and text pairs, can be applied to a wide range of text-to-image, image-to-image, and image-to-text prediction tasks. Moreover, multimodal models show high accuracy in zero-shot classification, i.e. predicting unseen categories across heterogeneous datasets. Based on three exploratory case studies, we argue that this zero-shot capability opens up the way for a multimodal turn in DH research. However, we also need to be aware of the specific (historical) bias of multimodal deep learning that stems from biases in the training data used to train these models.

### 中文翻译

**中文：** 直到近期，数字人文（DH）研究大多是单模态的——研究对象要么是文本，要么是图像。本文将多模态理论整合进 DH，演示了以 CLIP 为代表的多模态深度学习模型如何提供大规模探索和分析图像-文本组合的新可能。这些模型在图像-文本对上训练，可用于文本到图像、图像到图像和图像到文本等多种预测任务。多模态模型在零样本分类上表现出高准确率——即能够在未曾见过的异质数据集上预测新类别。基于三个探索性案例，作者认为零样本能力为 DH 研究的"多模态转向"开辟了道路。然而，研究者也需警惕多模态深度学习中内嵌的（历史性）偏见——这些偏见源自训练数据本身。

### 核心要点 / Key Points

- DH 长期以文本分析为主；多模态模型为"多模态转向"提供技术基础
- CLIP 的核心能力：**zero-shot 分类**——无需标注数据即可跨异质数据集预测新类别
- CLIP 部分缩小了"semantic gap"，但并未消除；VLM 输出仍需研究者的人文解释
- 三类任务：text-to-image、image-to-text、image-to-image
- **"Slippery" 概念**：抽象的、多模态的文化概念（family、love、piety）传统 CV 无法识别，CLIP 可部分处理
- **历史偏见**是核心方法论挑战：CLIP 训练数据来自 2008–2021 年互联网，将当代视角投射到历史材料
- 关键方法论问题："我们试图识别的视觉概念，在我们的资料所属的历史时期是否以同样的形式存在？"

---

## Methodology

### 整体流程

```text
输入：历史视觉数字馆藏（magic lantern slides / 荷兰儿童书插图 / 历史新闻照片）

Step 1: 提取 CLIP embeddings
  ├─ 图像编码器 → 图像向量
  └─ 文本编码器 → 文本（prompt）向量

Step 2: 三类检索任务
  ├─ Text-to-image：用文本 prompt 检索相似图像（cosine similarity）
  ├─ Image-to-text：用图像匹配预定义文本标签（zero-shot 分类）
  └─ Image-to-image：用图像检索视觉相似图像

Step 3: 验证与标注辅助
  └─ CLIP 生成候选标注 → crowd workers 核查 → 迁移学习改进模型

输出：元数据层（metadata labels）/ 可检索的视觉语义空间
```

### 关键设计

**CLIP 架构（Contrastive Language-Image Pre-training）**
- 双编码器：图像编码器 + 文本编码器
- 对比学习目标：最大化匹配图像-文本对的余弦相似度
- 训练数据：4亿张图像-文本对（LAION-400M）
- Zero-shot 能力：无需任务特定训练，可直接应用于未见过的类别

**Prompt Engineering 的重要性**（Case Study 1）
- "exterior/interior" → 整体准确率 0.807（最优）
- "outside/inside" → 0.769（中等）
- "outdoors/indoor" → 0.730（较低）
- 启示：prompt 措辞直接影响分类性能；多义词和同音词会误导模型

**与传统 CV 模型的比较**

| 模型 | 整体准确率 |
|---|---|
| ResNet-18（专项训练） | 0.898 |
| CLIP（zero-shot） | 0.807 |
| 文本模型（word unigrams） | 0.798 |

CLIP zero-shot 略低于专项训练模型，但**不需要任何标注数据**——这是根本性优势。

### 图示

- **Figure 1** — CLIP 对比预训练的视觉表示（图像-文本双编码器结构）
- **Figure 2** — Zero-shot 预测流程：prompt → text encoder → cosine similarity → 排名
- **Figure 3–4** — Top-4 检索结果（具象 + 抽象情感概念对比）
- **Figure 6** — 三种 prompt 的 Precision@N 曲线
- **Figure 7–9** — 荷兰儿童书中"a family"的正确识别 / 误识别 / 性别角色模式

---

## 核心发现 / Key Findings

- **Zero-shot 能力使多模态 DH 研究成为可能**：不再需要昂贵的人工标注，可以直接在历史馆藏上运行（Section 3）
- **"Slippery" 概念的可检索性**：CLIP 能检索"family"、"love"等抽象概念——但检索结果本身揭示了模型的文化假设（Section 4.2）
- **CLIP 的"错误"具有阐释价值**：模型错误地将照顾婴儿的女孩认定为"家庭"，反映了训练数据中关于性别角色的"disciplinary discourse" — 模型的偏见本身成为研究对象（p. 9）
- **历史偏见是根本性挑战**：CLIP 训练于 2008–2021 年互联网（年轻男性、英语母语、西方国家用户主导），投射到历史材料上可能产生系统性误判（Section 5）
- **语义鸿沟并未消失**：即使多模态模型大幅缩小了文本与图像的语义距离，"images need text to anchor them" 的问题依然存在 — 研究者仍需提供人文解释（p. 12）

---

## 对我研究的启示 / Implications

### 1. semantic gap 的持续性 — 多模态时代依然成立

本文证明：即使使用 CLIP 这类多模态模型，**语义鸿沟并未消失，只是被部分缩小**。这正是我论证 [YOUR_GAP_1] 所需的实证铺垫：VLM（GPT-4V 等）比 CLIP 能力更强，但 annotation/interpretation 的根本区分依然成立 — 计算输出是"intermediate surrogate"，而非人文解释。

### 2. "历史偏见" — 数据透明度的操作化

本文 Section 5 提供了"历史偏见"最具体的讨论：
- 训练数据时间段与研究对象时间段的不匹配
- 社会构成偏见（年轻、男性、西方、英语）
- 关键问题："该视觉概念在我们资料所属的历史时期是否以同样形式存在？"

这个框架可以直接迁移到 [YOUR_ARCHIVE_DOMAIN]：VLM 是否能识别我研究的历史时期的视觉语言？什么视觉概念可能因历史偏见而被系统性误读？

### 3. Prompt Engineering 与方法论透明度

本文对 prompt 选择的详细分析（accuracy 差异达 10%+ 取决于 prompt 措辞）提示：在设计 VLM 查询策略时，必须明确说明 prompt 选择的依据和测试过程。这是方法论透明度的要求。

### 4. CLIP 误识别的阐释价值 — "productive errors"

"模型的错误本身成为研究对象"这一观点（Section 4.2）值得在方法论章节中讨论。VLM 对档案视觉内容的"误读"可能揭示训练数据中编码的文化假设，本身可以成为批判性分析的素材。

---

## 可引用原文 / Quotable Lines

> "CV models are still unable to bridge the 'semantic gap' (Smeulders et al., 2000) between what computational methods can extract from visual data and what these data mean to a user. In other words, we need text if we want to understand what images mean."
>
> **中文：** CV 模型仍然无法弥合"语义鸿沟" — 计算方法能从视觉数据中提取的内容，与这些数据对用户来说意味着什么，两者之间依然存在鸿沟。换言之，我们需要文本才能理解图像的意义。（p. 2）

> "Multimodal models are not only biased toward the worldview of the most avid Internet users, the way in which they see the world is also tied to a specific historical period."
>
> **中文：** 多模态模型不仅偏向于最活跃的互联网用户的世界观，它们看待世界的方式还与特定的历史时期密切相关。（p. 12）

> "Did the visual concept that we are trying to identify exist (in the same form) in the time of our sources/when the training data for the multimodal model were collected?"
>
> **中文：** 我们试图识别的视觉概念，在我们的资料所属的历史时期（或多模态模型训练数据收集时）是否以同样的形式存在？（p. 12）

> "In this sense, CLIP's mistakes represent the same 'disciplinary discourse' about the family as the images that the model identified correctly."
>
> **中文：** 在这个意义上，CLIP 的错误与模型正确识别的图像一样，代表着同一种关于家庭的"规训性话语"。（p. 9）

---

## Thesis Use / 如何用于我的论文

- 更偏：**方法论先例 + 批判性反思资源**
- 最可能进入：[YOUR_CHAPTER]（semantic gap 讨论）、[YOUR_OTHER_CHAPTER]（历史偏见与数据透明度）
- 不该被拿来证明：
  - 不能用来等同 CLIP 和 VLM — 两者能力层次不同；CLIP 做相似性/分类，VLM 做完整描述生成
  - 不能用来声称多模态模型已解决 annotation/interpretation 问题 — 本文实际上是反证
- **Citation caution**：DOI 已核（10.1093/llc/fqad008），引用页码以本地 PDF 为准

---

## 与既有文献的对话 / Dialogue With Existing Literature

- [[Arnold_Tilton2024_Explainable_Search_VLM_Heritage]] — 同样讨论多模态模型在文化遗产档案中的应用；本文用 CLIP 做分类/检索，Arnold & Tilton 用 VLM 做可解释搜索；构成方法论路径的比较
- [[Noble2018_Algorithms_of_Oppression]] — 本文的"历史偏见"讨论（LAION 训练数据中的种族/性别刻板印象）与 Noble 的批判性 AI 框架直接呼应
- [[Lee2023_Collections_as_ML_Data_Checklist]] — Lee 的核查清单框架与本文的历史偏见讨论共同构成"使用 AI 分析档案前需要什么"的规范性回答

（重点已标分歧：本文用"semantic gap"而非"annotation/interpretation gap" — 两个概念框架的差异值得在文献综述中讨论）

---

## 局限性 / Limitations

- **CLIP 而非 VLM**：CLIP 不生成描述，只做相似性计算；直接引用时需明确区分 CLIP 与 GPT-4V 等 VLM
- **静态图像为主**：三个案例都是静态图像，对动态视频/广告影像的适用性未被讨论
- **历史偏见分析尚浅**：Section 5 识别了问题但解决方案有限，未提供系统性的偏见量化方法
- **非英语语境局限**：案例主要来自荷兰语历史资料；迁移到其他语言-视觉组合需要额外考量
- **Prompt 工程的脆弱性**：实验显示 prompt 措辞对结果影响极大（超 10%），这是一个稳健性问题

---

## 相关论文 / Related Papers

### 直接相关
- Smits, T. and Kestemont, M. 2021. 'Towards multimodal computational humanities. Using CLIP to analyze late-nineteenth century magic lantern slides' — 本文 Case Study 1 的前期研究
- Smits, T. and Wevers, M. 2021. 'The agency of computer vision models as optical instruments'. *Visual Communication*

### 方法论相关
- van Noord, N. 2022. 'A survey of computational methods for iconic image analysis'. *Digital Scholarship in the Humanities*
- Crawford, K. and Paglen, T. 2019. *Excavating AI* — 对 CLIP 训练数据偏见的批判性框架来源
- Birhane, A. et al. 2021. 'Multimodal datasets: misogyny, pornography, and malignant stereotypes'

---

## 我的综合评价 / Evaluation

**7.5/10** — 多模态转向的重要先行研究；历史偏见讨论是方法论亮点；但 CLIP 与 VLM 的能力差距需要在引用时注意区分

| 评分维度 | 分数 | 理由 |
|----------|------|------|
| 创新性 | 7/10 | 首批将 CLIP 系统性应用于历史视觉档案的 DH 论文；案例设计有说服力 |
| 方法质量 | 8/10 | 三个案例互补，quantitative 结果与 qualitative 解读并重 |
| 理论深度 | 6/10 | "历史偏见"概念有价值但理论化程度不深 |
| 对我的价值 | 8/10 | 提供历史档案多模态研究的直接方法论先例，历史偏见框架直接可用 |

---

## 我的笔记 / Personal Notes

%% 以下为个人补充 %%

**两个概念需要在写作中区分清楚：**
1. **Semantic gap**（Smits & Wevers / CV 文献用语）：计算提取的特征与用户理解的意义之间的鸿沟 — 技术层面问题
2. **Annotation/interpretation gap**（Arnold & Tilton / DV 框架用语）：算法标注与人文解释之间的本质区分 — 认识论层面问题

两者相关但不等同。

**值得深入的问题：**
- VLM（GPT-4V）在处理"slippery"概念时是否表现出与 CLIP 不同的失败模式？
- "训练数据时间偏见"在动态视频领域的具体表现是什么？
- 是否存在"productive errors"的系统性识别方法？

---

## Upgrade Candidate

- candidate_type: method
- confidence: medium
- reason: 本文的"prompt engineering 影响分类准确率"和"历史偏见框架"可作为方法论支撑被多次引用；但需要看是否能聚成一个跨多篇的 method block

---

## Single Reading Report

completed: [[Example_5star_Smits_Wevers_2023]]
dialogue: [[Arnold_Tilton2024_Explainable_Search_VLM_Heritage]], [[Noble2018_Algorithms_of_Oppression]], [[Lee2023_Collections_as_ML_Data_Checklist]]
unsure: none
