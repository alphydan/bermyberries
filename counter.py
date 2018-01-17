import datetime
import random

counter = 0 # counts how many lightnings
t0 = datetime.datetime.now() # when we start counting
# current time in increments of 10 s
tflash = t0 + datetime.timedelta(0,10) 

while (tflash-t0)< datetime.timedelta(0,10800):
    if random.uniform(0, 1) > 0.99:
        counter = counter + 1

    if tflash <= datetime.datetime.now():
        print('flash')
        print('count:', counter)
        tflash = datetime.datetime.now() + datetime.timedelta(0,10)
