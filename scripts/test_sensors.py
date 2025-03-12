from hardware.ultrasonic import get_distance
from hardware.pir_sensor import detect_motion

print(f"Ultrasonic Distance: {get_distance()} cm")
print(f"PIR Motion Detected: {detect_motion()}")
