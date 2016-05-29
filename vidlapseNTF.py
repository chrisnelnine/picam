#!/usr/bin/python
#python HDvidlapseNTF.py NumberOfClips TimePerVidInSec FileName

import sys
import time
import picamera

numberOfClips = int(sys.argv[1])
clipDuration = int(sys.argv[2]) #in seconds
fileName = str(sys.argv[3])

import picamera
with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.hflip = True
    camera.vflip = False
    for filename in camera.record_sequence("./vids/" + str(fileName) +
            '%02d.h264' % i for i in range(numberOfClips)):
        print('Recording to %s' % filename)
        camera.wait_recording(clipDuration)
