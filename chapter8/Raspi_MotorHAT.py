#!/usr/bin/env python3

# FILE: Raspi_MotorHAT.py

# PURPOSE:  provide Learn Robotics Programming interface to GoPiGo3 robot

from easygopigo3 import EasyGoPiGo3
from gopigo3 import GoPiGo3
import time

class Raspi_DCMotor():
    def __init__(self, controller, num):
        self.egpg = controller
        self.motornum = num
        self.motor = None

        if (num == 0):
            self.motor = GoPiGo3.MOTOR_LEFT
        elif (num == 1):
            self.motor = GoPiGo3.MOTOR_RIGHT
        else:
            self.motor = None

    def run(self, command):
        if (command == Raspi_MotorHAT.FORWARD):
            self.egpg.set_motor_dps(self.motor, self.egpg.DEFAULT_SPEED)
        elif (command == Raspi_MotorHAT.BACKWARD):
            self.egpg.set_motor_dps(self.motor, -self.egpg.DEFAULT_SPEED)
        elif (command == Raspi_MotorHAT.RELEASE):
            self.egpg.set_motor_dps(self.motor, 0)

    def setSpeed(self, speed):
        if (speed < 0):
            speed = 0
        elif (speed > 255):
            speed = 255
        self.egpg.set_motor_limits(self.motor, dps=speed*2)


class Raspi_MotorHAT():
    FORWARD = 1
    BACKWARD = 2
    BRAKE = 3
    RELEASE = 4

    SINGLE = 1
    DOUBLE = 2
    INTERLEAVE = 3
    MICROSTEP = 4

    egpg = None

    def __init__(self, addr=0x6f):
        self.egpg = EasyGoPiGo3(use_mutex=True)
        self.motors = [ Raspi_DCMotor(self.egpg, m) for m in range(4) ]

    def getMotor(self,num):
        return self.motors[num-1]
