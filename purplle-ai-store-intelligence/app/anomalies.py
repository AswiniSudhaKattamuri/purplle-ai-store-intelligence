from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get("/stores/{store_id}/anomalies")
def get_anomalies(store_id: str):

    conn = sqlite3.connect("data/store.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM events
    WHERE store_id = ?
    """, (store_id,))

    total_events = cursor.fetchone()[0]

    conn.close()

    anomalies = []

    if total_events == 0:
        anomalies.append({
            "type": "NO_ACTIVITY",
            "message": "No events recorded for this store"
        })

    return {
        "store_id": store_id,
        "anomalies": anomalies
    }