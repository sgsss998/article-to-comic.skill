# 连环漫画.skill · 文章一键漫画化工作流

> Skill 文件名：`连环漫画.skill`（复制到 Agent / OpenClaw 的 skills 目录即可）  
> 将长文章转成连环漫画风格图片，自动完成分镜、Prompt、批量生成与交付。

![连环漫画.skill 封面](./assets/chikawa-cover-v1.png)

---

## 🆕 版本更新（请先看）

- 当前建议版本：`v0.2`
- 完整迭代记录：`CHANGELOG.md`

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

