def test_anomalies():

    anomalies = [
        {
            "type": "QUEUE_SPIKE",
            "severity": "MEDIUM"
        }
    ]

    assert isinstance(anomalies, list)
    assert len(anomalies) > 0
    assert anomalies[0]["type"] == "QUEUE_SPIKE"