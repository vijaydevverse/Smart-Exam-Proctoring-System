from ultralytics import YOLO
import cv2
from logger import save_screenshot, log_violation

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

phone_detected = False

while True:

    ret, frame = cap.read()

    if not ret:
        break

    # Detect objects
    results = model(frame, verbose=False)

    current_phone = False

    for r in results:

        for box in r.boxes:

            cls = int(box.cls[0])

            label = model.names[cls]

            # Show everything YOLO detects
            print("Detected:", label)

            # Phone detection
            if label == "cell phone":

                current_phone = True

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Red rectangle around phone
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 0, 255),
                    2
                )

                # Warning text
                cv2.putText(
                    frame,
                    "CHEATING: PHONE DETECTED",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

    # Save screenshot and log only once
    if current_phone and not phone_detected:

        save_screenshot(frame, "phone_detected")

        log_violation("Phone Detected")

        print("Phone violation saved!")

        phone_detected = True

    elif not current_phone:

        phone_detected = False

    cv2.imshow("Phone Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()