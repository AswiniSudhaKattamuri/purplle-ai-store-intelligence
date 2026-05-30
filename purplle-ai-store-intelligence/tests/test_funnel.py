def test_funnel():

    funnel = {
        "entry": 30,
        "zone_visit": 31,
        "billing_queue": 21,
        "purchase": 8,
        "conversion_rate": 26.67
    }

    assert funnel["entry"] >= 0
    assert funnel["purchase"] >= 0
    assert funnel["conversion_rate"] >= 0