import RPi.GPIO as GPIO
import time

# Set GPIO pin for servo
servo_pin = 18

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Set PWM frequency
pwm = GPIO.PWM(servo_pin, 50)  
pwm.start(0)  # Start with initial duty cycle at 0

# Function to rotate servo to desired angle
def set_servo_angle(angle):
    duty = angle / 180 * (2 + 0.01)  # Calculate duty cycle based on angle
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.1)  # Small delay for stability



# Example usage:
set_servo_angle(0)  # Rotate to 0 degrees
time.sleep(1)
set_servo_angle(90) # Rotate to 90 degrees
time.sleep(1)
set_servo_angle(180) # Rotate to 180 degrees
time.sleep(1)

# Clean up GPIO

pwm.stop()
GPIO.cleanup()
