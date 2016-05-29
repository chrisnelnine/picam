#!/usr/bin/python
# Camera Preview for given length of time in seconds
# takes one argument and previews cam for that number of seconds
# e.g. previewT.py 5 keeps preview on for 5 seconds



import time
import picamera
import sys

import grovepi
from grovepi import *

sleepTime = float(sys.argv[1])	#sys.argv[1] is the first and only argument

# Connect the Grove Ultrasonic Ranger to digital port D3
# SIG,NC,VCC,GND
ultrasonic_ranger = 3

with picamera.PiCamera() as camera:
    camera.hflip = True
    camera.vflip = False    
    camera.start_preview()
    while True:
	try:
                
                # Get distance value
                distance = grovepi.ultrasonicRead(ultrasonic_ranger)
                L = str(distance)
                
                camera.annotate_text = L
                camera.preview.alpha = 230
    time.sleep(sleepTime)
    camera.stop_preview()
