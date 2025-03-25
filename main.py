import os
from generate_story import generate_story
from generate_voiceover import generate_voiceover
from create_video import create_video
from add_subtitles import add_subtitles
import uuid

def main():
    os.makedirs("output", exist_ok=True)
    uid = str(uuid.uuid4())
    
    print("Generating story...")
    story = generate_story()
    story_path = "output/story.txt"
    with open(story_path, "w", encoding="utf-8") as f:
        f.write(story)
    
    audio_path = f"output/{uid}_audio.mp3"
    raw_video_path = f"output/{uid}_video_raw.mp4"
    final_video_path = f"output/{uid}_final.mp4"
    
    print("Generating voiceover...")
    generate_voiceover(story, audio_path)
    
    print("Creating base video...")
    create_video(audio_path, raw_video_path, background_video="background_video.mp4")
    
    print("Adding subtitles...")
    add_subtitles(raw_video_path, story, final_video_path)
    
    print(f"Done! Final video saved at: {final_video_path}")

if __name__ == "__main__":
    main()
