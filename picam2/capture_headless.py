#!//usr/bin/python3

# FILE:  capture_headless.py

"""
OUTPUT:  

config: {'use_case': 'still',  
'transform': <libcamera._libcamera.Transform object at 0xb386c880>,  
'colour_space': <libcamera._libcamera.ColorSpace object at 0xb386c400>,  
'buffer_count': 1,  
'main': {'format': 'BGR888', 'size': (320, 240)},  
'lores': None, 'raw': None,  
'controls': {'NoiseReductionMode': <NoiseReductionMode.HighQuality: 2>, 'FrameDurationLimits': (1000,)},  
'display': None, 'encode': None}  

config["transform"].hflip True  
config["transform"].vflip True  
"""

from picamera2 import Picamera2
import libcamera

picam2 = Picamera2()

# configure only one parameter when creating config
# config = picam2.still_configuration(transform=libcamera.Transform(hflip=1, vflip=1))
# config = picam2.still_configuration(main={"size": (320, 240)})

# configure multiple parameters when creating config
config = picam2.still_configuration( \
                    main={"size": (320, 240)}, \
                    transform=libcamera.Transform(hflip=1, vflip=1) \
                    )

# configure parameters after creating config
# config = picam2.still_configuration()
# config["transform"] = libcamera.Transform(hflip=1, vflip=1)
# config["main"]["size"] = (320, 240)

# print them to be sure method result is same
print("config:",config)

# transform is a libcamera class object, not a json string
print('config["transform"].hflip', config["transform"].hflip)
print('config["transform"].vflip', config["transform"].vflip)

picam2.configure(config)

picam2.start()

np_array = picam2.capture_array()
print(np_array)
picam2.capture_file("demo.jpg")
picam2.stop()
