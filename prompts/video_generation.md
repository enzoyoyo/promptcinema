# Video Generation Prompts / 视频生成提示词

## Platform Selection Guide / 平台选择指南

| Need | Best Tool | Why |
|------|-----------|-----|
| Action/movement | Kling 3.0 | Strong physics engine |
| Dialogue/cinematic | Veo 3.1 | Native audio sync |
| Hyper-realistic | Sora 2 | Best realism |
| Quick draft/test | Hailuo 2.3 | Fastest turnaround |
| VFX/compositing | Runway | Creative toolkit |
| Quick 30-60s | Seedance | NanoBanana integrated |

---

## Image-to-Video Workflow

```
Nano Banana Pro (First Frame + Last Frame)
         ↓
    Choose Platform
   ┌─────┼─────┐
  Kling  Veo  Sora
   └─────┼─────┘
         ↓
  Upload Image + Motion Reference
         ↓
  Generate Multiple Variants → Pick Best
         ↓
     CapCut Final Edit
```

---

## Kling 3.0 Prompt Template

```json
{
  "platform": "kling_3.0",
  "input": {
    "start_frame": "path/to/before_image.png",
    "end_frame": "path/to/after_image.png",
    "motion_reference": "path/to/motion_ref.mp4"
  },
  "prompt": "Smooth transformation from [before state] to [after state].
    Camera: [static/slow dolly/pan].
    The subject [motion description].
    Duration: 5 seconds.
    Maintain facial consistency throughout.",
  "negative_prompt": "morphing artifacts, face distortion, melting,
    unnatural movement, floating objects, extra limbs",
  "settings": {
    "duration": "5s",
    "aspect_ratio": "9:16",
    "quality": "high",
    "motion_intensity": "medium"
  }
}
```

### Example — Fitness Transformation
```
Smooth cinematic transformation. A man in an oversized hoodie slowly straightens
his posture, his build gradually becomes more muscular and defined. His clothes
morph to a fitted t-shirt. Expression shifts from uncertain to confident.
Camera: static, eye level, medium shot. Soft natural lighting transition from
cool to warm. 5 seconds. Maintain exact same face throughout.
```

---

## Veo 3.1 Prompt Template

```json
{
  "platform": "veo_3.1",
  "input": {
    "reference_image": "path/to/character_ref.png",
    "style_ref": "golden_hour"
  },
  "prompt": "[Character description] in [scene], [action].
    Camera movement: [description].
    Audio: [ambient sound description].
    Mood: [emotional tone].",
  "settings": {
    "duration": "5-8s",
    "aspect_ratio": "9:16",
    "audio": "auto_generate",
    "quality": "cinematic"
  }
}
```

### Example — Lifestyle Scene
```
A confident 28-year-old man walks down a sun-drenched urban street,
fitted casual outfit, slight smile, headphones around neck. Camera: slow
tracking shot at eye level. Ambient city sounds, warm afternoon.
Golden hour backlight creating lens flare. Natural, effortless movement.
```

---

## Motion Reference Guidelines / 运动参考指南

### Source
- Pinterest video search
- Keep 20+ motion references in your library

### Selection Criteria
- **Duration**: 3-5 seconds maximum
- **Movement**: Slow, simple, clean
- **Background**: Clean, uncluttered
- **Action types**:
  - Slow head turn
  - Natural body shift
  - Walking toward camera
  - Subtle micro-expressions
  - Standing up from seated

### DO NOT use motion references with:
- Fast/complex movement
- Multiple people
- Busy backgrounds
- Camera shake
- Text overlays

---

## Common Negative Prompts / 通用负面提示词

Always include to avoid AI artifacts:
```
morphing artifacts, face distortion, melting features, unnatural skin texture,
extra fingers, floating objects, inconsistent lighting between frames,
uncanny valley, robotic movement, jittery motion, background warping
```
