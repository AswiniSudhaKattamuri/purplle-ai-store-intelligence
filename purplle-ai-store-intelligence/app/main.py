from fastapi import FastAPI
from app.health import router as health_router
from app.models import Event
from app.metrics import router as metrics_router
from app.funnel import router as funnel_router
from app.anomalies import router as anomalies_router
from app.heatmap import router as heatmap_router
from app.ingestion import save_events
from app.video_metrics import router as video_router
app = FastAPI()

app.include_router(health_router)
app.include_router(metrics_router)
app.include_router(funnel_router)
app.include_router(anomalies_router)
app.include_router(heatmap_router)
app.include_router(video_router)

events_db = []

@app.post("/events/ingest")
def ingest(events: list[Event]):

    save_events(events)

    return {
        "received": len(events),
        "status": "stored"
    }

@app.get("/")
def home():
    return {
        "project": "Purplle AI Store Intelligence",
        "status": "running"
    }