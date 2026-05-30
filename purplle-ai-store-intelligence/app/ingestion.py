from app.database import conn, cursor

def save_events(events):

    for event in events:

        cursor.execute("""
        INSERT INTO events VALUES (
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
        )
        """, (
            event.event_id,
            event.store_id,
            event.camera_id,
            event.visitor_id,
            event.event_type,
            event.timestamp,
            event.zone_id,
            event.dwell_ms,
            int(event.is_staff),
            event.confidence
        ))

    conn.commit()