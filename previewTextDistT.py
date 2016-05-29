#!/usr/bin/python
# Camera Preview for given length of time in seconds
# takes one argument and previews cam for that number of seconds
# e.g. previewTextDistT.py 5 keeps preview on for 5 seconds
# Preview has a text label top centre indicating distance of object from camera



import time
import picamera
import sys

import grovepi
from grovepi import *


# Connect two Grove Ultrasonic Rangers to digital ports D3 and D2
# SIG,NC,VCC,GND
ultrasonic_ranger1 = 3 # Ultrasonic Ranger at D3
ultrasonic_ranger2 = 2 # Ultrasonic Ranger at D2

sleepTime = int(sys.argv[1])	#sys.argv[1] is the first and only argument

t_end = time.time() + sleepTime

with picamera.PiCamera() as camera:
        camera.hflip = True
        camera.vflip = True
        camera.start_preview()
        camera.preview.alpha = 230

        while time.time() < t_end:

                try:
                    # Get distance value
                    distance1 = grovepi.ultrasonicRead(ultrasonic_ranger1)
                    distance2 = grovepi.ultrasonicRead(ultrasonic_ranger2)
                    R = min(distance1, distance2)
                    R = str(R)
                    camera.annotate_text = R
                    time.sleep(.5)
                    
                except (IOError,TypeError) as e:
                            print "Error"
                    
        camera.stop_preview()
