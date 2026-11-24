# FFmpeg Recipes Reference

## Per-Segment Extract with Grade + Audio Fades

```bash
# Extract segment with grade applied and 30ms audio fades (Hard Rule 3)
ffmpeg -i "$source" \
  -ss $start -to $end \
  -vf "eq=contrast=1.05:brightness=0.02:saturation=0.85,curves=r='0/0 0.2/0.18 0.8/0.75 1/0.9':g='0/0 0.2/0.22 0.8/0.78 1/0.95':b='0/0 0.2/0.25 0.8/0.72 1/0.85'" \
  -af "afade=t=in:st=0:d=0.03,afade=t=out:st=$(echo "$dur - 0.03" | bc):d=0.03" \
  -c:v libx264 -crf 18 -preset medium \
  -c:a aac -b:a 192k \
  "clips_graded/seg_$i.mp4"
```

## Lossless Concat (Hard Rule 2)

```bash
# Create concat list
for f in clips_graded/seg_*.mp4; do echo "file '$f'"; done > concat_list.txt

# Concat without re-encoding
ffmpeg -f concat -safe 0 -i concat_list.txt -c copy "edit/concat.mp4"
```

## Overlay (PTS-Shifted) (Hard Rule 4)

```bash
# Add an animation overlay at a specific output timestamp
# overlay_start = seconds from beginning of concat output
ffmpeg -i "edit/concat.mp4" -i "animations/slot_1/render.mp4" \
  -filter_complex "[1:v]setpts=PTS-STARTPTS+$overlay_start/TB[ov]; \
                   [0:v][ov]overlay=0:0:enable='between(t,$overlay_start,$overlay_end)'[vout]" \
  -map "[vout]" -map "0:a" \
  -c:v libx264 -crf 18 -c:a copy \
  "edit/with_overlays.mp4"
```

## Subtitles LAST (Hard Rule 1)

```bash
# Burn subtitles after all overlays are composited
ffmpeg -i "edit/with_overlays.mp4" \
  -vf "subtitles=edit/master.srt:force_style='FontName=Helvetica,FontSize=18,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Shadow=0,Alignment=2,MarginV=35'" \
  -c:v libx264 -crf 18 -c:a copy \
  "edit/final.mp4"
```

## Grade Presets

### warm_cinematic
```bash
-vf "eq=contrast=1.05:saturation=0.85,curves=r='0/0 0.3/0.25 0.8/0.72 1/0.88':g='0/0 0.3/0.28 0.8/0.76 1/0.93':b='0/0 0.3/0.32 0.8/0.68 1/0.82',hue=s=0.9"
```

### neutral_punch
```bash
-vf "eq=contrast=1.1:brightness=0.01:saturation=1.05,curves=all='0/0 0.15/0.12 0.5/0.5 0.85/0.88 1/1'"
```

## Generate SRT with Output-Timeline Offsets (Hard Rule 5)

```python
def build_srt(edl_ranges, transcripts):
    """
    Build master.srt with correct output-timeline timestamps.
    output_time = word.start - segment_start + segment_offset
    """
    subs = []
    offset = 0.0
    for i, seg in enumerate(edl_ranges):
        seg_dur = seg['end'] - seg['start']
        words = get_words_in_range(transcripts[seg['source']], seg['start'], seg['end'])
        for chunk in chunk_words(words, max_words=2):
            start_out = chunk[0]['start'] - seg['start'] + offset
            end_out = chunk[-1]['end'] - seg['start'] + offset
            text = ' '.join(w['word'] for w in chunk).upper()
            subs.append((start_out, end_out, text))
        offset += seg_dur
    return format_srt(subs)
```

## Filler Word Micro-Cut

```bash
# Cut out a filler word [filler_start, filler_end] from a segment
# Creates two pieces with 30ms fades at boundaries

ffmpeg -i seg.mp4 -ss 0 -to $filler_start \
  -af "afade=t=out:st=$(echo "$filler_start - 0.03" | bc):d=0.03" \
  -c:v libx264 -crf 18 -c:a aac piece_a.mp4

ffmpeg -i seg.mp4 -ss $filler_end \
  -af "afade=t=in:st=0:d=0.03" \
  -c:v libx264 -crf 18 -c:a aac piece_b.mp4

# Then concat piece_a + piece_b losslessly
```

## Preview Render (720p Fast)

```bash
ffmpeg -f concat -safe 0 -i concat_list.txt \
  -vf "scale=1280:720,subtitles=master.srt:force_style='...'" \
  -c:v libx264 -crf 23 -preset fast \
  -c:a aac -b:a 128k \
  edit/preview.mp4
```

## ffprobe — Inspect Source

```bash
# Duration, fps, resolution
ffprobe -v quiet -print_format json -show_streams -show_format "$input"

# Verify output duration matches EDL expectation
ffprobe -v quiet -show_entries format=duration -of csv=p=0 edit/final.mp4
```
