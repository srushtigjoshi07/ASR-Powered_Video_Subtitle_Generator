from moviepy.video.io.VideoFileClip import VideoFileClip
import cv2
import numpy as np
import re

# ─────────────────────────────────────────
# Parse SRT file manually
# ─────────────────────────────────────────
def parse_srt(srt_file):
    with open(srt_file, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = re.compile(
        r'\d+\s+'
        r'(\d{2}):(\d{2}):(\d{2}),(\d{3})\s+-->\s+'
        r'(\d{2}):(\d{2}):(\d{2}),(\d{3})\s+'
        r'(.*?)(?=\n\n|\Z)', re.DOTALL
    )

    subtitles = []
    for match in pattern.finditer(content):
        h1, m1, s1, ms1 = int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))
        h2, m2, s2, ms2 = int(match.group(5)), int(match.group(6)), int(match.group(7)), int(match.group(8))
        text = match.group(9).strip().replace("\n", " ")

        start = h1 * 3600 + m1 * 60 + s1 + ms1 / 1000
        end   = h2 * 3600 + m2 * 60 + s2 + ms2 / 1000
        subtitles.append((start, end, text))

    return subtitles

# ─────────────────────────────────────────
# Get subtitle text for a given timestamp
# ─────────────────────────────────────────
def get_subtitle_at(subtitles, t):
    for start, end, text in subtitles:
        if start <= t <= end:
            return text
    return None

# ─────────────────────────────────────────
# Burn subtitles directly onto each frame
# ─────────────────────────────────────────
def burn_subtitles(srt_file, input_video="video.mp4", output_video="output_with_subs.mp4"):
    subtitles = parse_srt(srt_file)
    video = VideoFileClip(input_video)

    W, H       = int(video.w), int(video.h)
    font       = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 1.2
    thickness  = 2
    padding    = 10

    def process_frame(frame, t):
        frame = frame.copy()
        text  = get_subtitle_at(subtitles, t)

        if text:
            # Split long lines
            words     = text.split()
            lines     = []
            line      = ""
            max_chars = 50
            for word in words:
                if len(line) + len(word) + 1 <= max_chars:
                    line += (" " if line else "") + word
                else:
                    lines.append(line)
                    line = word
            if line:
                lines.append(line)

            # Draw each line from bottom up
            for i, l in enumerate(reversed(lines)):
                (tw, th), baseline = cv2.getTextSize(l, font, font_scale, thickness)

                x = (W - tw) // 2
                y = H - padding - baseline - i * (th + 20) - 40  # ✅ +20 line spacing

                # Black background box
                cv2.rectangle(
                    frame,
                    (x - padding, y - th - padding),
                    (x + tw + padding, y + baseline + padding),
                    (0, 0, 0),
                    -1
                )

                # White text on black box
                cv2.putText(frame, l, (x, y), font, font_scale,
                            (255, 255, 255), thickness, cv2.LINE_AA)

        return frame

    # Apply frame processor
    final = video.fl(lambda gf, t: process_frame(gf(t), t))
    final = final.set_audio(video.audio)

    final.write_videofile(
        output_video,
        codec="libx264",
        audio_codec="aac",
        fps=video.fps
    )

    print("✅ Done! Saved to", output_video)

# ─────────────────────────────────────────
# Run
# ─────────────────────────────────────────
burn_subtitles(
    srt_file="subtitles.srt",
    input_video="video.mp4",
    output_video="output_with_subs.mp4"
)