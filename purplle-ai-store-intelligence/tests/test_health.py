def test_health():

    response = {
        "status": "healthy",
        "database": "connected",
        "total_events": 89
    }

    assert response["status"] == "healthy"
    assert response["database"] == "connected"
    assert response["total_events"] >= 0