#!/usr/bin/env python
# python HDrecordTF.py TIME FILENAME


import sys
import time
import picamera


recTime = float(sys.argv[1])	
fileName = str(sys.argv[2])
fileName = "./vids/" + str(fileName) + ".h264"

with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    camera.hflip = True
    camera.vflip = False
    camera.start_preview()
    camera.start_recording(fileName)
    camera.wait_recording(recTime)
    camera.stop_recording()
    camera.stop_preview()
