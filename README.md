# AI Viral Video Lab

> **AI 病毒式短视频全流程制作系统** | One-stop AI Viral Short Video Production System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

[中文](#中文说明) | [English](#english)

---

## 中文说明

### 核心哲学

**可信度 > 完美度。** 所有产出必须感觉像"一个真实的人无意间火了的内容"，而不是"AI 生成的广告片"。

- **停留率（Stop Rate）** 和 **完播率（Watch-through）** 是北极星指标
- 消灭 AI 恐怖谷效应：避免过度完美的皮肤、僵硬的姿势、不一致的光线
- 一条命中 → 翻拍 5-10 个变体，骑着热度走
- 每条视频 5-10 分钟完成，批量生产 10 条控制在 60-90 分钟

### 项目结构

```
ai-viral-video-lab/
├── styles/              # 导演视觉风格 JSON 配置
│   ├── urban_gritty.json
│   ├── clean_minimal.json
│   ├── neon_noir.json
│   ├── golden_hour.json
│   └── documentary_raw.json
├── prompts/             # 提示词模板库
│   ├── character_base.md        # 基础角色生成
│   ├── transformation.md        # 转变图 (before/after)
│   ├── scene_variants.md        # 场景变体
│   ├── storyboard_3x3.md       # 3×3 故事板网格
│   └── video_generation.md      # 视频生成提示词
├── workflows/           # 工作流配置
│   ├── image_to_video.md        # 图生视频完整流程
│   ├── batch_production.md      # 批量生产系统
│   └── weekly_schedule.md       # 每周节奏模板
├── tools/               # 辅助工具脚本
│   ├── broll_search.py          # B-roll 素材搜寻
│   ├── quality_checklist.py     # 发布前质量检查
│   └── export_settings.json     # 导出设置
├── resources/           # S-Tier 视觉灵感资源库
│   └── inspiration_sources.md   # 灵感网站分类索引
├── scripts/             # 自动化脚本
│   └── download_broll.sh        # B-roll 下载脚本模板
├── examples/            # 示例与教程
│   └── quickstart.md            # 快速开始指南
├── CONTRIBUTING.md      # 贡献指南
├── LICENSE              # MIT 许可证
└── README.md            # 本文件
```

### 七大阶段

| 阶段 | 内容 | 关键工具 |
|------|------|----------|
| 1. 灵感采集 | S-Tier 视觉资源库 + 趋势追踪 | Pinterest, Savee.it, Cosmos.so |
| 2. 角色与图像 | AI 图像生成 + 导演风格控制 | Nano Banana Pro, 风格 JSON |
| 3. AI 视频 | 图生视频 + 运动参考 | Kling 3.0, Veo 3.1, Sora 2 |
| 4. B-Roll | 自动化素材搜寻与组织 | yt-dlp, ffmpeg |
| 5. 剪辑导出 | CapCut 剪辑 + 导出规范 | CapCut, Premiere |
| 6. 发布增长 | 多平台分发 + 数据迭代 | TikTok, Reels, Shorts |
| 7. 批量生产 | 流水线模式 3h → 21 条内容 | 全工具链 |

### 快速开始

```bash
# 克隆项目
git clone https://github.com/enzoyoyo/promptcinema.git
cd promptcinema

# 安装 Python 依赖（用于辅助工具）
pip install -r requirements.txt

# 查看快速开始指南
cat examples/quickstart.md
```

### 工具矩阵（2026）

| 工具 | 最佳场景 | 特点 |
|------|----------|------|
| **Kling 3.0** | 动作序列、产品展示、角色动画 | 物理引擎强、边缘/Logo 保留好 |
| **Veo 3.1** | 对话镜头、电影级画面、品牌片 | 原生音频同步、流畅运镜 |
| **Sora 2** | 超写实场景、概念片 | 全动态 + 情感 + 同步音效 |
| **Hailuo 2.3** | 快速草稿、A/B 测试 | 速度快、适合迭代 |
| **Runway** | VFX、背景替换、运动捕捉 | 综合创意工具包 |
| **Seedance** | 快速生成、30-60 秒出片 | 集成在 NanoBanana 平台 |

---

## English

### Core Philosophy

**Believability > Perfection.** Every output must feel like "a real person who accidentally went viral," not "an AI-generated ad."

- **Stop Rate** and **Watch-through Rate** are the North Star metrics
- Eliminate AI uncanny valley: avoid overly perfect skin, stiff postures, inconsistent lighting
- One hit → remake 5-10 variants, ride the wave
- 5-10 minutes per video, batch produce 10 videos in 60-90 minutes

### Seven Phases

1. **Inspiration Collection** — S-Tier visual resource library + trend tracking
2. **Character & Image Generation** — AI image generation + director style control (Nano Banana Pro)
3. **AI Video Generation** — Image-to-video + motion reference (Kling / Veo / Sora)
4. **B-Roll Sourcing** — Automated footage search and organization
5. **Editing & Export** — CapCut editing + export specs (9:16, 1080x1920)
6. **Publishing & Growth** — Multi-platform distribution + data-driven iteration
7. **Batch Production** — Pipeline mode: 3 hours → 21 pieces of content

### Quick Start

```bash
git clone https://github.com/enzoyoyo/promptcinema.git
cd promptcinema
pip install -r requirements.txt
cat examples/quickstart.md
```

### Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
