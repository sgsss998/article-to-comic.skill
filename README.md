# 连环漫画.skill · 文章一键漫画化工作流

> Skill 文件名：`连环漫画.skill`（复制到 Agent / OpenClaw 的 skills 目录即可）  
> 将长文章转成连环漫画风格图片，自动完成分镜、Prompt、批量生成与交付。

![连环漫画.skill 封面](./assets/chikawa-cover-v1.png)

---

## 🆕 版本更新（请先看）

- 当前建议版本：`v0.5.1`
- 完整迭代记录：`CHANGELOG.md`

**v0.5.1 更新重点：**

- 示例分镜链接已切换为严格 SOP 产物目录 `outputs/comic/`（串行调用、5-6 秒间隔、scene_*.json+png 成对输出）。

**v0.5.0 更新重点：**

- 四篇文章全部升级为**深度分镜**：每篇 6 张连续漫画，共 24 张。
- README 与公众号文章同步从“单图示例”升级为“多图完整概括”。

**v0.4.0 更新重点：**

- 新增第 4 个真实示例：卡兹克《因为GPT-image-2，整个互联网都变成了巨大的黑暗森林。》
- 示例图为「原文摘录 vs 漫画」左右对比图，并加入 README 与公众号排版 HTML。

**v0.3.1 更新重点：**

- `SOURCES.md` 改为只收录**微信官方 mp 链接**，便于读者直接打开原文。

**v0.3.0 更新重点：**

- 新增 **3 组真实示例**：选自「AI干货家老明」往期公众号/博客稿节选，经同一套流程调用图像 API 生成单格漫画，并与原文摘录 **左右合成对比图**（见 `examples/`）。
- 提供生成脚本 `scripts/build_article_comic_examples.py`，可本地复现或改文案/Prompt。

**v0.2.1 更新重点：**

- 修复首张封面水印：改用系统中文字体渲染「AI干货家老明」，避免 Pillow 无法加载 `PingFang` 导致字不显示。

**v0.2 更新重点：**

- 封面首张叠加水印「AI干货家老明」；候选图二仅保留「API」等泛称画面。
- README 与 skill 中 Endpoint/Key 统一为占位符，便于接入任意兼容接口。
- 固化 6 步标准流程：阅读拆解 -> 分镜规划 -> Prompt 编写 -> API 调用 -> 下载 -> 交付。

---

## 🎯 我能做什么

当你给我一篇文章时，我会自动完成：

- 提炼核心观点并规划分镜
- 为每一帧生成可执行 Prompt
- 调用你配置的**图像生成 API**批量出图
- 下载整理为统一目录结构
- 按顺序发送并附图注说明

---

## 📸 实战示例：四篇文章深度分镜（每篇6张）

以下示例按“原文节选 -> 分镜拆解 -> 漫画生成”流程执行，不再只用1张图粗略概括。每篇均提供 6 张连续分镜，尽量完整覆盖论点。

> 原文官方链接见 [`examples/SOURCES.md`](./examples/SOURCES.md)。

### 例一：《为什么我们需要建立 AI 记忆库》
![例一-对比图](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/examples/example-01-ai-memory-library-compare.png)
![例一-分镜1](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/ai-memory-library/scene_1.png)
![例一-分镜2](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/ai-memory-library/scene_2.png)
![例一-分镜3](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/ai-memory-library/scene_3.png)
![例一-分镜4](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/ai-memory-library/scene_4.png)
![例一-分镜5](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/ai-memory-library/scene_5.png)
![例一-分镜6](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/ai-memory-library/scene_6.png)

### 例二：《Openclaw 小龙虾：embedding 放本地》
![例二-对比图](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/examples/example-02-openclaw-embedding-compare.png)
![例二-分镜1](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/openclaw-local-embedding/scene_1.png)
![例二-分镜2](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/openclaw-local-embedding/scene_2.png)
![例二-分镜3](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/openclaw-local-embedding/scene_3.png)
![例二-分镜4](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/openclaw-local-embedding/scene_4.png)
![例二-分镜5](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/openclaw-local-embedding/scene_5.png)
![例二-分镜6](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/openclaw-local-embedding/scene_6.png)

### 例三：《Cursor 全局 Rule — RIPER-5 五模式》
![例三-对比图](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/examples/example-03-cursor-riper5-compare.png)
![例三-分镜1](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/cursor-riper5/scene_1.png)
![例三-分镜2](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/cursor-riper5/scene_2.png)
![例三-分镜3](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/cursor-riper5/scene_3.png)
![例三-分镜4](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/cursor-riper5/scene_4.png)
![例三-分镜5](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/cursor-riper5/scene_5.png)
![例三-分镜6](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/cursor-riper5/scene_6.png)

### 例四：《因为GPT-image-2，整个互联网都变成了巨大的黑暗森林》
![例四-对比图](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/examples/example-04-khazix-dark-forest-compare.png)
![例四-分镜1](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/khazix-dark-forest/scene_1.png)
![例四-分镜2](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/khazix-dark-forest/scene_2.png)
![例四-分镜3](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/khazix-dark-forest/scene_3.png)
![例四-分镜4](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/khazix-dark-forest/scene_4.png)
![例四-分镜5](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/khazix-dark-forest/scene_5.png)
![例四-分镜6](https://raw.githubusercontent.com/sgsss998/article-to-comic.skill/master/outputs/comic/khazix-dark-forest/scene_6.png)

---

## 📋 API 配置（公开版占位）

- **工具**：任意兼容 `nano-banana-pro-light-t2i` 的**图像生成 API**（把 Endpoint 换成你自己的服务商地址即可）
- **接口**：`POST {YOUR_IMAGE_ENDPOINT}/v3/nano-banana-pro-light-t2i`
- **鉴权**：`Authorization: Bearer YOUR_IMAGE_API_KEY`
- **推荐尺寸**：`16x9`
- **输出目录**：`./outputs/comic/`

> 注意：公开版不内置真实 Key；请使用你自己的 API 密钥。

---

## 🚀 使用方法

### 第一步：输入文章

发给我文章原文（或长段落内容），并说明目标平台（公众号/小红书/微博等）。

### 第二步：我自动处理

我会按以下顺序执行：

1. 阅读理解，提取核心框架
2. 规划分镜（每帧只讲一件事）
3. 编写逐帧 Prompt（统一漫画风格）
4. 串行调用 API（避免并发失败）
5. 下载图片并按序整理
6. 按序输出并附简短图注

### 第三步：检查并发布

- 检查图片逻辑是否完整
- 若某帧不满意，指定“重画第 N 张”
- 通过后直接用于图文发布

---

## 📁 输出文件结构

```
outputs/
└── comic/
    ├── scene_1.png
    ├── scene_2.png
    ├── scene_3.png
    ├── scene_1.json
    ├── scene_2.json
    └── ...
```

---

## ⚡ 标准调用示例

```bash
curl -s -X POST "${YOUR_IMAGE_ENDPOINT}/v3/nano-banana-pro-light-t2i" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_IMAGE_API_KEY" \
  -d '{"prompt":"职场漫画风格，单格漫画，简洁有力","size":"16x9","quality":"2k","n":1,"response_format":"url"}' \
  -o ./outputs/comic/scene_1.json
```

---

## 🧩 Prompt 规则

- 风格固定：`职场漫画风格 / comic style`
- 单帧单信息：每图只表达一个观点
- 构图简洁：避免复杂场景叠加
- 文字嵌入：在 prompt 中写明关键展示文本
- 情绪明确：喜剧、反讽、温情等要写清楚

---

## 📌 常见问题

**Q: 文章太长怎么办？**  
A: 先提炼 5-8 个关键观点；超长内容拆为上下集。

**Q: 图看不懂怎么办？**  
A: 把“画面文字+角色动作+情绪”写进 prompt。

**Q: API 调用失败怎么办？**  
A: 检查 `size` 必须是 `16x9`，并确认 Key 与额度状态。

**Q: 风格不统一怎么办？**  
A: 全部帧统一使用同一风格前缀与镜头语言。

---

## 🔧 管理员配置（可选）

请在 `连环漫画.skill` 中替换以下占位符：

- `YOUR_IMAGE_API_KEY` / `YOUR_IMAGE_ENDPOINT`
- `./outputs/comic/`
- 你的默认风格模板（如职场漫画/黑白速写/美式漫画）

---

## 技术说明

- 基于 OpenClaw Agent Skill 工作流
- 支持多轮迭代重画
- 支持串行批量生成
- 支持微信/Telegram/Discord/Slack 等平台输出

---

## 联系作者

微信号：`soplaoming`

| 微信二维码 | 收款码 |
|---|---|
| ![微信二维码](https://raw.githubusercontent.com/sgsss998/baoxiao.skill/master/wechat-qrcode.jpg) | ![收款码](https://raw.githubusercontent.com/sgsss998/baoxiao.skill/master/wechat-pay-qrcode.jpg) |

