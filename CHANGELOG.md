# Changelog

## v0.3.1 - 2026-04-23

- `examples/SOURCES.md`：原文出处改为微信公众号**官方链接**，不再写本地知识库路径。

## v0.3.0 - 2026-04-23

- 新增 `examples/`：三篇「AI干货家老明」往期文章节选 + 真实调用图像 API 生成的漫画，**左右对比 PNG**。
- 新增 `examples/SOURCES.md` 记录原文出处索引；新增 `scripts/build_article_comic_examples.py` 供复现。
- README 增加「实战示例」区块与 raw 图外链。

## v0.1 - 2026-04-22

- 首次发布公开版 `连环漫画.skill`。
- 基于原 SOP 完成脱敏处理（移除明文 Key、私有路径、敏感识别信息）。
- README 改为 `baoxiao.skill` 风格结构（版本说明、使用方法、FAQ、文末二维码与收款码）。

## v0.2.1 - 2026-04-23

- 修复封面水印：此前使用 `PingFang.ttc` 在 Pillow 中无法加载，中文未渲染；改为 `STHeiti Medium.ttc` 叠字，并加大字号保证可见。

## v0.2 - 2026-04-22

- 封面图重新用图像 API 生成；首张叠加水印「AI干货家老明」。
- 第二张候选图仅使用泛称「API」，不出现第三方平台名。
- README 文案统一为「图像生成 API + 占位 Endpoint」，避免绑定单一品牌表述。

