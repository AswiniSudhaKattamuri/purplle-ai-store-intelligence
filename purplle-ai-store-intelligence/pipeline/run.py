from detect import detect_people
from emit import simulate_customer_journey

detections = detect_people(
    "data/Images/test.jpg"
)

for i, person in enumerate(detections):

    simulate_customer_journey(
        f"VISITOR_{i+1}"
    )