from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get("/stores/{store_id}/anomalies")
def get_anomalies(store_id: str):

    conn = sqlite3.connect("data/store.db")
    cursor = conn.cursor()

    anomalies = []

    # Total Events
    cursor.execute("""
    SELECT COUNT(*)
    FROM events
    WHERE store_id = ?
    """, (store_id,))

    total_events = cursor.fetchone()[0]

    if total_events == 0:
        anomalies.append({
            "type": "NO_ACTIVITY",
            "severity": "HIGH",
            "message": "No events recorded for this store"
        })

    # Unique Visitors
    cursor.execute("""
    SELECT COUNT(DISTINCT visitor_id)
    FROM events
    WHERE store_id = ?
    """, (store_id,))

    visitors = cursor.fetchone()[0]

    # Purchases
    cursor.execute("""
    SELECT COUNT(*)
    FROM events
    WHERE store_id = ?
    AND event_type = 'PURCHASE'
    """, (store_id,))

    purchases = cursor.fetchone()[0]

    # Billing Queue
    cursor.execute("""
    SELECT COUNT(*)
    FROM events
    WHERE store_id = ?
    AND event_type = 'BILLING_QUEUE'
    """, (store_id,))

    queue_count = cursor.fetchone()[0]

    # Zone Statistics
    cursor.execute("""
    SELECT zone_id, COUNT(*)
    FROM events
    WHERE store_id = ?
    GROUP BY zone_id
    """, (store_id,))

    zones = cursor.fetchall()

    # LOW_CONVERSION
    if visitors > 0:

        conversion_rate = (
            purchases / visitors
        ) * 100

        if conversion_rate < 20:

            anomalies.append({
                "type": "LOW_CONVERSION",
                "severity": "MEDIUM",
                "message": f"Conversion rate is only {conversion_rate:.2f}%"
            })

    # QUEUE_SPIKE
    if queue_count > purchases * 2 and queue_count > 5:

        anomalies.append({
            "type": "QUEUE_SPIKE",
            "severity": "MEDIUM",
            "message": "High billing queue compared to purchases"
        })

    # DEAD_ZONE
    if zones:

        max_visits = max(
            count for _, count in zones
        )

        for zone_id, count in zones:

            if count < 5:

                anomalies.append({
                    "type": "DEAD_ZONE",
                    "severity": "LOW",
                    "message": f"{zone_id} has unusually low traffic ({count} visits)"
                })

    conn.close()

    return {
        "store_id": store_id,
        "anomalies": anomalies
    }