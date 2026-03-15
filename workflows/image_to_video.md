# Image-to-Video Workflow / 图生视频完整流程

## Overview

Complete pipeline from character reference to final video output.

---

## Step-by-Step Pipeline

### Step 1: Character Reference
- Source candid reference photos from Pinterest
- Criteria: natural light, clear face, everyday clothing
- Save to `references/characters/` folder

### Step 2: Base Image Generation (Nano Banana Pro)
```
Input: Character reference photo
Output: Base character image matching your style JSON
Tool: Nano Banana Pro (Google Flow / Gemini)

Tips:
- Use the simplified JSON prompt format
- Load your chosen style config (e.g., urban_gritty.json)
- Generate 3-4 variants, pick the best
```

### Step 3: Scene Variants
```
Input: Best base character image
Output: 5-9 scene variants (see prompts/scene_variants.md)
Tool: Nano Banana Pro

Tips:
- Use previous output as reference for next generation
- Keep same session for consistency
- Generate 3x3 storyboard grid (see prompts/storyboard_3x3.md)
```

### Step 4: Transformation Images
```
Input: Base character image + style config
Output: Before image + After image
Tool: Nano Banana Pro

Tips:
- Follow prompts/transformation.md templates
- Lighting shift is critical: harsh → flattering
- Same person, different state
```

### Step 5: First Frame + Last Frame
```
Select from your generated images:
- First frame: The "before" state OR the hook shot
- Last frame: The "after" state OR the reveal shot

These become the anchors for video generation.
```

### Step 6: Motion Reference
```
Source: Pinterest video search
Selection: Simple, slow movement, 3-5 seconds, clean background
Save to: references/motion/

Good actions:
- Slow head turn
- Walking toward camera
- Standing up confidently
- Subtle smile
```

### Step 7: Video Generation
```
Platform Selection:
- Action/movement → Kling 3.0
- Cinematic/dialogue → Veo 3.1
- Hyper-realistic → Sora 2
- Quick draft → Hailuo 2.3

Input: First frame + Last frame + Motion reference
Settings: 9:16, 5 seconds, high quality

Generate 3-5 variants → select best
```

### Step 8: CapCut Edit
```
Import: Best video variant
Add:
  - Trending audio (TikTok Creative Center)
  - Text overlay (short, punchy, human)
  - Quick cuts on beat
Duration: 10-15 seconds
Aspect: 9:16, 1080x1920

Export: H.264, 30fps, 1080x1920
```

---

## Time Budget

| Step | Time |
|------|------|
| Reference selection | 2 min |
| Base image generation | 3 min |
| Scene variants | 5 min |
| Transformation images | 3 min |
| Video generation | 5 min (+ wait time) |
| CapCut edit | 5 min |
| **Total** | **~23 min per video** |

For batch production, use pipeline mode (see workflows/batch_production.md).
