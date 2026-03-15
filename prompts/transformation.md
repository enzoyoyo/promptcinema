# Transformation Prompts / 转变图提示词 (Before/After)

## Core Principle / 核心原则

The transformation must feel **believable, not magical**. Think "6 months of consistent effort" not "instant AI filter."

转变必须感觉**可信而非魔法**。想象"6 个月的持续努力"而不是"瞬间 AI 滤镜"。

---

## Transformation Prompt Template

### JSON Format

```json
{
  "transformation_type": "fitness/style/confidence/lifestyle",
  "before": {
    "subject_state": "description of before state",
    "clothing": "unflattering but realistic",
    "posture": "slightly slouched, low energy",
    "lighting": "harsh/flat/unflattering",
    "environment": "mundane/messy",
    "mood": "tired/uncertain"
  },
  "after": {
    "subject_state": "description of after state",
    "clothing": "well-fitted, intentional style",
    "posture": "upright, confident, relaxed",
    "lighting": "flattering natural light",
    "environment": "aspirational but achievable",
    "mood": "confident/content/energetic"
  },
  "style_ref": "use matching style JSON",
  "consistency_ref": "link to base character image"
}
```

### Natural Language Template

#### Before Frame
```
A candid photo of [same character description], looking [before mood], wearing
[unflattering clothing], [poor posture description], in [mundane environment].
[Unflattering lighting]. Shot on phone, slightly out of focus, raw unedited feel.
```

#### After Frame
```
A candid photo of [same character description], looking [after mood], wearing
[well-styled clothing], [confident posture], in [aspirational environment].
{style.prompt_suffix}
```

---

## Transformation Categories & Examples

### 1. Fitness Glow-Up
```
BEFORE: A candid bathroom mirror selfie of a 25-year-old woman, soft build,
wearing an oversized faded college t-shirt and leggings, tired expression,
fluorescent bathroom lighting, messy counter visible. Phone flash visible in mirror.

AFTER: A candid outdoor photo of the same 25-year-old woman, toned athletic build,
wearing a fitted tank top and high-waisted jeans, bright confident smile, standing
on a sunlit patio. Natural golden hour backlight, shot on Sony A7S III aesthetic.
```

### 2. Style Transformation
```
BEFORE: A candid photo of a 30-year-old man in ill-fitting khakis and a wrinkled
polo shirt, neutral expression, standing under harsh office fluorescent lights,
bland grey wall behind. Flat unflattering light.

AFTER: A candid street photo of the same 30-year-old man in a well-tailored navy
blazer over a crisp white tee, dark fitted jeans, confident walk, urban street with
warm afternoon light. Shot on RED V-RAPTOR, bleach bypass aesthetic.
```

### 3. Confidence / Lifestyle
```
BEFORE: A candid photo of a 35-year-old woman sitting alone at a cluttered desk,
slouched posture, baggy sweater, dim room lit only by laptop screen, tired eyes.
Raw digital noise from high ISO.

AFTER: A candid photo of the same 35-year-old woman at a bright café window seat,
upright posture, elegant casual outfit, warm smile, reading a book with coffee.
Soft window light, warm tones, aspirational but natural.
```

---

## Critical Rules / 关键规则

1. **Same person**: Before and after MUST look like the same individual
2. **Lighting shift**: Before = harsh/flat, After = flattering/natural
3. **Environment shift**: Before = mundane, After = aspirational (but realistic)
4. **No extremes**: The transformation should be achievable, not fantasy
5. **Clothing matters**: Fit and style of clothes carry 50% of the transformation
6. **Posture is key**: Slouched → Upright accounts for massive perceived change
