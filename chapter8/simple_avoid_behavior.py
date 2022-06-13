#!/usr/bin/env python3

from robot import Robot
from time import sleep

class ObstacleAvoidingBehavior:
    """Simple obstacle avoiding"""
    def __init__(self, the_robot):
        self.robot = the_robot
        self.speed = 20

    def get_motor_speed(self, distance):
        """This method chooses a speed for a motor based on the distance from a sensor"""
        if distance < 0.2:
            print("Obstacle Detected")
            return -self.speed
        else:
            return self.speed

    def run(self):
        while True:
            # Get the sensor readings in meters
            left_distance = self.robot.left_distance_sensor.distance
            right_distance = self.robot.right_distance_sensor.distance
            print("Left: {:.2f}, Right: {:.2f}".format(left_distance, right_distance))
            # and drive
            left_speed = self.get_motor_speed(left_distance)
            self.robot.set_right(left_speed)
            right_speed = self.get_motor_speed(right_distance)
            self.robot.set_left(right_speed)
             # Wait a little
            sleep(0.05)

bot = Robot()
behavior = ObstacleAvoidingBehavior(bot)
try:
    behavior.run()
except KeyboardInterrupt:
    print("\nCtrl-c .. Exiting")

