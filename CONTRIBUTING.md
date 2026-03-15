# Contributing to AI Viral Video Lab / 贡献指南

Thank you for your interest in contributing! This project thrives on community input.

感谢你对本项目的关注！社区贡献让这个项目越来越好。

---

## How to Contribute / 如何贡献

### 1. Add New Director Styles / 添加新导演风格

Create a new JSON file in `styles/` following the existing format:

```json
{
  "style_name": "your_style_name",
  "description": "English description",
  "description_zh": "中文描述",
  "camera": "Camera body model",
  "lens": "Lens model and focal length",
  "color_grade": "Color grading technique",
  "lighting": "Lighting approach",
  "grain": "Film stock or digital noise profile",
  "mood": "comma, separated, mood, keywords",
  "best_for": ["content type 1", "content type 2"],
  "prompt_suffix": "Complete prompt suffix string combining all parameters"
}
```

### 2. Add Prompt Templates / 添加提示词模板

Add new `.md` files to `prompts/` for:
- New transformation types
- New content categories
- Platform-specific optimizations
- New AI model prompt formats

### 3. Improve Tools / 改进工具

Enhance the Python tools in `tools/`:
- Better search query generation
- New automation scripts
- Integration with AI APIs
- Analytics/tracking tools

### 4. Share Workflow Tips / 分享工作流技巧

Add to `workflows/` or `examples/`:
- Platform-specific strategies
- Niche-specific guides
- Optimization tips with data

---

## Guidelines / 指南

1. **Bilingual**: Include both English and Chinese where possible
2. **Practical**: Every addition should be directly usable, not theoretical
3. **Tested**: Share prompt templates that you've actually used successfully
4. **No secrets**: Don't include API keys, personal data, or paid content
5. **Keep it real**: Our core philosophy is authenticity over perfection

---

## Pull Request Process / PR 流程

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make your changes
4. Test any Python tools: `python tools/your_tool.py --help`
5. Submit a PR with a clear description

---

## Code of Conduct / 行为准则

- Be respectful and constructive
- Focus on helping creators make better content
- No spam, self-promotion, or low-effort contributions
- Credit original sources when sharing inspiration resources

---

## Ideas We'd Love / 我们期待的贡献

- New visual style presets for specific niches (food, travel, tech, beauty)
- Automation scripts for n8n / Make.com workflows
- Templates for emerging AI video platforms
- Analytics dashboard templates
- Localized content strategies for different regions
- Integration guides for specific AI tools
