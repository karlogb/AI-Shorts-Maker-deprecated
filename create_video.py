from moviepy.editor import *
import os

def create_video(audio_path, output_path, background_video=None, bg_music_path="background_music.mp3"):
    audio = AudioFileClip(audio_path)
    if background_video and os.path.exists(background_video):
        video = VideoFileClip(background_video).subclip(0, audio.duration)
    else:
        video = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=audio.duration)
    
    if os.path.exists(bg_music_path):
        bg_music = AudioFileClip(bg_music_path).subclip(0, audio.duration).volumex(0.2)
        combined_audio = CompositeAudioClip([audio, bg_music])
    else:
        combined_audio = audio
    
    video = video.set_audio(combined_audio)
    video.write_videofile(output_path, fps=24)

if __name__ == "__main__":
    create_video("output/audio.mp3", "output/video_raw.mp4")
