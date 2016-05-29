#!/usr/bin/python
#HDvidlapseNTF.py takes three arguments NumberOfClips(N) TimePerVidInSec(T) FileName(F)
#Records N video clips with resolution 1024 X 768, each of T seconds length with filename HD"F"000.h264, HD"F"001.h264 etc 
#clips are found in the folderName folder

import sys
import time
import picamera

folderName = "/media/pi/WHITE/HD"
numberOfClips = int(sys.argv[1])
clipDuration = int(sys.argv[2]) #in seconds
fileName = str(sys.argv[3])

import picamera
with picamera.PiCamera() as camera:
    camera.start_preview()
    camera.preview.alpha = 230
    camera.resolution = (1024, 768)
    camera.hflip = True
    camera.vflip = False
    for filename in camera.record_sequence(folderName + str(fileName) +
            '%02d.h264' % i for i in range(numberOfClips)):
        print('Recording to %s' % filename)
        camera.wait_recording(clipDuration)
