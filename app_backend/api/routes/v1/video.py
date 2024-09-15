"""
Video Route for all the endpoints related to video processing and analytics.
"""
import os
import json
import logging
from helpers.mongo_streamer_helper import MongoStreamer
from helpers.firebase_helper import firebase
from fastapi import APIRouter, WebSocket
from fastapi.responses import Response

logger = logging.getLogger(__name__)
video = APIRouter()

mongo = MongoStreamer("hack")

@video.websocket("/stream")
async def stream_video_data(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()

        await mongo.stream_insert("video_data", json.loads(data))
        await websocket.send_text("Data inserted successfully.")

@video.get("/download")
async def download_file(file_name: str):
    """
    This endpoint downloads a file from the Firebase storage.
    """
    try:
        file = await firebase.get_file(file_name=file_name, file_type="video", unique_id="12345")
        headers = {'Content-Disposition': f'attachment; filename={file_name}'}
    except Exception as e:
        logger.error(f"Error downloading file: {e}")
        return {"message": "Error downloading file."}

    return Response(file.getvalue(), headers=headers, media_type="video/mp4")