from detect import detect_people
from emit import emit_entry_event

detections = detect_people(
    "data/Images/test.jpg"
)

for i, person in enumerate(detections):

    emit_entry_event(
        f"VISITOR_{i+1}"
    )