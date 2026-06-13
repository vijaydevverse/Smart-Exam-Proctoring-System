import cv2
import csv
import os
from datetime import datetime

os.makedirs("screenshots", exist_ok=True)
os.makedirs("logs", exist_ok=True)

def save_screenshot(frame, reason):

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"screenshots/{reason}_{timestamp}.jpg"

    cv2.imwrite(filename, frame)

    print(f"Screenshot Saved: {filename}")

def log_violation(reason):

    file_exists = os.path.exists("logs/violations.csv")

    with open(
        "logs/violations.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["Time", "Violation"])

        writer.writerow([
            datetime.now(),
            reason
        ])

    print(f"Violation Logged: {reason}")