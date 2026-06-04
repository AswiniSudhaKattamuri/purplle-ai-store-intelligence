from fastapi import APIRouter
from pipeline.tracker import track_people

router = APIRouter()

@router.get("/video/metrics")
def get_video_metrics():

    return track_people(
        "data/Videos/CAM 1.mp4"
    )