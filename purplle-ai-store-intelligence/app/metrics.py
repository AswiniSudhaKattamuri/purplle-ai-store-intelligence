from fastapi import APIRouter
from app.database import cursor

router = APIRouter()

@router.get("/stores/{store_id}/metrics")
def get_metrics(store_id: str):

    # Count only customers
    cursor.execute("""
    SELECT COUNT(DISTINCT visitor_id)
    FROM events
    WHERE store_id = ?
    AND is_staff = 0
    """, (store_id,))

    visitors = cursor.fetchone()[0]

    # Count only customer purchases
    cursor.execute("""
    SELECT COUNT(*)
    FROM events
    WHERE store_id = ?
    AND event_type = 'PURCHASE'
    AND is_staff = 0
    """, (store_id,))

    purchases = cursor.fetchone()[0]

    # Count staff members
    cursor.execute("""
    SELECT COUNT(DISTINCT visitor_id)
    FROM events
    WHERE store_id = ?
    AND is_staff = 1
    """, (store_id,))

    staff_count = cursor.fetchone()[0]

    conversion_rate = 0

    if visitors > 0:
        conversion_rate = round(
            (purchases / visitors) * 100,
            2
        )

    return {
        "store_id": store_id,
        "unique_visitors": visitors,
        "staff_count": staff_count,
        "purchase_count": purchases,
        "conversion_rate": conversion_rate
    }