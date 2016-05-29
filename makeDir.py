#!/usr/bin/python
#python HDtimelapseT.py TimeInSec FileName

import sys
import time
import picamera
import os


#pauseTime = int(sys.argv[1]) #Time between captures in seconds
# fileName = str(sys.argv[2])

#dateStamp= time.strftime("%Y%m%d")
#hourStamp = time.strftime("%H")
#hourMinSecStamp = time.strftime("%H%M%S")


#directory = '~/TLpics/' + str(dateStamp)

if not os.path.exists('/home/pi/new'):
    os.makedirs('/home/pi/new')

#with picamera.PiCamera() as camera:
   # camera.start_preview()
   # camera.resolution = (1024, 768)
   # camera.hflip = True
  #  camera.vflip = False
    #time.sleep(2)
    #for filename in camera.capture_continuous('~/TLpics/' + str(dateStamp) + "/" + str(hourMinSecStamp) + '{counter:03d}.jpg'):
      #  print('Captured %s' % filename)
       # time.sleep(pauseTime) # wait pauseTime seconds
