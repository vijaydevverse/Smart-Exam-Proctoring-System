import cv2
import mediapipe as mp
from ultralytics import YOLO

from logger import save_screenshot
from logger import log_violation

# -----------------------------
# Face Detection
# -----------------------------

mp_face = mp.solutions.face_detection

face_detector = mp_face.FaceDetection(
    min_detection_confidence=0.6
)

# -----------------------------
# YOLO
# -----------------------------

model = YOLO("yolov8n.pt")

# -----------------------------
# Webcam
# -----------------------------

cap = cv2.VideoCapture(0)

multiple_face_detected = False
phone_detected = False

while True:

    ret, frame = cap.read()

    if not ret:
        break

    rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # -----------------------------
    # FACE DETECTION
    # -----------------------------

    face_results = face_detector.process(rgb)

    count = 0

    if face_results.detections:

        count = len(face_results.detections)

        for detection in face_results.detections:

            bbox = detection.location_data.relative_bounding_box

            h, w, _ = frame.shape

            x = int(bbox.xmin * w)
            y = int(bbox.ymin * h)

            bw = int(bbox.width * w)
            bh = int(bbox.height * h)

            cv2.rectangle(
                frame,
                (x, y),
                (x + bw, y + bh),
                (0, 255, 0),
                2
            )

    cv2.putText(
        frame,
        f"Faces: {count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # -----------------------------
    # MULTIPLE FACE CHEATING
    # -----------------------------

    if count > 1:

        cv2.putText(
            frame,
            "CHEATING: MULTIPLE FACES",
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

        if not multiple_face_detected:

            save_screenshot(
                frame,
                "multiple_faces"
            )

            log_violation(
                "Multiple Faces"
            )

            multiple_face_detected = True

    else:

        multiple_face_detected = False

    # -----------------------------
    # PHONE DETECTION
    # -----------------------------

    phone_found = False

    results = model(
        frame,
        verbose=False
    )

    for r in results:

        for box in r.boxes:

            cls = int(box.cls[0])

            label = model.names[cls]

            if label == "cell phone":

                phone_found = True

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )

                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 0, 255),
                    2
                )

                cv2.putText(
                    frame,
                    "PHONE DETECTED",
                    (20, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    2
                )

    if phone_found:

        if not phone_detected:

            save_screenshot(
                frame,
                "phone_detected"
            )

            log_violation(
                "Phone Detected"
            )

            phone_detected = True

    else:

        phone_detected = False

    # -----------------------------
    # DISPLAY
    # -----------------------------

    cv2.imshow(
        "Smart Exam Proctoring System",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()