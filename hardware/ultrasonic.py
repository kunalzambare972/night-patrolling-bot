import RPi.GPIO as GPIO
import time

TRIG = 5
ECHO = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

def get_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.0002)
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    start_time, stop_time = time.time(), time.time()
    
    while GPIO.input(ECHO) == 0:
        start_time = time.time()
    
    while GPIO.input(ECHO) == 1:
        stop_time = time.time()
    
    distance = ((stop_time - start_time) * 34300) / 2
    return distance
