#!/bin/bash
# =============================================================================
# B-Roll Download Script Template / B-Roll 下载脚本模板
# =============================================================================
#
# Prerequisites / 前置依赖:
#   pip install yt-dlp
#   brew install aria2 ffmpeg   (macOS)
#   apt install aria2 ffmpeg    (Linux)
#
# Usage / 使用方法:
#   1. Fill in URLs and timestamps below
#   2. Run: chmod +x download_broll.sh && ./download_broll.sh
#
# =============================================================================

set -euo pipefail

# Configuration
OUTPUT_DIR="broll_$(date +%Y%m%d)"
QUALITY="best[height<=1080]"

mkdir -p "$OUTPUT_DIR"

echo "=== B-Roll Download Script ==="
echo "Output directory: $OUTPUT_DIR"
echo ""

# -----------------------------------------------------------------------------
# Helper function: Download a clip with timestamp
# Args: output_name, url, start_time, end_time
# -----------------------------------------------------------------------------
download_clip() {
    local name="$1"
    local url="$2"
    local start="$3"
    local end="$4"

    echo "Downloading: $name ($start → $end)"
    yt-dlp \
        -o "$OUTPUT_DIR/${name}.%(ext)s" \
        -f "$QUALITY" \
        --download-sections "*${start}-${end}" \
        --force-keyframes-at-cuts \
        --no-playlist \
        "$url" || echo "  FAILED: $name — check URL"
    echo ""
}

# -----------------------------------------------------------------------------
# CLIPS — Fill in your URLs and timestamps
# Format: download_clip "filename" "url" "start" "end"
# -----------------------------------------------------------------------------

# Example entries (replace with your actual sources):
# download_clip "segment_01_gym" "https://youtube.com/watch?v=XXXXX" "0:15" "0:20"
# download_clip "segment_02_street" "https://youtube.com/watch?v=YYYYY" "1:02" "1:07"
# download_clip "segment_03_cooking" "https://youtube.com/watch?v=ZZZZZ" "0:45" "0:50"

echo "=== Instructions ==="
echo "1. Search YouTube/X/Google for B-roll matching your script"
echo "2. Prefer: raw footage, small channels, foreign news, archival"
echo "3. Add download_clip entries above with URLs and timestamps"
echo "4. Re-run this script to download all clips"
echo ""
echo "=== Post-Download Processing ==="
echo "# Trim to exact frame: ffmpeg -ss START -to END -i input.mp4 -c copy output.mp4"
echo "# Convert to 9:16:   ffmpeg -i input.mp4 -vf 'scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2' output.mp4"
echo ""
echo "Done. Files saved to: $OUTPUT_DIR/"
