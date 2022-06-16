# Using libcamera-still instead of raspistill on PiOS Bullseye

Instead of:
```
$ raspistill -o test.jpg
```
use:
```
$ libcamera-still -o test.jpg
```

Useful options:
```
# if cable comes out the top of camera board
--rotation 180

# for low resolution
--width 320  --height 240
```


# Installing picamera2
1) Do not set  legacy Pi Camera in raspi-config
2) install python3-libcamera and more
```
sudo apt install -y python3-libcamera python3-kms++
sudo apt install -y python3-pyqt5 python3-prctl libatlas-base-dev ffmpeg
sudo pip3 install numpy --upgrade
sudo pip3 install picamera2
```

# Testing picamera2

```
capture_headless.py:  Capture a jpg image w/o preview (headless)
$ wget https://raw.githubusercontent.com/raspberrypi/picamera2/main/examples/capture_headless.py

$ python3 capture_headless.py
```
local copy: (updated to transform vflip and hflip, and reduce size.  Documented various ways to set and print config items. )

```
mjpeg_server.py:  Stream 640x480 video to browser at port 8000
$ wget https://raw.githubusercontent.com/raspberrypi/picamera2/main/examples/mjpeg_server.py
$ sudo pip3 install simplejpeg

$ python3 mjpeg_server.py
point browser to LRP.local:8000
```
local copy: (updated to transform vflip and hflip)


