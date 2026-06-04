from ultralytics import YOLO
import cv2


def track_people(video_path):

    model = YOLO("yolov8n.pt")

    cap = cv2.VideoCapture(video_path)

    unique_ids = set()

    frame_count = 0
    max_people = 0

    while True:

        ret, frame = cap.read()

        if not ret:
            break

        frame_count += 1

        if frame_count > 2000:
            break

        # Process every 10th frame
        if frame_count % 10 != 0:
            continue

        results = model.track(
            frame,
            persist=True,
            classes=[0],
            verbose=False
        )

        people_count = 0

        for result in results:

            if result.boxes.id is not None:

                ids = result.boxes.id.cpu().numpy()

                people_count = len(ids)

                for person_id in ids:

                    unique_ids.add(
                        int(person_id)
                    )

        max_people = max(
            max_people,
            people_count
        )

        print(
            f"Frame {frame_count} | "
            f"Unique Visitors: {len(unique_ids)} | "
            f"Current People: {people_count}"
        )

    cap.release()

    print("\n====================")
    print(
        f"Final Unique Visitors: {len(unique_ids)}"
    )
    print(
        f"Max Concurrent Visitors: {max_people}"
    )
    print("====================")

    return {
        "unique_visitors": len(unique_ids),
        "max_concurrent_visitors": max_people
    }