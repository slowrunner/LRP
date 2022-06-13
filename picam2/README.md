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

