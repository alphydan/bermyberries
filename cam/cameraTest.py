from picamera import PiCamera
from time import sleep
import datetime as dt

camera = PiCamera()

str_time = dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
sleep(30)

camera.capture(str_time + '.jpg')
camera.stop_preview()
