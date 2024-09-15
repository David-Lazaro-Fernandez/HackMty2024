import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.v1.audio import router

os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "1"

app = FastAPI()

app.include_router(router, prefix="/v1/audio", tags=["audio"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

@app.get("/")
def read_root():
    return {"Hello": "World"}