from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_people(image_path):

    results = model(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])

            if class_id == 0:

                detections.append({
                    "class": "person",
                    "confidence": float(box.conf[0])
                })

    return detections