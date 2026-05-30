from fastapi import APIRouter
import sqlite3

router = APIRouter()

@router.get("/health")
def health():

    try:

        conn = sqlite3.connect("data/store.db")
        cursor = conn.cursor()

        cursor.execute("""
        SELECT COUNT(*)
        FROM events
        """)

        total_events = cursor.fetchone()[0]

        conn.close()

        return {
            "status": "healthy",
            "database": "connected",
            "total_events": total_events
        }

    except Exception as e:

        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }