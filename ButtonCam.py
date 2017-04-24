from time import sleep
from picamera import PiCamera
from gpiozero import Button

camera = PiCamera()
button = Button(2)
button2 = Button(4)

camera.start_preview(fullscreen = False, window = (100, 20, 640, 480))

buttoncam = 1

while True:
       button.wait_for_press()
       print ("I have been pushed.")
##       camera.start_preview()
##       sleep(2)
       camera.capture('/home/pi/git_repos/doris/Doris Photos/buttoncam%03d.jpg' % buttoncam)
       buttoncam +=1
##       sleep(3)
##       camera.stop_preview()
       button2.wait_for_press()
       camera.stop_preview()
       
