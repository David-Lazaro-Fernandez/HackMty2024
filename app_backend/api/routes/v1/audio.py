"""
Audio Route for all the endpoints related to audio processing.
"""
import os
import logging
from helpers.parser import parse_srt
from helpers.ai_helper import Agent
from helpers.mongo_helper import Mongo
from helpers.firebase_helper import firebase
from fastapi import APIRouter, File, UploadFile
from tempfile import NamedTemporaryFile
from transformers import pipeline

# Logger configuration
logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize the MongoDB client
mongo = Mongo("hack")

# Initialize the AI agent and the sentiment classifier
AI = Agent("openai")
classifier = pipeline(
    "sentiment-analysis",
    model="finiteautomata/beto-sentiment-analysis",
    device="mps"
)

@router.get("/analyze")
async def analyze_audio_file(file_name: str):
    """
    This endpoint uploads a file and returns the transcription of the audio file using OpenAI SDK.
    """
    try:
        file = await firebase.get_file(file_name=file_name, file_type="audio", unique_id="12345")

        srt_text = AI.transcript_to_text(file_object=file)
        parsed_transcript = parse_srt(srt_text)
        sentences = [text['content'] for text in parsed_transcript]
        sentiment = classifier(sentences)

        analysis = [
            {
                "data": text,
                "sentiment": sentiment
            } for text, sentiment in zip(parsed_transcript, sentiment)
        ]

        clean_text = " ".join(sentences)

        data = {
            "context": clean_text,
            "sentiment": analysis
        }

        mongo.insert_document("audio_transcripts", data)
        
    except Exception as e:
        logger.error(e)
        return {"message": "An error occurred while processing the audio file."}

    finally:
        data["_id"] = str(data["_id"])

    return {"transcription": data}
