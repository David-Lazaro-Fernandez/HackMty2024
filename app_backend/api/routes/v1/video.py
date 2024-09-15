"""
Video Route for all the endpoints related to video processing and analytics.
"""
import os
import json
import logging
from helpers.mongo_streamer_helper import MongoStreamer
from helpers.firebase_helper import firebase
from fastapi import APIRouter, WebSocket

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
