#!/usr/bin/env python3

import robot
from time import sleep
r = robot.Robot()
# r.set_left(80)
# r.set_right(80)
# print("l dist:", r.left_distance_sensor.distance())
# print("l dist:", r.left_distance_sensor.distance())
#sleep(1)
r.pan_servo.center()
sleep(1)
r.pan_servo.pan(45)
sleep(1)
r.pan_servo.pan(-45)
sleep(1)
r.pan_servo.center()
sleep(1)
