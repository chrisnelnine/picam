#!/usr/bin/python
# Camera Preview for given length of time in seconds
# takes one argument and previews cam for that number of seconds
# e.g. previewN.py 5 keeps preview on for 5 seconds



import time
import picamera
import sys

sleepTime = float(sys.argv[1])	#sys.argv[1] is the first and only argument

with picamera.PiCamera() as camera:
    camera.hflip = True
    camera.vflip = False    
    camera.start_preview()
    camera.preview.alpha = 230
    time.sleep(sleepTime)
    camera.stop_preview()
