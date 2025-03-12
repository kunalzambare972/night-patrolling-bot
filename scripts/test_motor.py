from hardware.motor_control import move_forward, stop_motors
import time

print("Moving forward for 2 seconds")
move_forward(70)
time.sleep(2)
stop_motors()
print("Test complete.")
