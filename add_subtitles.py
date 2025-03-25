from moviepy.editor import *
import textwrap

def add_subtitles(video_path, text, output_path):
    video = VideoFileClip(video_path)
    duration = video.duration
    lines = textwrap.wrap(text, width=50)
    num_lines = len(lines)
    seconds_per_line = duration / num_lines
    
    clips = []
    for i, line in enumerate(lines):
        txt_clip = TextClip(line, fontsize=40, color='white', font='Arial-Bold',
                            bg_color='rgba(0,0,0,0.5)', size=(video.w * 0.9, None), method='caption')
        txt_clip = txt_clip.set_position(("center", "bottom")).set_duration(seconds_per_line).set_start(i * seconds_per_line)
        clips.append(txt_clip)
    
    final = CompositeVideoClip([video, *clips])
    final.write_videofile(output_path, fps=24)

if __name__ == "__main__":
    text = open("output/story.txt", "r", encoding="utf-8").read()
    add_subtitles("output/video_raw.mp4", text, "output/final_video.mp4")
