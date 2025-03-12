import RPi.GPIO as GPIO
import time

PIR_PIN = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

def detect_motion():
    return GPIO.input(PIR_PIN) == GPIO.HIGH
