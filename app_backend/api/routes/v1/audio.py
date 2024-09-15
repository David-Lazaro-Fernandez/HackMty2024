"""
Audio Route for all the endpoints related to audio processing.
"""
from helpers.ai_helper import Agent
from fastapi import APIRouter, File, UploadFile
from tempfile import NamedTemporaryFile

router = APIRouter()
AI = Agent("openai")

@router.post("/transcript")
def upload_audio_file(file: UploadFile = File(...)):
    """
    This endpoint uploads a file and returns the transcription of the audio file using OpenAI SDK.
    """
    try:
        contents = file.file.read()
        print(file.filename)
        with open(file.filename, "wb") as temp_file:
            temp_file.write(contents)

        text = AI.transcript_to_text(file_object=file.filename)
    except Exception:
        return {"message": "An error occurred while processing the audio file."}

    finally:
        file.file.close()

    return {"transcription": text}
