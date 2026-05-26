---
status: prompt
type: prompt
task: discussion_evidence_pack
use_when: "已有 Results，需要建立 findings ↔ literature 映射作为 Discussion 素材"
do_not_use_when: "Results 还没定；或只是润色"
input_required:
  - "Discussion Writing Configuration"
  - "Results 草稿或 Results Evidence Pack"
  - "相关 reading notes 路径"
output: "Discussion Evidence Pack：findings × literature × stance 矩阵 + literature gaps"
stop_points:
  - "证据包输出后停下，等用户确认"
quality_gates:
  - "每条 literature reference 必须能在 reading notes 里找到出处"
  - "区分 finding / interpretation / implication / speculation"
related_prompts:
  - "03_章节结构规划_prompt"
  - "../../阅读/03_根据反馈找Gap并补文献_prompt"
---

# Discussion 证据包生成 prompt

## 复制给 LLM 的 prompt

```text
请为 Discussion 章节生成证据包。不要起草正文。任务是把我的 findings
和已有文献建立显式映射。

## 知识隔离

只用 Results 草稿里实际报告过的 findings，和我提供的 reading notes 里实际
读到过的文献。不要凭训练记忆补"这个领域大概有 X 研究"——不在 reading notes 里
的，标 [需要新读]。

## 输出

## Discussion Evidence Pack

### Findings × Literature Matrix

| Finding | Engages with（reading note key）| Stance | What it adds | Reading note evidence |
|---|---|---|---|---|

Stance 取值（最重要的一列）：
- **支持**（confirms）：我的发现与文献一致；
- **延伸**（extends）：我的发现在文献观点基础上扩展到新对象 / 新条件；
- **修正**（refines）：我的发现修正了文献中的过强或过弱表述；
- **反驳**（contradicts）：我的发现与文献结论不一致；
- **桥接**（bridges）：我的发现连接了两组以往不对话的文献；
- **揭示 gap**（reveals gap）：我的发现暴露出文献没有处理过的现象。

不允许出现"general background reference"——如果一个引用没有具体 stance，
就不该出现在 Discussion 里。

### Literature Gaps for Discussion

| Gap I want to discuss | Existing literature I have / need | What to do |
|---|---|---|

### Interpretive Options

对每个核心 finding，列出 2-3 个可能的解释 (rival interpretations)：

| Finding | Interpretation A | Interpretation B | Interpretation C | Evidence to prefer one |
|---|---|---|---|---|

如果一个 finding 只有一个可能解释，那要么是 finding 极其窄，要么是你
没认真想过 rival。多数情况下应该至少有两个。

### Implications Candidates（暂列，不展开）

- theoretical:
- methodological:
- practical:
- policy（如适用）:

### Do Not Overclaim

- 典型 over-interpretation 模式：
  - 把局部 finding 升级为 broad theoretical claim；
  - 把 association 解释为 mechanism；
  - 用一个理论解释 N 个 unrelated finding；
  - 把 "future research could explore" 包装成 "this study suggests"。

输出后停下，问我哪些 stance / interpretation 进入结构规划。

## 输入

Discussion Writing Configuration：
[粘贴]

Results 草稿 / Results Evidence Pack：
[粘贴或路径]

相关 reading notes 路径或 keys：
[填]
```
