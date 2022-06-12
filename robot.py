#!/usr/bin/env python3

from Raspi_MotorHAT import Raspi_MotorHAT
import atexit
from easygopigo3 import EasyGoPiGo3

class LeftDistanceSensor():
    def __init__(self, ds):
        self.ds = ds
        self.pan = -30

    def distance(self):
        # pan left
        return self.ds.read_mm()

class RightDistanceSensor():
    def __init__(self, ds):
        self.ds = ds
        self.pan = 30

    def distance(self):
        # pan left
        return self.ds.read_mm()


class Robot:
    def __init__(self, motorhat_addr=0x6f):
        # Setup the motorhat with the passed in address
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        # get local variable for each motor
        self.left_motor = self._mh.getMotor(1)
        self.right_motor  = self._mh.getMotor(2)

        self.distance_sensor = self._mh.egpg.init_distance_sensor()
        # print("distance: ", self.distance_sensor.read_mm())
        self.left_distance_sensor = LeftDistanceSensor(self.distance_sensor)
        self.right_distance_sensor = RightDistanceSensor(self.distance_sensor)
        print("l distance: ", self.left_distance_sensor.distance())
        print("r distance: ", self.right_distance_sensor.distance())

        # ensure the motors get stopped when the code exits
        atexit.register(self.stop_motors)

    def convert_speed(self, speed):
        # Choose the running mode
        mode = Raspi_MotorHAT.RELEASE
        if speed > 0:
            mode = Raspi_MotorHAT.FORWARD
        elif speed < 0:
            mode = Raspi_MotorHAT.BACKWARD
        # Scale the speed
        output_speed = (abs(speed) * 255) // 100
        return mode, int(output_speed)

    def set_left(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.left_motor.setSpeed(output_speed)
        self.left_motor.run(mode)

    def set_right(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.right_motor.setSpeed(output_speed)
        self.right_motor.run(mode)

    def stop_motors(self):
        self.left_motor.run(Raspi_MotorHAT.RELEASE)
        self.right_motor.run(Raspi_MotorHAT.RELEASE)

