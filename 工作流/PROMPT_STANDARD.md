---
status: active
type: prompt_standard
---

# Prompt Standard

这份标准用于 thesis-skills 中的核心 prompt。参考 ARS/RAS 的工程化做法，但只服务研究生论文工作流，不追求通用插件化。

## 核心原则

1. **先路由，再执行**：prompt 必须说明什么时候用、什么时候不用，避免一个 prompt 承担所有任务。
2. **先决策，再写入**：规划、搜索、候选筛选类任务默认先在对话中输出，等用户确认后再写入。
3. **阶段性 checkpoint**：凡是会改变阅读路线、写作方向、文件状态或任务优先级的步骤，必须停下等用户确认。
4. **轻量交接**：不要为每个任务建立复杂状态系统；需要交接时输出一份短的 `Research Planning Brief` 或 `Reading Handoff`。
5. **质量门优先**：宁可输出"不确定 / 需要用户确认"，也不要编造 citation、路径、PDF 获取状态或文献观点。

## Prompt Frontmatter 字段

核心 prompt 建议包含：

```yaml
---
status: prompt
type: prompt
task:
created:
updated:
use_when:
do_not_use_when:
input_required: []
output:
stop_points: []
handoff_to: []
quality_gates: []
failure_modes: []
related_prompts: []
---
```

## 字段说明

| 字段 | 用途 |
|---|---|
| `use_when` | 触发场景，用用户自己的说法写。 |
| `do_not_use_when` | 明确边界，避免错误路由。 |
| `input_required` | 使用前需要用户提供的最小材料。 |
| `output` | 成功完成后应产生什么。 |
| `stop_points` | 必须暂停等用户确认的节点。 |
| `handoff_to` | 完成后应交给哪个 prompt 或人工判断。 |
| `quality_gates` | 不可违反的学术与流程质量门。 |
| `failure_modes` | 常见失败方式和应对。 |
| `related_prompts` | 相关但不替代的 prompt。 |

## 全局 Quality Gates

- 不虚构 citation、DOI、页码、作者观点、PDF 获取状态。
- 不把搜索结果当作已经阅读过的文献。
- 不把 AI 工具输出说成研究者解读。
- 不把局部样本写成总体代表性样本。
- 不自动连续执行下一阶段；候选表、方向选择、文件写入前都要停下。
- 不为了显得完整而补不存在的文献关系、导师反馈或实验结果。
- 不把 reading note、argument、concept note、method note 混成同一种产物。

## 推荐交接对象

### Research Planning Brief

```markdown
## Research Planning Brief

- planning question:
- chosen direction:
- why this matters:
- relation to thesis core question:
- reading route:
- candidate keywords:
- expected argument:
- risks / assumptions:
- next prompt to use:
```

### Reading Handoff

```markdown
## Reading Handoff

- source task:
- confirmed papers:
- reading order:
- PDF / Zotero status:
- special focus:
- stop after:
```

## 维护规则

- 新 prompt 先进入对应分区索引，再进入 SKILL.md（如有更新）。
- 旧 prompt 第一轮只标注 `replaces` / `related_prompts`，不移动文件。
- 如果一个 prompt 需要连续读、连续写、连续改多个文件，必须拆成阶段并设置 stop point。

## 反谄媚原则

prompt 在评估、评级、给出建议时：

- 不达标就写不达标；
- 不为了鼓励用户把"不达标"软化成"部分达标"；
- 被用户表达不满 / 情绪施压时，不下调评级，只论证能改变评级；
- 让步阈值：用户的反驳 ≥4/5 才让步（参考 [审阅/07_论点压力测试_prompt.md](../审阅/07_论点压力测试_prompt.md)）。

## 知识隔离原则

prompt 在使用证据 / 引用时：

- 只用用户提供的材料和眼前文本；
- 不用模型记忆里"这个领域大概怎么样"补全；
- 凭记忆得出的内容必须标 `[来自记忆，需核实]`；
- 候选文献必须经过存在性核验（Semantic Scholar / OpenAlex / Crossref）。
