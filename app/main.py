import os
import socket
from fastapi import FastAPI

API_NUMBER = os.getenv("API_NUMBER", "1")

app = FastAPI(title=f"Baseline Model API {API_NUMBER}")


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "api_number": API_NUMBER,
        "host": socket.gethostname(),
    }


@app.get("/info")
async def info():
    return {
        "service": f"baseline_model_api_{API_NUMBER}",
        "description": "API container for batch calculations",
    }
