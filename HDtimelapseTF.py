#!/usr/bin/python
#python HDtimelapseTF.py TimeInSec FileName

import sys
import time
import picamera

pauseTime = int(sys.argv[1])
fileName = str(sys.argv[2])

with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.resolution = (1024, 768)
    camera.hflip = True
    camera.vflip = False
    time.sleep(2)
    for filename in camera.capture_continuous("./pics/HD" + str(fileName) + '{counter:03d}.jpg'):
        print('Captured %s' % filename)
        time.sleep(pauseTime) # wait pauseTime seconds
