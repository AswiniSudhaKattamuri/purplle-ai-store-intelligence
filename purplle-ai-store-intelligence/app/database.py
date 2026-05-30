import sqlite3

conn = sqlite3.connect("data/store.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    event_id TEXT,
    store_id TEXT,
    camera_id TEXT,
    visitor_id TEXT,
    event_type TEXT,
    timestamp TEXT,
    zone_id TEXT,
    dwell_ms INTEGER,
    is_staff INTEGER,
    confidence REAL
)
""")

conn.commit()