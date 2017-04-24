from gpiozero import MotionSensor
from time import sleep
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()


while True:
    #pir.wait_for_motion()
    if pir.motion_detected:
        print("motion")
    #camera.start_preview()
    #pir.wait_for_no_motion()
    else:
        print("no motion")
    #camera.stop_preview()
    

