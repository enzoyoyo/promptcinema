# Character Base Image Prompts / 基础角色图像提示词

## Selection Criteria / 角色参考选择标准

### YES (可用)
- Candid portraits: natural lighting, clear face, everyday clothing, high authenticity
- Sources: Pinterest search `candid portrait` / `street style` / `everyday look`

### NO (禁用)
- Studio shots, model-tier faces, heavy retouching, AI-generated images

---

## Nano Banana Pro — Base Character Prompt Template

### JSON Format (Simplified)

```json
{
  "subject": {
    "type": "person",
    "gender": "male/female",
    "age_range": "20s/30s/40s",
    "build": "athletic/average/slim",
    "ethnicity": "description",
    "expression": "natural smile/neutral/confident",
    "clothing": "casual everyday outfit description",
    "pose": "candid, natural posture"
  },
  "scene": {
    "location": "urban street/coffee shop/gym/park",
    "time_of_day": "morning/afternoon/golden hour",
    "weather": "clear/overcast/rainy"
  },
  "style_ref": "urban_gritty",
  "camera_angle": "eye level/slight low angle",
  "framing": "medium shot/close-up/full body"
}
```

### Natural Language Template

```
A candid photo of a [age] [gender], [build] build, wearing [clothing description],
[expression] expression, standing/sitting in [location] during [time of day].
[Camera angle], [framing]. Natural lighting, authentic feel.
{style.prompt_suffix}
```

### Example Prompts

#### Fitness Transformation — Before
```
A candid phone photo of a 28-year-old man, average build, wearing an oversized
grey hoodie and sweatpants, slightly tired expression, standing in a dimly lit
bathroom mirror. Eye level, medium shot. Harsh fluorescent overhead light,
authentic feel, slight motion blur from phone camera.
```

#### Fitness Transformation — After
```
A candid photo of a 28-year-old man, muscular fit build, wearing a fitted black
t-shirt and well-fitted jeans, confident relaxed expression, standing on a sunny
urban street. Slight low angle, medium shot. Natural golden hour sidelight,
authentic candid feel.
```

---

## Tips / 关键技巧

1. **3x3 Storyboard Grid**: Generate 9 consistent shots at once for ample visual context
2. **Subtle Keywords**: Use "muscular," "fit," "confident posture" — avoid extreme exaggeration
3. **Save Every Winner**: Archive every successful prompt immediately to your Prompt Swipe File
4. **Iterative Reference**: Use previous output as reference for next generation to maintain character consistency
5. **Avoid**: "8K, masterpiece, ultra-detailed, hyper-realistic" — these scream AI
