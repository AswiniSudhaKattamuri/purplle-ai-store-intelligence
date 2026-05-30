def test_metrics():

    data = {
        "store_id": "STORE_001",
        "unique_visitors": 10
    }

    assert data["unique_visitors"] >= 0