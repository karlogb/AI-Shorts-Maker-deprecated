# 🎥 Story Video Generator

This project automatically creates short horror videos with voiceover, subtitles, background music, and dark visuals using AI tools. Perfect for TikTok, YouTube Shorts, or Reels.

## 🧠 What It Does

- 📝 Generates a story using OpenAI GPT-4
- 🗣️ Converts the story into voiceover using ElevenLabs
- 🎬 Creates a vertical video with MoviePy
- 🔤 Adds auto-synced subtitles
- 🎵 Optionally includes dark ambient background music

## 🗂️ Project Structure

```
creepy_video_generator/
├── .env
├── generate_story.py
├── generate_voiceover.py
├── create_video.py
├── add_subtitles.py
├── main.py
└── output/
```

## 🔧 Setup

1. Clone the repo
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create `.env` with your keys:
```
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
VOICE_ID=your_elevenlabs_voice_id
```

4. Run the generator:
```bash
python main.py
```

The video will be saved to `output/` with voiceover, subtitles and visuals.
