#!/usr/bin/env python3
import time
import math
from adafruit_servokit import ServoKit

# Initialize the ServoKit with 16 channels
kit = ServoKit(channels=16)

# Configure servos with your specific pulse widths (in microseconds)
kit.servo[0].set_pulse_width_range(400, 1800)  # Hip servo
kit.servo[1].set_pulse_width_range(500, 2000)  # Tibia servo

timeBetween = 2

# Test movement
try:
    while True:
        print("Resetting")
        # Move to 2 degrees
        kit.servo[0].angle = 10
        kit.servo[1].angle = 2
        time.sleep(timeBetween)
        
        print("Slowly increasing")
        start_time = time.time()
        for i in range(101):
            t = i / 100
            ease = (1 - math.cos(t * math.pi)) / 2
            kit.servo[0].angle = 180 * ease
            kit.servo[1].angle = 180 * ease
            time.sleep(0.03)
except KeyboardInterrupt:
    print("\nDisabling servos...")
    kit.servo[0].angle = None
    kit.servo[1].angle = None          
    