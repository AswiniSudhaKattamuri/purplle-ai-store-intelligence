from fastapi import APIRouter
from app.database import cursor

router = APIRouter()

@router.get("/stores/{store_id}/metrics")
def get_metrics(store_id: str):

    cursor.execute("""
    SELECT COUNT(DISTINCT visitor_id)
    FROM events
    WHERE store_id = ?
    """, (store_id,))

    visitors = cursor.fetchone()[0]

    return {
        "store_id": store_id,
        "unique_visitors": visitors
    }