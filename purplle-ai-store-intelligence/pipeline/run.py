from detect import detect_people
from emit import simulate_customer_journey
import random

detections = detect_people(
    "data/Images/test2.jpg"
)

person_count = len(detections)

for i in range(person_count):

    is_staff = random.random() < 0.2

    visitor_id = (
        f"STAFF_{i+1}"
        if is_staff
        else f"VISITOR_{i+1}"
    )

    simulate_customer_journey(
        visitor_id,
        is_staff
    )