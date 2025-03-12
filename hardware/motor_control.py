import RPi.GPIO as GPIO
import time

# Motor Pins
LEFT_MOTOR_IN1 = 17
LEFT_MOTOR_IN2 = 18
LEFT_MOTOR_EN  = 27
RIGHT_MOTOR_IN1 = 22
RIGHT_MOTOR_IN2 = 23
RIGHT_MOTOR_EN  = 24

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([LEFT_MOTOR_IN1, LEFT_MOTOR_IN2, LEFT_MOTOR_EN, 
            RIGHT_MOTOR_IN1, RIGHT_MOTOR_IN2, RIGHT_MOTOR_EN], GPIO.OUT)

left_motor_pwm = GPIO.PWM(LEFT_MOTOR_EN, 100)
right_motor_pwm = GPIO.PWM(RIGHT_MOTOR_EN, 100)
left_motor_pwm.start(0)
right_motor_pwm.start(0)

def move_forward(speed=50):
    GPIO.output(LEFT_MOTOR_IN1, GPIO.HIGH)
    GPIO.output(LEFT_MOTOR_IN2, GPIO.LOW)
    GPIO.output(RIGHT_MOTOR_IN1, GPIO.HIGH)
    GPIO.output(RIGHT_MOTOR_IN2, GPIO.LOW)
    left_motor_pwm.ChangeDutyCycle(speed)
    right_motor_pwm.ChangeDutyCycle(speed)

def stop_motors():
    GPIO.output([LEFT_MOTOR_IN1, LEFT_MOTOR_IN2, RIGHT_MOTOR_IN1, RIGHT_MOTOR_IN2], GPIO.LOW)
    left_motor_pwm.ChangeDutyCycle(0)
    right_motor_pwm.ChangeDutyCycle(0)
