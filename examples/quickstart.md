# Quick Start Guide / 快速开始指南

Create your first AI viral short video in 30 minutes.

用 30 分钟制作你的第一条 AI 病毒短视频。

---

## Step 1: Choose a Style (2 min)

Browse the `styles/` directory and pick a visual style:

```bash
ls styles/
# urban_gritty.json    — Raw street documentary
# clean_minimal.json   — Bright, aspirational
# neon_noir.json       — Moody cyberpunk
# golden_hour.json     — Warm golden glow
# documentary_raw.json — Authentic handheld
```

Read your chosen style:
```bash
cat styles/urban_gritty.json
```

The `prompt_suffix` field is what you'll append to your image generation prompts.

---

## Step 2: Find a Character Reference (3 min)

Go to **Pinterest** and search:
- `candid portrait street style`
- `everyday look natural light`
- `authentic portrait`

**Pick a photo that:**
- Has natural lighting
- Shows a clear face
- Features everyday clothing
- Feels real, not posed

**Avoid:**
- Studio shots
- Model-tier perfection
- Heavy retouching

Save the reference image.

---

## Step 3: Generate Base Character (5 min)

Open **Nano Banana Pro** (via Google Flow) and use this prompt template:

```
A candid photo of a [age]-year-old [gender], [build] build, wearing
[everyday clothing], [natural expression], standing in [everyday location].
Eye level, medium shot. [paste prompt_suffix from your style JSON]
```

**Example:**
```
A candid photo of a 27-year-old man, average build, wearing a grey
crewneck sweatshirt and dark jeans, neutral relaxed expression,
standing on an overcast city sidewalk. Eye level, medium shot.
Shot on RED V-RAPTOR with Zeiss Super Speed MKII 35mm, bleach bypass
color grade with teal shadows, available light with practicals,
16mm Kodak 7219 500T grain, raw documentary street-level aesthetic.
```

Generate 3-4 variants. Pick the best one.

---

## Step 4: Generate Transformation (5 min)

Using the same character, generate **before** and **after** images.

See `prompts/transformation.md` for full templates.

**Quick version:**

Before:
```
A candid photo of [same character], looking tired, wearing oversized
unflattering clothes, slouched posture, in a dimly lit room. Harsh
fluorescent light, phone camera quality.
```

After:
```
A candid photo of [same character], fit confident build, wearing a
well-fitted [stylish outfit], confident relaxed expression, in a
sun-lit urban setting. [paste prompt_suffix from style JSON]
```

---

## Step 5: Generate Video (5 min)

Choose your platform:
- **Kling 3.0** — Best for action/transformation
- **Veo 3.1** — Best for cinematic quality
- **Hailuo 2.3** — Fastest for testing

Upload your **before image** as start frame and **after image** as end frame.

Add a motion reference (slow, simple movement from Pinterest video search).

Prompt:
```
Smooth transformation. Subject straightens posture, build becomes more
defined, clothes transition to fitted style. Expression shifts from
uncertain to confident. Camera static, eye level. 5 seconds.
```

Generate 3 variants. Pick the best.

---

## Step 6: Edit in CapCut (10 min)

1. Import your best video
2. Add a **trending sound** (check TikTok Creative Center)
3. Add **text overlay**: short, punchy, human
   - Example: "6 months no excuses"
   - Example: "Day 1 vs Day 180"
4. Cut on the beat
5. Keep it under 15 seconds
6. End naturally — no logo, no CTA

**Export settings:**
- 1080 x 1920 (9:16)
- 30fps
- H.264

---

## Step 7: Publish

Upload to all three platforms:
- TikTok
- Instagram Reels
- YouTube Shorts

**Don't publish the same day you create.** Schedule it.

**Best times to test:** 7-10 AM and 6-10 PM in your target timezone.

---

## What's Next?

- Read `workflows/batch_production.md` to scale to 10+ videos per session
- Explore all 5 style presets in `styles/`
- Build your Prompt Swipe File from successful generations
- Check `resources/inspiration_sources.md` for visual reference sites

**Remember:** If one video hits, immediately make 5-10 variants (different character, different audio, different caption). Ride the wave.
