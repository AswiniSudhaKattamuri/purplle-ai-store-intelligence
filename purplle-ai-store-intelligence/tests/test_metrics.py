def test_metrics():

    data = {
        "store_id": "STORE_001",
        "unique_visitors": 11,
        "staff_count": 1,
        "purchase_count": 8,
        "conversion_rate": 72.73
    }

    assert data["unique_visitors"] > 0
    assert data["staff_count"] >= 0
    assert data["purchase_count"] >= 0
    assert data["conversion_rate"] >= 0