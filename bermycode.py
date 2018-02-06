import time
import os # to name files and directories

import datetime as dt
from picamera import PiCamera

from display import animation as anim
from cam import imgprocess as ipro
from magneto import magnetcode as mag

'''
This file brings together all the elements of our experiment:

(1) Save magnetic data [(magnetic field, time)]
(2) Detect lightnings
(3) Store data about lightnings [(position, time), ...]
(4) Display information for astronauts

'''

###########################
# Parameters & Definitions

# How many seconds does the experiment last?
x = 100

# Number of lightnings so far
n_li = 0

# Brightness Threshold
# percent of bright pixels with 180 threshold
bri_thresh = 30  

# Start camera for the whole experiment
camera = PiCamera()
camera.resolution = (640, 480)

# low lighting mode
camera.iso = 1200
camera.exposure_mode = 'night'
time.sleep(2) # let sensor settle
                 


############################
# Hi there astronauts!
# anim.display_greeting() <-- UNCOMMENT LATER

#############################################
# Main loop
# looks at Bx,By,Bz and picture approx. every second


for i in range(x):
    # define timestamp for this loop
    right_now = dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S_%f")

    mag.save_magnet_data(right_now) # <-- WORKS!

    # capture image for current loop
    path_to_img = os.path.join(os.getcwd(),'cam/tmp/')
    image_name = path_to_img + right_now + '-' + str(i) + '.jpg'
    myimage = camera.capture(image_name)
    high_contrast_name = image_name.split('.')[0]+'_HC'+'.jpg'
    # check if it's too bright in daylight
    bri_s = ipro.brightness_score(image_name)

    if bri_s > bri_thresh:
        # os.remove(image_name)
        # os.remove(high_contrast_name)
        print("that image was too bright")
        print("IMAGE DELETED")
    elif bri_s <= bri_thresh:
        # high_contrast = ipro.high_contrast_image(myimage)
        # <- DR FEITO WORKING on this
        print("it's a dark picture! hurray!")

        # MILA working on this -->
        # ipro.find_lightning_positions(high_contrast)


        ## MORE STUFF GOES HERE


        # Show the number of lightnings & a lightning animation on the display
        anim.display_animation(n_li)






