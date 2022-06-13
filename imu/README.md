# Using GoPiGo3 IMU for Orion Robot's Learn Robotics Programming

sudo pip3 install imu4gopigo3ros

Test:

* startIMU
* readIMU
* resetIMU
* calibrateIMU
* startIMU -i
* python3  

  >>>import ros_safe_inertial_measurement_unit as imupkg  
  
  >>>imu=imupkg.SafeIMUSensor()  
  
  >>>imu.readAndPrint()  
  
  ctrl-c  
  
  ctrl-d  


# installing Visual Python (VPython) 
$ pip3 install git+https://github.com/orionrobots/vpython-jupyter.git

* Run plot_temperature.py:
```
VPYTHON_PORT=9020 VPYTHON_NOBROWSER=true python3 plot_temperature.py
```
and point browser to LRP.local:9020 to see the temperature plotted

add to .bashrc
```
$ echo 'alias vpython="VPYTHON_PORT=9020 VPYTHON_NOBROWSER=true python3"' >>~/.bashrc
```
