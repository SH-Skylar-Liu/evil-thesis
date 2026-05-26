---
status: prompt
type: prompt
task: academic_english_polishing
use_when: "已有内容基础的英文段落，需要把语言提升到学术水准"
do_not_use_when: "还没确定证据 / 结构 → 先用章节专用 workflow；只是审稿 → 用 审阅 区"
input_required:
  - "待润色英文段落"
  - "可选：段落所在章节 / 论文主题"
output: "Revised English + 中文解释改了什么 + citation/claim risks + 下一步"
quality_gates:
  - "不增加我没有写出的 claim"
  - "不把意思改得更强"
  - "保留我的智识立场"
  - "如果原文逻辑有问题，先指出问题，不只润色"
related_prompts:
  - "../../审阅/01_通用学术审阅_prompt"
---

# 学术英文润色 prompt

用于润色已经有内容基础的英文段落。它不是审稿 prompt，也不是重写 prompt。

## 复制给 LLM 的 prompt

```text
请把下面这段文字润色为国际研究生水平的学术英文。

要求：

- 保留我的智识立场；
- 优先清晰、准确、可论证；
- 不要过度母语化修辞；
- 不要把意思改得更强；
- 不要添加我没有写出的 claim；
- 我是英语非母语的国际研究生：不要模仿母语者的习惯表达，优先国际学术英语
  的正确性与清晰度；文章读起来应该像受过严格学术训练的国际学者写的；
- 不确定的内容用 hedging 语言（appears to argue / suggests / may address）；
- 不用夸大评价词（foundational / definitive / most cutting-edge）；

风格规则（硬性）：
- 禁用词：significant / crucial / robust / leverage / nuanced / delve /
  foundational / definitive / most cutting-edge / it is worth noting /
  importantly；以及中文"值得注意的是 / 显著 / 至关重要 / 不可忽视的是"；
- 不用破折号；
- 不用 firstly / secondly 或"首先 / 其次"；
- 每句有明确主语；
- 长短句交替；
- 主动 / 被动混用，不默认其一；
- 如果有 citation risk，请单独列出；
- 如果原文逻辑有问题，不要只润色，请先指出问题。

请输出：

1. Revised English；
2. 中文解释：你主要改了什么；
3. Citation / claim risks；
4. 如果需要，我下一步应该补什么。

原文：
[粘贴文本]
```
