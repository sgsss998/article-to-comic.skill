#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Strict SOP runner for 连环漫画.skill
- Step4: serial API calls with 5-6s interval
- Step5: parse url and download
- Output: ./outputs/comic/<article>/scene_N.json|png
"""
import json, os, time, subprocess, random, urllib.request
from pathlib import Path

ROOT = Path('/Volumes/T7/Super_Knowledge_Base/AI分身专用工作区/workflow.skill')
OUT = ROOT / 'outputs' / 'comic'

ARTICLES = {
    'ai-memory-library': [
        '职场漫画风格，单格漫画。主题开场：未来AI竞争在“谁更懂你”，画面是公共汽车写“通用大模型”与房车写“私有记忆库”并列。中文标题清晰。',
        '单格漫画。信息爆炸与注意力有限的冲突：屏幕上信息流暴涨，人物只剩一个聚光灯注意力槽。',
        '单格漫画。建立本地记忆库：人物把日记、工作、偏好、会议笔记放入“本地记忆仓库”。',
        '单格漫画。四地备份+云端备份：Mac mini、MacBook、移动硬盘、NVMe、GitHub云端图标组成防护网。',
        '单格漫画。多年后AGI时代，人物把多年资料一键喂给AI，AI气泡“我比任何人都懂你”。',
        '单格漫画收束。标语：AI时代最宝贵资产=你的记忆。风格温暖坚定。'
    ],
    'openclaw-local-embedding': [
        '职场漫画风格，单格。小龙虾角色抱账单，标题“token越用越贵”。',
        '单格漫画。解释embedding：文字被切块变成向量，箭头进入向量数据库，检索再回到对话上下文。',
        '单格漫画。云端API路径导致持续扣费，心跳任务频繁触发，钱包在滴血。',
        '单格漫画。本地方案：Ollama + bge-m3 + 本地endpoint，人物开开心心看成本=0。',
        '单格漫画。对比卡片：成本、速度、隐私三项，云端 vs 本地。中文表述简洁。',
        '单格漫画结论：省下embedding成本，把预算留给推理；小龙虾继续长记忆。'
    ],
    'cursor-riper5': [
        '职场漫画风格，单格。开场问题：AI过度自主，未授权先改文件，用户抓狂。',
        '单格漫画。五模式门牌：研究、创新、计划、执行、回顾，机器人站在门外等待口令。',
        '单格漫画。规则核心：未经明确指令不得切换模式，红色警示条。',
        '单格漫画。设置方式一：Cursor设置页 Rules。界面感插画。',
        '单格漫画。设置方式二：项目根目录 rule.md，写入协议模板。',
        '单格漫画结论：流程更工程化，减少擅自修改，协作更可控。'
    ],
    'khazix-dark-forest': [
        '职场漫画风格，单格。社媒被大量真假图刷屏，人物困惑“这张到底真不真？”。',
        '单格漫画。猜疑链闭环：截图被怀疑是AI，怀疑截图的截图也被怀疑。',
        '单格漫画。核心命题：造假成本趋近0，信任成本趋近无穷。数学符号强化。',
        '单格漫画。三条公理：信息爆炸、注意力恒定、辨别成本高于内容价值。',
        '单格漫画。生存策略：不再筛信息本身，转向筛信息源头，信任附着在人。',
        '单格漫画结尾：在黑暗森林里，做一个值得被信任的人。情绪沉稳。'
    ]
}


def load_key():
    if os.environ.get('JIEKOU_API_KEY'):
        return os.environ['JIEKOU_API_KEY'].strip()
    md = Path('/Volumes/T7/Super_Knowledge_Base/CLAUDE.md')
    for line in md.read_text(encoding='utf-8').splitlines():
        if 'API Key:' in line and 'sk_' in line:
            return line.split('`')[1].strip()
    raise RuntimeError('No API key')

KEY = load_key()
URL = 'https://api.jiekou.ai/v3/nano-banana-pro-light-t2i'

for slug, scenes in ARTICLES.items():
    d = OUT / slug
    d.mkdir(parents=True, exist_ok=True)
    for i, prompt in enumerate(scenes, 1):
        j = d / f'scene_{i}.json'
        p = d / f'scene_{i}.png'
        if p.exists() and j.exists():
            print(f'{slug} scene_{i} skip (exists)')
            continue
        payload = {
            'prompt': prompt + ' 16比9横向，中文文字清晰。',
            'size': '16x9',
            'quality': '2k',
            'n': 1,
            'response_format': 'url'
        }
        req = urllib.request.Request(URL, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'), headers={'Content-Type':'application/json','Authorization':f'Bearer {KEY}'}, method='POST')
        last=None
        for _ in range(4):
            try:
                with urllib.request.urlopen(req, timeout=120) as r:
                    data = json.loads(r.read().decode('utf-8'))
                last=None
                break
            except Exception as e:
                last=e
                time.sleep(4)
        if last: raise last
        j.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
        url = data['data'][0]['url']
        subprocess.run(['curl','-fsSL','--retry','3','--retry-delay','2','-o',str(p),url], check=True)
        print(f'{slug} scene_{i} done')
        # Strict SOP interval: 5-6s
        time.sleep(random.uniform(5.0,6.0))

print('strict run done')
