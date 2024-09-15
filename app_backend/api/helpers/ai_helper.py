"""
This is a helper class for the AI agent. It will contain all the methods that the AI agent will use to make decisions.
"""
import os
import io
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class Agent():
    def __init__(self, provider: str):
        kwargs = {
            "api_key": os.getenv("FRIDA_AI_KEY"),
            "base_url": os.getenv("FRIDA_AI_BASE_URL")
        } if provider == "firda" else {
            "api_key": os.getenv("OPEN_AI_KEY")
        }
        self.client = OpenAI(**kwargs)
    
    def transcript_to_text(self, file_object):
        audio_data = io.BufferedReader(file_object)

        transcription = self.client.audio.transcriptions.create(
            model="whisper-1",
            file=("audio.m4a", audio_data),
            response_format="srt"
        )

        return transcription
