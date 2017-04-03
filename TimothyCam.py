from picamera import PiCamera
from time import sleep


camera = PiCamera()

x=1
while x<6:
    x+=1
    camera.start_preview()
    sleep(10)
    camera.capture('/home/pi/Documents/teacher/Doris/timothycam%s.jpg' % x)
    camera.stop_preview()

 
