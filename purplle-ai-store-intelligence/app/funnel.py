from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get("/stores/{store_id}/funnel")
def get_funnel(store_id: str):

    conn = sqlite3.connect("data/store.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT event_type, COUNT(*)
        FROM events
        WHERE store_id = ?
        AND is_staff = 0
        GROUP BY event_type
        """,
        (store_id,)
    )

    rows = cursor.fetchall()

    conn.close()

    funnel = {
        "store_id": store_id,
        "entry": 0,
        "zone_visit": 0,
        "billing_queue": 0,
        "purchase": 0,
        "conversion_rate": 0
    }

    for event_type, count in rows:

        if event_type == "ENTRY":
            funnel["entry"] = count

        elif event_type == "ZONE_VISIT":
            funnel["zone_visit"] = count

        elif event_type == "BILLING_QUEUE":
            funnel["billing_queue"] = count

        elif event_type == "PURCHASE":
            funnel["purchase"] = count

    if funnel["entry"] > 0:
        funnel["conversion_rate"] = round(
            (funnel["purchase"] / funnel["entry"]) * 100,
            2
        )

    return funnel