import cv2
from logger import save_screenshot

cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if ret:
    save_screenshot(frame, "test")

cap.release()

print("Done")