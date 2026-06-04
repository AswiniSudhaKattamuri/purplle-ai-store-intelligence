
import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def detect_people(source_path):

    detections = []

    # IMAGE SUPPORT
    if source_path.endswith((".jpg", ".jpeg", ".png")):

        results = model(source_path)

        for result in results:

            for box in result.boxes:

                class_id = int(box.cls[0])

                if class_id == 0:

                    detections.append({
                        "class": "person",
                        "confidence": float(box.conf[0])
                    })

        print(
            f"People detected: {len(detections)}"
        )

        return detections

    # VIDEO SUPPORT
    elif source_path.endswith((".mp4", ".avi", ".mov")):

        cap = cv2.VideoCapture(source_path)

        max_frames = 1000
        max_people = 0
        frame_count = 0

        while True:

            ret, frame = cap.read()

            if not ret:
                break

            frame_count += 1

            if frame_count > max_frames:
                break

            # Process every 10th frame
            if frame_count % 10 != 0:
                continue

            print(
                f"Processing Frame {frame_count}"
            )

            results = model(frame)

            people_count = 0

            for result in results:

                for box in result.boxes:

                    class_id = int(box.cls[0])

                    if class_id == 0:
                        people_count += 1

            print(
                f"Frame {frame_count}: {people_count} people"
            )

            if people_count > max_people:

                max_people = people_count

                print(
                    f"New Maximum Found: {max_people} people"
                )

        cap.release()

        print(
            f"Maximum people detected: {max_people}"
        )

        return [
            {
                "class": "person",
                "confidence": 1.0
            }
            for _ in range(max_people)
        ]

    else:

        print("Unsupported file format")

        return []