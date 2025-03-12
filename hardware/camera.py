import cv2
import time

def capture_image():
    cap = cv2.VideoCapture(0)  # Open camera
    ret, frame = cap.read()
    
    if ret:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"data/images/captured_{timestamp}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image saved: {filename}")

    cap.release()
