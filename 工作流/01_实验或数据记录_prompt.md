---
status: prompt
type: prompt
task: experiment_or_data_log
use_when: "跑完实验 / 数据收集 / 编码会议 / 模型调参后，立刻结构化记录——不要等到 Methodology 写作时才补"
do_not_use_when: "只是日常调试，没有新发现或新参数——不值得写一份完整记录"
input_required:
  - "口述的当次操作"
  - "选择记录版本（量化实验 / 质性数据收集 / 编码会议 / 计算实验 / 快速版）"
output: "结构化记录文件 + frontmatter 元数据"
quality_gates:
  - "不发明用户没说过的内容"
  - "字段缺失时写 [未记录]，不猜测"
related_prompts:
  - "../写作/Methodology/02_证据包生成_prompt"
  - "../写作/Results/02_证据包生成_prompt"
---

# 实验或数据记录 prompt

> 这是可复现性 / dependability 的直接证据。每次跑一组数据 / 做一次访谈 / 开一次编码会议，记一次。
> 五种版本按任务类型选择。

---

## 版本 A：量化实验记录（统计 / 数据分析）

```text
请帮我把今天的量化分析整理成结构化记录。

## 输入（我口述，你整理）

我会告诉你今天做了什么。你负责把它整理成标准格式，补全缺失字段，不要发明
我没有说过的内容。如果某个字段我没有提到，写 [未记录]，不要猜测。

今天的描述：
[在这里口述，可以很零散]

## 输出格式

请把记录写入：
[路径，例如 D:/Notes/Data_Logs/Quant_Log_YYYY-MM-DD.md]

---
log_id: QUANT-YYYY-MM-DD-N
date: YYYY-MM-DD
analysis_type: [例如 OLS / logistic / multilevel / SEM / factor analysis]
status: [completed / partial / failed]
---

# 量化分析记录：[简短名称]

## 分析目标

[一句话：这次分析想回答什么问题]

## 数据

| 字段 | 值 |
|---|---|
| 数据集 / 文件 | |
| 样本量 N | |
| 时间窗 | |
| 关键变量 | |
| Missing 处理 | |

## 模型与方法

| 字段 | 值 |
|---|---|
| 软件 + 版本 | [例如 R 4.3.2 / Stata 18 / Python 3.11 + statsmodels 0.14] |
| 模型 | |
| 关键参数 / specification | |
| Pre-registered? | [是 / 否] |

## 结果摘要

| 关键发现 | 数值 | CI / p / SE | 备注 |
|---|---|---|---|

## Robustness / Sensitivity

[做了什么、结果如何]

## 已知问题

[这次确认的问题，例如 multicollinearity / endogeneity 怀疑]

## 与上次分析的对比

[如果之前有，简述本次有什么变化]

## 下一步

[下次想测什么变化]

## 对论文的影响

[影响 Methodology / Results 哪个 section]

## 未解决问题

[需要问导师 / 需要查文献 / 需要更多数据]
```

---

## 版本 B：质性数据收集记录（访谈 / 观察）

```text
请帮我把今天的质性数据收集整理成结构化记录。

今天的描述：
[口述]

## 输出格式

路径：[路径，例如 D:/Notes/Data_Logs/Qual_Log_YYYY-MM-DD.md]

---
log_id: QUAL-YYYY-MM-DD-N
date: YYYY-MM-DD
data_type: [interview / focus group / observation / document collection]
participant_id: [按你的匿名编号]
status: [completed / partial / aborted]
---

# 质性数据记录：[简短名称]

## 这次收集的目的

[对应哪个 RQ / sub-question]

## 参与者 / 场景信息

| 字段 | 值 |
|---|---|
| 参与者编号 | [匿名] |
| 简要背景 | [年龄段 / 角色 / 经验等去敏感信息] |
| 招募渠道 | |
| 知情同意状态 | [已签纸质 / 数字 / 口头] |
| 时间 | |
| 地点 / 平台 | |
| 时长 | |

## 数据形式

| 字段 | 值 |
|---|---|
| 录音 / 录像 | [是 / 否；存储位置] |
| 笔记 | [位置] |
| 转录状态 | [完成 / 部分 / 待转] |
| 匿名化状态 | |

## 主题印象（First impressions）

不是分析，是 fieldnote：印象、关键时刻、出乎意料的回应。

## Reflexivity 备忘

我自己的位置 / 偏见可能怎么影响了今天的收集？

## 已知问题

[设备问题 / 信号不好 / 中断 / 等]

## 下一步

[需要转录 / 编码 / 二次接触 / 等]

## 对论文的影响

[影响 Methodology / Results 哪个 section]
```

---

## 版本 C：编码 / 主题分析会议记录

```text
请帮我把今天的编码协商整理成结构化记录。

今天的描述：
[口述]

## 输出格式

路径：[路径]

---
log_id: CODE-YYYY-MM-DD-N
date: YYYY-MM-DD
coding_round: [round number]
participants: [谁参与了 inter-coder]
status: [completed / partial]
---

# 编码协商记录：[简短名称]

## 本轮范围

[处理了哪几个 transcript / which themes]

## Coding scheme 状态

| 字段 | 值 |
|---|---|
| Scheme 版本 | |
| 新增 codes | |
| 合并 / 拆分 codes | |
| 删除 codes | |

## Inter-coder agreement

| Metric | Value | Notes |
|---|---|---|

如果有 disagreement 没解决，列出：
| Item | Coder A | Coder B | Decision | Reason |

## 关键讨论

[3-5 个重要的讨论点，特别是 boundary cases]

## 已知问题

## 下一步

## 对论文的影响

[Methodology coding section / Results theme section]
```

---

## 版本 D：计算 / 模型实验记录（含 LLM / ML / CV）

```text
请帮我把今天的计算实验整理成结构化记录。

今天的描述：
[口述]

## 输出格式

路径：[路径]

---
log_id: COMP-YYYY-MM-DD-N
date: YYYY-MM-DD
model: [例如 GPT-4 (gpt-4-0125) / BERT-base / custom CNN]
task_type: [classification / generation / annotation / segmentation]
status: [completed / partial / failed]
---

# 计算实验记录：[简短名称]

## 实验目标

## 实验参数

| 字段 | 值 |
|---|---|
| 模型 + 版本 | |
| 输入格式 | |
| Prompt 版本（如适用） | [粘贴或引用文件] |
| 温度 / top-p / 等 | |
| 输出格式 | |
| 运行环境 | [硬件 / OS / Python 版本] |
| 数据范围 | [输入材料的特征：N、时间窗、来源] |

## 输入样本描述

[简述输入材料]

## 输出摘要

[描述模型产出了什么：标签分布 / 样例 / 总体质量印象]

典型输出示例（好的 + 差的各 1-2 个）：
- [好的]
- [有问题的]

## 已知问题 / 失败模式

[这次发现的具体问题：幻觉 / 偏差 / 边界 case 错误]

## 与上次实验的对比

## 下一步假设

[下次实验想测试什么变化]

## 对论文的影响

[影响 Methodology / Results 哪个 section]

## 未解决问题
```

---

## 版本 E：快速版（5 分钟填完）

如果没有时间写完整记录，至少保存这个：

```text
请帮我生成一条简短日志条目，追加到：
[路径，例如 D:/Notes/Data_Logs/Quick_Log.md]

格式：

## YYYY-MM-DD [类型：QUANT/QUAL/CODE/COMP] — [一句话描述]

**做了什么**：[口述]
**结果**：[口述]
**问题**：[口述，或"无"]
**下一步**：[口述]

今天做了：
[在这里口述]
```
