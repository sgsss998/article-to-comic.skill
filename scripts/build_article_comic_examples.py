#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 3 article→comic examples with before/after comparison PNGs for README / 公众号."""
from __future__ import annotations

import json
import os
import subprocess
import textwrap
import time
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "examples"
OUT.mkdir(parents=True, exist_ok=True)


def load_api_key() -> str:
    k = os.environ.get("JIEKOU_API_KEY", "").strip()
    if k:
        return k
    claude = Path("/Volumes/T7/Super_Knowledge_Base/CLAUDE.md")
    if claude.exists():
        for line in claude.read_text(encoding="utf-8").splitlines():
            if "API Key:" in line and "sk_" in line:
                return line.split("`")[1].strip()
    raise SystemExit("Set JIEKOU_API_KEY or add key path in script")


def call_t2i(prompt: str, out_json: Path) -> str:
    api_key = load_api_key()
    url = "https://api.jiekou.ai/v3/nano-banana-pro-light-t2i"
    payload = {
        "prompt": prompt,
        "size": "16x9",
        "quality": "2k",
        "n": 1,
        "response_format": "url",
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        data = json.loads(r.read().decode("utf-8"))
    img_url = data["data"][0]["url"]
    out_json.parent.mkdir(parents=True, exist_ok=True)
    out_json.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return img_url


def download(url: str, path: Path) -> None:
    """Prefer curl: Python urlretrieve 对部分 CDN 会触发 SSL EOF。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        ["curl", "-fsSL", "--retry", "3", "--retry-delay", "2", "-o", str(path), url],
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        raise RuntimeError(f"curl download failed: {r.stderr or r.stdout}")


def draw_text_panel(
    size: tuple[int, int],
    title: str,
    excerpt: str,
    source_line: str,
) -> Image.Image:
    w, h = size
    img = Image.new("RGB", (w, h), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    try:
        font_title = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 32, index=0)
        font_body = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 22, index=0)
        font_small = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 16, index=0)
    except OSError:
        font_title = font_body = font_small = ImageFont.load_default()

    margin = 24
    y = margin
    draw.rectangle((0, 0, w, 6), fill=(59, 130, 246))
    draw.text((margin, y), "原文摘录", font=font_small, fill=(100, 116, 139))
    y += 28
    for line in textwrap.wrap(title, width=14):
        draw.text((margin, y), line, font=font_title, fill=(17, 24, 39))
        y += 40
    y += 8
    for para in excerpt.split("\n"):
        for line in textwrap.wrap(para, width=18):
            draw.text((margin, y), line, font=font_body, fill=(31, 41, 55))
            y += 30
            if y > h - 100:
                break
        if y > h - 100:
            break
    y = h - margin - 24
    for line in textwrap.wrap(source_line, width=20):
        draw.text((margin, y), line, font=font_small, fill=(148, 163, 184))
        y -= 20
    return img


def composite_compare(
    comic_path: Path,
    title: str,
    excerpt: str,
    source_line: str,
    out_path: Path,
    left_w: int = 520,
) -> None:
    comic = Image.open(comic_path).convert("RGB")
    H = 1080
    left = draw_text_panel((left_w, H), title, excerpt, source_line)
    # fit comic to right panel height
    cw, ch = comic.size
    target_h = H - 40
    new_w = int(cw * target_h / ch)
    comic_r = comic.resize((new_w, target_h), Image.Resampling.LANCZOS)
    W = left_w + new_w + 48
    canvas = Image.new("RGB", (W, H), (248, 250, 252))
    canvas.paste(left, (24, 0))
    # label strip
    d = ImageDraw.Draw(canvas)
    try:
        f = ImageFont.truetype("/System/Library/Fonts/STHeiti Medium.ttc", 20, index=0)
    except OSError:
        f = ImageFont.load_default()
    d.text((left_w + 32, 12), "连环漫画.skill 生成效果", font=f, fill=(71, 85, 105))
    canvas.paste(comic_r, (left_w + 24, 36))
    canvas.save(out_path, quality=92)
    print("wrote", out_path, "size", canvas.size)


def main() -> None:
    specs = [
        {
            "slug": "example-01-ai-memory-library",
            "title": "为什么我们需要建立 AI 记忆库",
            "excerpt": "未来的 AI 竞争，不在于模型参数更大，而在于谁更了解你。\n通用大模型像公共汽车谁都能上；挂载私有记忆库的 Agent，才是专属房车。\n记忆应是本地、多备份、可持续更新的数字资产。",
            "source": "往期：公众号《为什么我们需要建立 AI 记忆库》2026-03-09",
            "prompt": (
                "职场漫画风格，单格漫画，明亮简洁。画面左右分镜对比：左侧公共汽车写着'通用大模型'，"
                "右侧可爱房车写着'私有记忆库'，中间箭头。上方标题条用小字写'谁更懂你'。"
                "所有文字清晰中文。16比9横向构图。"
            ),
        },
        {
            "slug": "example-02-openclaw-embedding",
            "title": "OpenClaw 小龙虾：embedding 放本地",
            "excerpt": "三级记忆靠 embedding 把文字变成向量。默认走云端 API，心跳一频繁 token 就烧。\n换成本地 Ollama 跑 bge-m3：成本接近 0，向量检索仍在，隐私不离开本机。",
            "source": "往期：公众号《把 embedding 放在本地》2026-03-10",
            "prompt": (
                "职场漫画风格，单格漫画。橙色小龙虾角色：左边抱超长账单流汗，气泡写'云端 embedding 烧钱'；"
                "右边同一小龙虾抱芯片箱开心，气泡写'本地 bge-m3 零元'。中文清晰。16比9横向。"
            ),
        },
        {
            "slug": "example-03-cursor-riper5",
            "title": "Cursor 全局 Rule：RIPER-5 五模式",
            "excerpt": "Cursor 自主性太强会未获指令就改文件。用 RIPER-5：研究、创新、计划、执行、回顾——只有明确口令才允许切换模式，改动更可控。",
            "source": "往期：公众号《严格操作协议》2026-03-16",
            "prompt": (
                "职场漫画风格，单格漫画。五个门牌竖排或横排写：研究、创新、计划、执行、回顾；"
                "小机器人在门外举手等待，旁白大字'没口令不切换'。中文清晰。16比9横向。"
            ),
        },
    ]

    for i, spec in enumerate(specs, 1):
        slug = spec["slug"]
        jpath = OUT / f"{slug}-api.json"
        print(f"[{i}/3] calling API …", slug)
        u = call_t2i(spec["prompt"], jpath)
        comic_path = OUT / f"{slug}-comic.png"
        download(u, comic_path)
        time.sleep(2)
        composite_compare(
            comic_path,
            spec["title"],
            spec["excerpt"],
            spec["source"],
            OUT / f"{slug}-compare.png",
        )
        print("done", slug)


if __name__ == "__main__":
    main()
