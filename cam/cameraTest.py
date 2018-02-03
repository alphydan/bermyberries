from picamera import PiCamera
from time import sleep
import datetime as dt
import cv2

camera = PiCamera()

str_time = dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
sleep(2)

# take a picture with the camera
myimage = camera.capture(str_time + '.jpg')
# myimage=camera.capture("physics"+ '.jpg')
camera.stop_preview()
img=cv2.imread("physics.jpg")
img=cv2.imread(str_time + '.jpg')

img[img < 220] = 0
cv2.imwrite("editedimg5.jpg",img)

'''
similar we are going to do the reverse
we are seeing the earth and keep all the bright spots
'''
