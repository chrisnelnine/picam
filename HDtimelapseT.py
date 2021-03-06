#!/usr/bin/python
#python HDtimelapseT.py TimeInSec FileName

import sys
import time
import picamera
import os


pauseTime = int(sys.argv[1]) #Time between captures in seconds
# fileName = str(sys.argv[2])

#dateStamp= time.strftime("%Y%m%d")
#hourStamp = time.strftime("%H")
dateHourStamp = str(time.strftime("%Y%m%d")) + "_" + str(time.strftime("%H")) + "h"
hourMinSecStamp = time.strftime("%H%M%S")


directory = './TLpics/' + str(dateHourStamp)

if not os.path.exists(directory):
    os.makedirs(directory)

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.preview.alpha = 230
    camera.resolution = (1024, 768)
    camera.hflip = True
    camera.vflip = False
    time.sleep(2)
    for filename in camera.capture_continuous('./TLpics/' + str(dateHourStamp) + "/" + str(hourMinSecStamp) + '_{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(pauseTime) # wait pauseTime seconds
