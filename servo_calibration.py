from gpiozero import Servo
from time import sleep
import os

if os.geteuid() != 0:
    print("Please run with sudo")
    exit(1)

# Start with standard values and adjust
# Standard servo: 0.5ms to 2.5ms pulses
# But many servos can handle 0.4ms to 2.6ms or even wider

print("Servo Calibration Test")
print("=" * 40)

# Test different pulse widths
test_widths = [
    (0.4, 1.8, "Standard range")
]
   
try:
    servo = Servo(
        12,
        min_pulse_width=test_widths[0][0]/1000,  # Convert ms to seconds
        max_pulse_width=test_widths[0][1]/1000
    )
    
    print("  Moving to MIN...")
    servo.min()
    sleep(2)
    
    print("  Moving to MID...")
    servo.mid()
    sleep(2)
    
    print("  Moving to MAX...")
    servo.max()
    sleep(2)
    
    servo.close()
            
except Exception as e:
    print(f"  Error: {e}")