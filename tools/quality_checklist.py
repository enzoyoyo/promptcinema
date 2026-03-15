#!/usr/bin/env python3
"""
Pre-Publish Quality Checklist / 发布前质量检查工具

Interactive checklist that must be passed before publishing any video.

Usage:
    python quality_checklist.py
    python quality_checklist.py --json  # Output as JSON
"""

import argparse
import json
import sys
from datetime import datetime


CHECKLIST = [
    {
        "id": "hook",
        "category": "Attention",
        "question": "Does the first frame grab attention within 0.5 seconds?",
        "question_zh": "第一帧能在 0.5 秒内抓住注意力？",
        "critical": True,
    },
    {
        "id": "face_consistency",
        "category": "Quality",
        "question": "Is the character's face consistent across all frames?",
        "question_zh": "角色面部在所有帧中保持一致？",
        "critical": True,
    },
    {
        "id": "lighting_match",
        "category": "Quality",
        "question": "Do lighting angles match between before/after?",
        "question_zh": "光线角度在 before/after 之间匹配？",
        "critical": True,
    },
    {
        "id": "believable",
        "category": "Authenticity",
        "question": "Is the transformation believable (not exaggerated)?",
        "question_zh": "转变可信而非夸张？",
        "critical": True,
    },
    {
        "id": "no_uncanny",
        "category": "Authenticity",
        "question": "No AI uncanny valley (overly perfect skin / stiff pose / melting fingers)?",
        "question_zh": "没有 AI 恐怖谷破绽（过完美皮肤/僵硬姿势/融化手指）？",
        "critical": True,
    },
    {
        "id": "duration",
        "category": "Format",
        "question": "Duration is 15 seconds or less?",
        "question_zh": "时长控制在 15 秒以内？",
        "critical": False,
    },
    {
        "id": "trending_audio",
        "category": "Growth",
        "question": "Is the audio a current trending sound?",
        "question_zh": "音效是当前趋势音？",
        "critical": False,
    },
    {
        "id": "text_overlay",
        "category": "Growth",
        "question": "Text overlay is short and punchy?",
        "question_zh": "文字叠加简短有力？",
        "critical": False,
    },
    {
        "id": "natural_ending",
        "category": "Format",
        "question": "Natural ending — no logo, no CTA?",
        "question_zh": "结尾自然，没有 Logo/CTA？",
        "critical": False,
    },
    {
        "id": "export_spec",
        "category": "Format",
        "question": "Exported as 9:16 / 1080x1920?",
        "question_zh": "导出为 9:16 / 1080×1920？",
        "critical": False,
    },
]

# Style filter — automatic fail conditions
STYLE_FILTERS = {
    "forbidden": [
        "Over-produced feel / 过度制作感",
        "Generic AI aesthetic / 通用 AI 质感",
        "Slow pacing / 节奏拖沓",
        "Tutorial energy / 教程能量",
        "Obviously fake / 明显造假",
    ],
    "required": [
        "Authenticity / 真实感",
        "Shareability / 可分享感",
        "Real transformation feel / 真实转变感",
        "Scroll-stopping power / 滑动停止力",
    ],
}


def run_interactive_checklist() -> dict:
    """Run the checklist interactively in terminal."""
    results = {
        "timestamp": datetime.now().isoformat(),
        "items": [],
        "passed": True,
        "critical_failures": [],
    }

    print("\n" + "=" * 60)
    print("  VIDEO QUALITY CHECKLIST / 视频质量检查")
    print("=" * 60)
    print("\nAnswer y/n for each item:\n")

    for item in CHECKLIST:
        critical_tag = " [CRITICAL]" if item["critical"] else ""
        prompt = f"  [{item['category']}]{critical_tag} {item['question']}\n  {item['question_zh']}\n  (y/n): "

        while True:
            answer = input(prompt).strip().lower()
            if answer in ("y", "n", "yes", "no"):
                break
            print("  Please enter y or n.")

        passed = answer in ("y", "yes")
        results["items"].append({
            "id": item["id"],
            "passed": passed,
            "critical": item["critical"],
        })

        if not passed and item["critical"]:
            results["passed"] = False
            results["critical_failures"].append(item["id"])
            print("  !! CRITICAL FAILURE — must fix before publishing\n")
        elif not passed:
            print("  -> Warning: consider fixing\n")
        else:
            print("  OK\n")

    # Summary
    total = len(results["items"])
    passed_count = sum(1 for i in results["items"] if i["passed"])

    print("\n" + "=" * 60)
    print(f"  RESULT: {passed_count}/{total} passed")

    if results["passed"]:
        print("  STATUS: READY TO PUBLISH")
    else:
        print(f"  STATUS: NOT READY — {len(results['critical_failures'])} critical failures")
        print(f"  Fix: {', '.join(results['critical_failures'])}")

    print("=" * 60 + "\n")

    return results


def export_json_template() -> None:
    """Export checklist as JSON template for automation."""
    template = {
        "checklist": CHECKLIST,
        "style_filters": STYLE_FILTERS,
        "export_settings": {
            "resolution": "1080x1920",
            "aspect_ratio": "9:16",
            "frame_rate": "30fps",
            "codec": "H.264",
            "max_duration_seconds": 15,
        },
    }
    print(json.dumps(template, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(
        description="Pre-publish video quality checklist"
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output checklist template as JSON (for automation)"
    )
    args = parser.parse_args()

    if args.json:
        export_json_template()
    else:
        results = run_interactive_checklist()
        sys.exit(0 if results["passed"] else 1)


if __name__ == "__main__":
    main()
