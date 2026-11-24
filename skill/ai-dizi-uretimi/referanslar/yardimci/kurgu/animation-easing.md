# Animation Reference: PIL + ffmpeg & Easing Functions

## Easing Functions (copy inline into every sub-agent — do not import across slots)

```python
def ease_out_cubic(t: float) -> float:
    """Single reveals — slow landing. Use for: text appear, element pop-in."""
    return 1 - (1 - t) ** 3

def ease_in_out_cubic(t: float) -> float:
    """Continuous draws — smooth through. Use for: bar fills, progressive reveals."""
    if t < 0.5:
        return 4 * t ** 3
    return 1 - (-2 * t + 2) ** 3 / 2

def ease_out_elastic(t: float, amplitude: float = 1.0, period: float = 0.3) -> float:
    """Springy reveal. Use for: emphasis, counter landing."""
    if t == 0 or t == 1:
        return t
    s = period / (2 * 3.14159) * (amplitude if amplitude >= 1 else period / (2 * 3.14159))
    return amplitude * (2 ** (-10 * t)) * ((t - s) * (2 * 3.14159) / period) + 1

def ease_in_cubic(t: float) -> float:
    """Slow start. Use for: exits, fade-outs."""
    return t ** 3

# NEVER USE: linear easing — it looks robotic and mechanical
```

## PIL Overlay Card Pattern

```python
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import subprocess
import os

# Config
WIDTH, HEIGHT = 1920, 1080
FPS = 24
DURATION_S = 6.0
TOTAL_FRAMES = int(FPS * DURATION_S)
OUTPUT_DIR = "frames"
OUTPUT_VIDEO = "render.mp4"

# Palette
BG = (10, 10, 10)
ACCENT = (255, 90, 0)       # #FF5A00
LABEL = (110, 110, 110)
WHITE = (255, 255, 255)
FONT_PATH = "/System/Library/Fonts/Menlo.ttc"   # macOS — adjust for Linux

# Load fonts
try:
    font_title = ImageFont.truetype(FONT_PATH, 56, index=1)
    font_label = ImageFont.truetype(FONT_PATH, 28, index=1)
    font_small = ImageFont.truetype(FONT_PATH, 20, index=1)
except:
    font_title = ImageFont.load_default()
    font_label = font_small = font_title

os.makedirs(OUTPUT_DIR, exist_ok=True)

def render_frame(frame_idx: int) -> Image.Image:
    t_global = frame_idx / TOTAL_FRAMES   # 0.0 → 1.0

    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    # Example: text reveal over first 0.5s
    reveal_end = 0.5
    if t_global <= reveal_end:
        t = ease_out_cubic(t_global / reveal_end)
        alpha = int(255 * t)
        y_offset = int(30 * (1 - t))
    else:
        alpha = 255
        y_offset = 0

    # Anchor text on FULL string width (prevents sliding left during reveal)
    title = "Your Title Here"
    bbox = draw.textbbox((0, 0), title, font=font_title)
    full_width = bbox[2] - bbox[0]
    x = (WIDTH - full_width) // 2
    y = HEIGHT // 2 - 60 + y_offset

    # Draw with alpha (PIL doesn't support alpha on RGB directly — use RGBA)
    img_rgba = img.convert("RGBA")
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    d.text((x, y), title, font=font_title, fill=(*ACCENT, alpha))
    img_rgba = Image.alpha_composite(img_rgba, overlay)
    img = img_rgba.convert("RGB")

    return img

# Render all frames
for i in range(TOTAL_FRAMES):
    frame = render_frame(i)
    frame.save(f"{OUTPUT_DIR}/frame_{i:05d}.png")

# Encode to MP4
subprocess.run([
    "ffmpeg", "-y",
    "-framerate", str(FPS),
    "-i", f"{OUTPUT_DIR}/frame_%05d.png",
    "-c:v", "libx264",
    "-crf", "18",
    "-pix_fmt", "yuv420p",
    "-preset", "medium",
    OUTPUT_VIDEO
], check=True)

# Verify
result = subprocess.run(
    ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
     "-of", "csv=p=0", OUTPUT_VIDEO],
    capture_output=True, text=True
)
print(f"Rendered: {OUTPUT_VIDEO} — duration: {result.stdout.strip()}s (expected {DURATION_S}s)")
```

## Typewriter Text (anchor trick)

```python
def draw_typewriter(draw, text, x_center, y, font, color, progress):
    """
    Reveals text character by character.
    CRITICAL: always center on FULL text width, not partial — prevents sliding.
    """
    full_bbox = draw.textbbox((0, 0), text, font=font)
    full_width = full_bbox[2] - full_bbox[0]
    x = x_center - full_width // 2   # anchored to full width

    chars_to_show = max(1, int(len(text) * progress))
    visible = text[:chars_to_show]
    draw.text((x, y), visible, font=font, fill=color)
```

## Animation Payoff Sync

```python
def compute_overlay_start(narration_transcript, payoff_keyword, reveal_duration_s):
    """
    Find the payoff word in the narration and back-calculate overlay start
    so the animation's landing frame coincides with the spoken payoff word.
    """
    for word in narration_transcript['words']:
        if payoff_keyword.lower() in word['word'].lower():
            payoff_time = word['start']
            return max(0, payoff_time - reveal_duration_s)
    raise ValueError(f"Payoff keyword '{payoff_keyword}' not found in transcript")
```

## Common Animation Specs

### Stat card reveal (5s total)
```
0.0s–0.0s: Frame is black (pre-roll)
0.0s–0.3s: Background rectangle fades in (ease_out_cubic)
0.3s–0.8s: Label text fades + slides up from y+20px (ease_out_cubic)
0.8s–1.8s: Number counts up from 0 to target (ease_out_cubic on counter)
1.8s–4.5s: Hold
4.5s–5.0s: Entire card fades out (ease_in_cubic)
```

### Lower-third (4s total)
```
0.0s–0.0s: Pre-roll
0.0s–0.4s: Left-side accent bar slides in from x-20px (ease_out_cubic)
0.1s–0.5s: Name text fades in (ease_out_cubic), slight offset behind bar
0.3s–0.7s: Title/role text fades in below (ease_out_cubic)
0.7s–3.3s: Hold
3.3s–4.0s: Entire card fades out + slides left 20px (ease_in_cubic)
```

### Bar chart reveal (6s total)
```
0.0s–0.5s: Axis lines draw in (ease_out_cubic)
0.5s–2.5s: Bars grow upward simultaneously (ease_out_cubic per bar, slight stagger 0.1s)
2.5s–5.5s: Hold (labels fade in at 2.5s with 0.5s duration)
5.5s–6.0s: Fade out (ease_in_cubic)
```

## Linux Font Fallbacks

```python
import os

def find_font(preferred_paths: list, size: int = 40) -> ImageFont.FreeTypeFont:
    """Find first available font from a priority list."""
    for path in preferred_paths:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()

FONT_OPTIONS = [
    "/System/Library/Fonts/Menlo.ttc",                    # macOS
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", # Linux
    "/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf",  # Linux alt
    "/Windows/Fonts/consola.ttf",                          # Windows
]
font = find_font(FONT_OPTIONS, size=48)
```
