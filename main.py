import threading
import time
from hardware.motor_control import move_forward, stop_motors
from hardware.ultrasonic import get_distance
from hardware.pir_sensor import detect_motion
from security.motion_detection import camera_motion_detection

def patrol():
    try:
        while True:
            distance = get_distance()
            print(f"Distance: {distance:.2f} cm")
            
            if distance < 30:
                print("Obstacle detected! Stopping.")
                stop_motors()
                time.sleep(1)
            else:
                move_forward(60)

            if detect_motion():
                print("Motion detected! Capturing image.")
                camera_motion_detection()

            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Stopping patrol.")
        stop_motors()

if __name__ == "__main__":
    camera_thread = threading.Thread(target=camera_motion_detection, daemon=True)
    camera_thread.start()
    patrol()
