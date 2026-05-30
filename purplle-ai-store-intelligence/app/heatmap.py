from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get("/stores/{store_id}/heatmap")
def get_heatmap(store_id: str):

    conn = sqlite3.connect("data/store.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT zone_id, COUNT(*)
    FROM events
    WHERE store_id = ?
    GROUP BY zone_id
    ORDER BY COUNT(*) DESC
    """, (store_id,))

    rows = cursor.fetchall()

    conn.close()

    zones = []

    for zone_id, count in rows:

        zones.append({
            "zone_id": zone_id,
            "visits": count
        })

    return {
        "store_id": store_id,
        "zones": zones
    }