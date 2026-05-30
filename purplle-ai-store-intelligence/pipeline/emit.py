import requests
from datetime import datetime

def emit_entry_event(visitor_id):

    payload = [
        {
            "event_id": visitor_id,
            "store_id": "STORE_001",
            "camera_id": "CAM_01",
            "visitor_id": visitor_id,
            "event_type": "ENTRY",
            "timestamp": datetime.now().isoformat(),
            "zone_id": "ENTRANCE",
            "dwell_ms": 0,
            "is_staff": False,
            "confidence": 0.95
        }
    ]

    response = requests.post(
        "http://127.0.0.1:8000/events/ingest",
        json=payload
    )

    print(response.json())