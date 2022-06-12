#!/usr/bin/env python3

from Raspi_MotorHAT import Raspi_MotorHAT
import atexit
from easygopigo3 import EasyGoPiGo3
import time

class LeftDistanceSensor():
    def __init__(self, ds, ps):
        self.ds = ds
        self.ps = ps
        self.angle = -30

    def distance(self):
        self.ps.pan(self.angle)
        time.sleep(.2)
        return self.ds.read()  # cm

class RightDistanceSensor():
    def __init__(self, ds, ps):
        self.ds = ds
        self.ps = ps
        self.angle = 30

    def distance(self):
        self.ps.pan(self.angle)
        time.sleep(.2)
        return self.ds.read()  # cm

class Pan_Servo():
    def __init__(self, egpg):
        self.egpg = egpg
        self.ps = self.egpg.init_servo("SERVO1")
        self.SERVO_CENTER = 82
        self.center()

    def center(self):
        self.ps.rotate_servo(self.SERVO_CENTER)
        time.sleep(0.2)

    def pan(self,angle):
        print("Pan_Servo.pan:",angle)
        self.ps.rotate_servo(self.SERVO_CENTER-angle)
        time.sleep(0.2)

    def off(self):
        try:
            self.ps.gpg.set_servo(self.ps.portID, 0)
        except Exception as e:
            print("Pan_Servo.off Exception:", str(e))

class Robot:
    def __init__(self, motorhat_addr=0x6f):
        # Setup the motorhat with the passed in address
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)
        self.egpg = self._mh.egpg
        # get local variable for each motor
        self.left_motor = self._mh.getMotor(1)
        self.right_motor  = self._mh.getMotor(2)

        self.distance_sensor = self._mh.egpg.init_distance_sensor()
        # print("distance: ", self.distance_sensor.read_mm())
        self.pan_servo = Pan_Servo(self.egpg)

        self.left_distance_sensor = LeftDistanceSensor(self.distance_sensor, self.pan_servo)
        self.right_distance_sensor = RightDistanceSensor(self.distance_sensor, self.pan_servo)
        # print("l distance: ", self.left_distance_sensor.distance())
        # print("r distance: ", self.right_distance_sensor.distance())

        # ensure the pan servo is not holding after exit
        atexit.register(self.pan_servo.off)

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

