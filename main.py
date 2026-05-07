import cv2
import numpy as np
from ultralytics import YOLO
from sort import Sort

# Load model
model = YOLO("yolov8n.pt")

# Tracker
tracker = Sort()

# Camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO detection
    results = model(frame)
    r = results[0]
    boxes = r.boxes

    detections = []

    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        conf = float(box.conf[0])

        if conf > 0.5:
            detections.append([int(x1), int(y1), int(x2), int(y2), conf])

    detections = np.array(detections)

    # Tracking
    tracked_objects = tracker.update(detections)

    # Draw
    for obj in tracked_objects:
        x1, y1, x2, y2, obj_id = obj

        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
        cv2.putText(frame, f"ID: {int(obj_id)}",
                    (int(x1), int(y1)-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                    (0,255,0), 2)

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()