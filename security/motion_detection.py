import cv2
import time

def camera_motion_detection():
    cap = cv2.VideoCapture(0)
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    while True:
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            filename = f"data/images/intruder_{timestamp}.jpg"
            cv2.imwrite(filename, frame1)
            print(f"Motion detected! Image saved as {filename}")
            time.sleep(2)

        frame1, frame2 = frame2, cap.read()[1]

    cap.release()
    cv2.destroyAllWindows()
