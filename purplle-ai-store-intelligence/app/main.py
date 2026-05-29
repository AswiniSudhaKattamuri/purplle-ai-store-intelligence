from fastapi import FastAPI
from app.health import router as health_router

app = FastAPI()

app.include_router(health_router)

@app.get("/")
def home():
    return {
        "status": "running",
        "project": "Purplle AI Store Intelligence"
    }