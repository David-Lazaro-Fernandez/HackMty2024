"""
Audio Route for all the endpoints related to audio processing.
"""
import os
import logging
from fastapi import APIRouter, File, UploadFile
from helpers.firebase_helper import firebase
from fastapi.responses import Response

# Logger configuration
logger = logging.getLogger(__name__)
datastore = APIRouter()


@datastore.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    This endpoint uploads a file and returns the transcription of the audio file using OpenAI SDK.
    """
    try:
        await firebase.upload_file(file_object=file, unique_id="12345")

    except Exception as e:
        logger.error(f"Error uploading file: {e}")
        return {"message": "Error uploading file."}
    
    finally:
        file.file.close()

    return {"message": "File uploaded successfully."}

@datastore.get("/list")
async def list_audio_files():
    """
    This endpoint lists all the files uploaded to the Firebase storage.
    """
    try:
        files = await firebase.list_files(unique_id="12345")

    except Exception as e:
        logger.error(f"Error listing files: {e}")
        return {"message": "Error listing files."}

    return {"files": files}

@datastore.get("/download")
async def download_file(file_name: str, file_type: str, media_type: str):
    """
    This endpoint downloads a file from the Firebase storage.
    """
    try:
        file = await firebase.get_file(file_name=file_name, file_type=file_type, unique_id="12345")
        headers = {'Content-Disposition': f'attachment; filename={file_name}'}
    except Exception as e:
        logger.error(f"Error downloading file: {e}")
        return {"message": "Error downloading file."}

    return Response(file.getvalue(), headers=headers, media_type=media_type)