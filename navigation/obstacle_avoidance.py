from hardware.ultrasonic import get_distance
from hardware.motor_control import move_forward, stop_motors
import time

def avoid_obstacles():
    while True:
        distance = get_distance()
        print(f"Distance: {distance:.2f} cm")

        if distance < 30:  # Stop if an obstacle is detected
            print("Obstacle detected! Stopping.")
            stop_motors()
            time.sleep(1)
        else:
            move_forward(50)  # Move forward if clear

        time.sleep(0.1)

if __name__ == "__main__":
    avoid_obstacles()
