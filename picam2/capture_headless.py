#!//usr/bin/python3

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
