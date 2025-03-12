from hardware.motor_control import move_forward, stop_motors
import time

# Define waypoints (x, y positions)
waypoints = [(0, 0), (5, 5), (10, 0), (5, -5), (0, 0)]

def follow_path():
    for point in waypoints:
        print(f"Moving to waypoint {point}")
        move_forward(60)
        time.sleep(2)  # Move for a fixed duration (replace with actual path logic)
        stop_motors()
        time.sleep(1)

if __name__ == "__main__":
    follow_path()
