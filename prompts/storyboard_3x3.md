# 3x3 Storyboard Grid / 3x3 故事板网格

## Overview / 概述

Generate 9 consistent shots in a single grid to establish visual context for your video. This is the most efficient way to plan a short video's visual narrative.

一次生成 9 张一致风格的镜头，为视频提供充足的视觉上下文。这是规划短视频视觉叙事最高效的方式。

---

## Grid Layout

```
┌─────────────┬─────────────┬─────────────┐
│  1. HOOK    │  2. SETUP   │  3. BEFORE  │
│  (0-1s)     │  (1-3s)     │  (3-5s)     │
├─────────────┼─────────────┼─────────────┤
│  4. TENSION │  5. TURNING │  6. CHANGE  │
│  (5-7s)     │  POINT(7-9s)│  (9-11s)    │
├─────────────┼─────────────┼─────────────┤
│  7. REVEAL  │  8. PAYOFF  │  9. FINAL   │
│  (11-12s)   │  (12-14s)   │  (14-15s)   │
└─────────────┴─────────────┴─────────────┘
```

---

## Prompt Template

### Nano Banana Pro Grid Prompt

```
Generate a 3x3 storyboard grid for a [transformation type] short video featuring
[character description]. Each cell should be a distinct shot:

Row 1 (Setup):
- Cell 1: Close-up hook shot — [dramatic detail that stops the scroll]
- Cell 2: Wide establishing shot — [character in before environment]
- Cell 3: Medium shot — [clear before state]

Row 2 (Transformation):
- Cell 4: Detail shot — [the catalyst/effort montage]
- Cell 5: Medium shot — [turning point moment]
- Cell 6: Medium shot — [visible change beginning]

Row 3 (Payoff):
- Cell 7: Dramatic reveal shot — [full after state]
- Cell 8: Close-up — [confident expression/detail]
- Cell 9: Wide shot — [character in aspirational environment]

Maintain consistent character appearance across all 9 cells.
{style.prompt_suffix}
```

---

## Example: Fitness Transformation Grid

```
3x3 storyboard grid, consistent character throughout:

1. Extreme close-up of a hand gripping a bathroom scale — harsh overhead light
2. Wide shot of a 26-year-old man in oversized clothes, dimly lit apartment
3. Medium shot, same man looking in bathroom mirror, uncertain expression
4. Close-up of running shoes hitting pavement — early morning, cool tones
5. Medium shot, same man at gym, mid-rep, determined face, slight sweat
6. Medium shot, trying on a new fitted shirt, slight surprise at reflection
7. Full body reveal — same man, muscular build, confident stance, golden hour
8. Close-up face — genuine smile, sharp jawline, warm natural light
9. Wide shot — walking through sunny urban street, confident stride

Same person in all frames. Shot on RED V-RAPTOR, bleach bypass grade,
16mm Kodak grain, raw documentary aesthetic.
```

---

## Usage Tips / 使用技巧

1. **Cell 1 is everything**: This becomes your first frame — it must stop the scroll
2. **Maintain arc**: The grid tells a story — setup → conflict → resolution
3. **Vary shot sizes**: Mix close-ups, medium, and wide shots for visual rhythm
4. **Time mapping**: Each cell ≈ 1.5-2 seconds of final video
5. **Export cells individually**: Use each as a keyframe for video generation
