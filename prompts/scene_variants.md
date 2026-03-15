# Scene Variant Prompts / 场景变体提示词

## Purpose / 目的

Generate the same character in multiple environments to create a rich visual narrative for video content.

将同一角色放置在多个环境中，为视频内容创造丰富的视觉叙事。

---

## Scene Variant Template

### JSON Format

```json
{
  "character_ref": "base character image reference",
  "scenes": [
    {
      "location": "gym",
      "action": "mid-workout, lifting weights",
      "time": "early morning",
      "framing": "medium shot, slight low angle"
    },
    {
      "location": "kitchen",
      "action": "preparing meal prep containers",
      "time": "morning light",
      "framing": "over-the-shoulder, close on hands"
    },
    {
      "location": "urban street",
      "action": "walking confidently toward camera",
      "time": "golden hour",
      "framing": "full body, centered"
    }
  ],
  "style_ref": "urban_gritty",
  "maintain_consistency": ["face", "build", "hair", "skin tone"]
}
```

### Natural Language Template

```
The same [character description] from the reference image, now [action] in [location]
during [time of day]. [Framing description]. Maintaining exact same facial features,
build, and hair. {style.prompt_suffix}
```

---

## Common Scene Progressions

### Fitness Journey (5 scenes)
1. Gym — lifting weights, focused expression
2. Kitchen — meal prep, healthy food visible
3. Mirror selfie — progress check, slight smile
4. Outdoor run — park or street, morning light
5. Social setting — confident posture, well-dressed

### Style Glow-Up (5 scenes)
1. Closet — looking at old clothes, uncertain expression
2. Shopping — trying on new outfit, mirror reflection
3. Barber/Salon — mid-haircut, anticipation
4. Street — walking in new outfit, confident stride
5. Social event — getting compliments, genuine smile

### Lifestyle Change (5 scenes)
1. Messy room — overwhelmed, cluttered desk
2. Planning — clean desk, journal open, morning coffee
3. Working out — simple home workout, determined
4. Working — focused, organized workspace
5. Evening — relaxed, content expression, tidy home

---

## Consistency Tips / 一致性技巧

- Always include the base character reference image in your generation
- Keep clothing colors consistent within a scene sequence
- Match lighting temperature across scenes in the same "time period"
- Use the same style JSON across all scenes in a sequence
- Generate all scenes in one session to maintain model memory
