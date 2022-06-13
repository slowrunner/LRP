import vpython as vp
import time
from robot_imu import RobotImu

imu = RobotImu()

vp.graph(xmin=0, xmax=60, scroll=True)
graph_x = vp.gcurve(color=vp.color.red)
graph_y = vp.gcurve(color=vp.color.green)
graph_z = vp.gcurve(color=vp.color.blue)

start = time.time()
while True:
    vp.rate(100)
    elapsed = time.time() - start
    accel = imu.read_accelerometer()
    graph_x.plot(elapsed, accel.x)
    graph_y.plot(elapsed, accel.y)
    graph_z.plot(elapsed, accel.z)
