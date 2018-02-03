from picamera import PiCamera
from time import sleep
from time import time
import datetime as dt
import cv2

camera = PiCamera()
camera.resolution= (640, 480)
                         
#take 10 pictures
t0 = time()
for i in range(10):
    str_time = dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S.%f")
    myimage = camera.capture(str_time + i +'.jpg')
    #print('image' + str_time)
    sleep(0.1)
t_total = time()
print(t_total - t0)
print(camera.resolution)



print('finished')



'''
similar we are going to do the reverse
we are seeing the earth and keep all the bright spots
'''
