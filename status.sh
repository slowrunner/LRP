#!/bin/bash
#
# loop printing out processor temp, processor clock freq, and throttled status
#
# 0x50000  means throttling occurred, under-voltage occurred
# 0x50005  means throttled now and under-voltage now
# 0x80008  means soft temperature limit exceeded (no throttling yet)
#
while true; do uptime && vcgencmd measure_temp && vcgencmd measure_clock arm && vcgencmd get_throttled; free -t -m; /home/pi/LRP/plib/battery.py; sleep 2; echo ''; done
