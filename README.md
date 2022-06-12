# LRP
Orion Robotics Learn Robotics Programming Using GoPiGo3

```
import robot
from time import sleep
r = robot.Robot()

# Read left distance sensor
print("l dist:", r.left_distance_sensor.distance())

# Read right distance sensor
print("r dist:", r.right_distance_sensor.distance())
sleep(1)

# Center pan servo
r.pan_servo.center()

# Set speed for left motor
r.set_left(80)
# Set speed for right motor
r.set_right(80)

```
