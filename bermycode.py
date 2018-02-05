import time
import os # to name files and directories

import datetime as dt
from picamera import PiCamera

from display import animation as anim
from cam import imgprocess as ipro
from magneto import magnetcode as mag

'''
This file brings together all the elements of our experiment:

(1) Detect lightnings
(2) Store data about lightnings [(position, time), ...]
(3) Save magnetic data [(magnetic field, time)]

'''

###########################
# Parameters & Definitions

# How many seconds does the experiment las?
x = 10

# Number of lightnings so far
n_li = 0

# Brightness Threshold
bri_thresh = 40  # number is made up, come back here!!

# Start camera for the whole experiment
camera = PiCamera()
camera.resolution = (640, 480)


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
    print('magnetic data saved')

    # capture image for current loop
    path_to_img = os.path.join(os.getcwd(),'cam/tmp/')
    image_name = path_to_img + right_now + '-' + str(i) + '.jpg'
    myimage = camera.capture(image_name)

    # check if it's too bright in daylight
    briS = ipro.brightness_score(image_name) # <-- DR FEITO working on this

    if briS > bri_thresh:
        # delete image
        pass
    elif briS <= bri_thresh:
        # high_contrast = ipro.high_contrast_image(myimage)
        # <- DR FEITO WORKING on this
        pass

        # MILA working on this -->
        ipro.find_lightning_positions(high_contrast)


        ## MORE STUFF GOES HERE


        # Show the number of lightnings & a lightning animation on the display
        anim.display_animation(n_li)






