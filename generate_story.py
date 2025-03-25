import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_story(prompt="Write a short story with a mysterious tone."):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
        max_tokens=600
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    story = generate_story()
    print(story)
