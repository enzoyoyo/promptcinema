#!/usr/bin/env python3
"""
B-Roll Search Tool / B-Roll 素材搜寻工具

Analyzes a script and generates structured B-roll search queries,
timestamps, and download scripts.

Usage:
    python broll_search.py --script script.txt --output broll_plan.md
    python broll_search.py --script script.txt --download  # generates download script
"""

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class BRollClip:
    """Represents a single B-roll clip requirement."""
    script_line: str
    search_queries: list[str]
    preferred_sources: list[str] = field(default_factory=list)
    timestamp_best: str = ""
    timestamp_alt: str = ""
    notes: str = ""


@dataclass
class BRollPlan:
    """Complete B-roll plan for a script."""
    script_title: str
    clips: list[BRollClip] = field(default_factory=list)


def parse_script(script_path: str) -> list[str]:
    """Parse script file into individual lines/sentences."""
    with open(script_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by sentences or line breaks
    lines = []
    for paragraph in content.split("\n"):
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        # Split long paragraphs into sentences
        sentences = re.split(r'(?<=[.!?])\s+', paragraph)
        lines.extend(s.strip() for s in sentences if s.strip())

    return lines


def generate_search_queries(line: str) -> list[str]:
    """Generate search queries for a script line.

    This provides baseline queries. For AI-powered query generation,
    integrate with your preferred LLM API.
    """
    queries = []

    # Base query from the line itself (cleaned up)
    clean_line = re.sub(r'[^\w\s]', '', line).strip()
    if len(clean_line.split()) <= 6:
        queries.append(f"{clean_line} stock footage")
    else:
        # Take key phrases
        words = clean_line.split()
        queries.append(f"{' '.join(words[:5])} footage")

    # Add "raw footage" variant for authenticity
    queries.append(f"{' '.join(clean_line.split()[:4])} raw footage")

    return queries


def generate_broll_plan(script_lines: list[str], title: str = "Untitled") -> BRollPlan:
    """Generate a complete B-roll plan from script lines."""
    plan = BRollPlan(script_title=title)

    for line in script_lines:
        clip = BRollClip(
            script_line=line,
            search_queries=generate_search_queries(line),
            preferred_sources=["YouTube", "X/Twitter", "Google"],
            notes="Prefer: raw/unprocessed, small channels, foreign news, archival footage"
        )
        plan.clips.append(clip)

    return plan


def export_markdown(plan: BRollPlan, output_path: str) -> None:
    """Export B-roll plan as Markdown."""
    lines = [
        f"# B-Roll Plan: {plan.script_title}\n",
        f"Generated for {len(plan.clips)} script segments.\n",
        "---\n",
    ]

    for i, clip in enumerate(plan.clips, 1):
        lines.append(f"## Segment {i}\n")
        lines.append(f"**Script:** {clip.script_line}\n")
        lines.append("**Search Queries:**\n")
        for q in clip.search_queries:
            lines.append(f"- `{q}`\n")
        lines.append(f"**Sources:** {', '.join(clip.preferred_sources)}\n")
        if clip.timestamp_best:
            lines.append(f"**Best Timestamp:** {clip.timestamp_best}\n")
        if clip.timestamp_alt:
            lines.append(f"**Alt Timestamp:** {clip.timestamp_alt}\n")
        lines.append(f"**Notes:** {clip.notes}\n")
        lines.append("---\n")

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"B-roll plan saved to: {output_path}")


def generate_download_script(plan: BRollPlan, output_dir: str = "broll") -> str:
    """Generate a shell script for downloading B-roll clips using yt-dlp."""
    script_lines = [
        "#!/bin/bash",
        "# Auto-generated B-roll download script",
        f"# Script: {plan.script_title}",
        f"# Segments: {len(plan.clips)}",
        "",
        "# Prerequisites: yt-dlp, aria2, ffmpeg",
        "# Install: pip install yt-dlp && brew install aria2 ffmpeg",
        "",
        f'OUTPUT_DIR="{output_dir}"',
        'mkdir -p "$OUTPUT_DIR"',
        "",
        "# Add URLs below after searching. Format:",
        "# yt-dlp -o '$OUTPUT_DIR/segment_XX.%(ext)s' --download-sections '*START-END' 'URL'",
        "",
    ]

    for i, clip in enumerate(plan.clips, 1):
        script_lines.append(f"# --- Segment {i}: {clip.script_line[:60]}...")
        script_lines.append(f'# Search: {clip.search_queries[0]}')
        script_lines.append(
            f"# yt-dlp -o '$OUTPUT_DIR/segment_{i:02d}.%(ext)s' "
            f"--download-sections '*0:00-0:05' 'PASTE_URL_HERE'"
        )
        script_lines.append("")

    script_lines.append('echo "Download complete. Files in $OUTPUT_DIR/"')

    return "\n".join(script_lines)


def main():
    parser = argparse.ArgumentParser(
        description="B-Roll Search Tool — Generate search plans from scripts"
    )
    parser.add_argument(
        "--script", required=True, help="Path to script text file"
    )
    parser.add_argument(
        "--output", default="broll_plan.md", help="Output markdown file path"
    )
    parser.add_argument(
        "--title", default="Untitled", help="Script/project title"
    )
    parser.add_argument(
        "--download", action="store_true",
        help="Also generate a download shell script"
    )
    parser.add_argument(
        "--download-dir", default="broll",
        help="Directory for downloaded clips"
    )

    args = parser.parse_args()

    if not os.path.exists(args.script):
        print(f"Error: Script file not found: {args.script}", file=sys.stderr)
        sys.exit(1)

    # Parse and generate plan
    script_lines = parse_script(args.script)
    plan = generate_broll_plan(script_lines, title=args.title)

    # Export markdown plan
    export_markdown(plan, args.output)

    # Optionally generate download script
    if args.download:
        dl_script = generate_download_script(plan, args.download_dir)
        dl_path = args.output.replace(".md", "_download.sh")
        with open(dl_path, "w") as f:
            f.write(dl_script)
        os.chmod(dl_path, 0o755)
        print(f"Download script saved to: {dl_path}")


if __name__ == "__main__":
    main()
