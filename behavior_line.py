#!/usr/bin/env python3

import robot
from time import sleep
r = robot.Robot()
r.set_left(80)
r.set_right(80)
sleep(1)
r.set_left(0)
r.set_right(0)
sleep(1)
r.set_left(-20)
r.set_right(-20)
sleep(3)

