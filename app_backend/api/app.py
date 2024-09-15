import os
import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.v1.audio import router
from routes.v1.datastore import datastore
from routes.v1.video import video

# Enable MPS Fallback for PyTorch
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

# Logger configuration
logger = logging.getLogger(__name__)

# FastAPI configuration
app = FastAPI()
app.include_router(router, prefix="/v1/audio", tags=["audio"])
app.include_router(datastore, prefix="/v1/datastore", tags=["datastore"])
app.include_router(video, prefix="/v1/video", tags=["video"])
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

# Health endpoint
@app.get("/")
def read_root():
    return {"Hello": "World"}