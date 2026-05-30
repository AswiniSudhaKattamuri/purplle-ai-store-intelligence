import requests
from datetime import datetime
import random
import uuid


def emit_event(
    visitor_id,
    event_type,
    zone_id,
    is_staff=False
):

    payload = [
        {
            "event_id": str(uuid.uuid4()),
            "store_id": "STORE_001",
            "camera_id": "CAM_01",
            "visitor_id": visitor_id,
            "event_type": event_type,
            "timestamp": datetime.now().isoformat(),
            "zone_id": zone_id,
            "dwell_ms": random.randint(1000, 10000),
            "is_staff": is_staff,
            "confidence": 0.95
        }
    ]

    response = requests.post(
        "http://127.0.0.1:8000/events/ingest",
        json=payload
    )

    print(response.json())


def simulate_customer_journey(
    visitor_id,
    is_staff=False
):

    emit_event(
        visitor_id,
        "ENTRY",
        "ENTRANCE",
        is_staff
    )

    if random.random() < 0.9:
        emit_event(
            visitor_id,
            "ZONE_VISIT",
            "COSMETICS",
            is_staff
        )

    if random.random() < 0.6:
        emit_event(
            visitor_id,
            "BILLING_QUEUE",
            "BILLING",
            is_staff
        )

    if random.random() < 0.4:
        emit_event(
            visitor_id,
            "PURCHASE",
            "CHECKOUT",
            is_staff
        )

    emit_event(
        visitor_id,
        "EXIT",
        "ENTRANCE",
        is_staff
    )

    if random.random() < 0.3:

        emit_event(
            visitor_id,
            "REENTRY",
            "ENTRANCE",
            is_staff
        )

        emit_event(
            visitor_id,
            "ZONE_VISIT",
            "COSMETICS",
            is_staff
        )

        emit_event(
            visitor_id,
            "EXIT",
            "ENTRANCE",
            is_staff
        )