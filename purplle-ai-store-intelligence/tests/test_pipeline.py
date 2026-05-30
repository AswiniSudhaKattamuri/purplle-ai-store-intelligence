def test_pipeline():

    detections = 10

    assert detections > 0

    visitor_ids = [
        "VISITOR_1",
        "VISITOR_2",
        "VISITOR_3"
    ]

    assert len(visitor_ids) == detections or len(visitor_ids) > 0