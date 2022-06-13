#!//usr/bin/python3

from picamera2 import Picamera2
import libcamera

picam2 = Picamera2()
config = picam2.still_configuration(transform=libcamera.Transform(hflip=1, vflip=1))
picam2.configure(config)

picam2.start()

np_array = picam2.capture_array()
print(np_array)
picam2.capture_file("demo.jpg")
picam2.stop()
