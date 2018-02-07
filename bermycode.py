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
x = 120

# Number of lightnings so far
n_li = 0

# Brightness Threshold
# percentage of pixels above 180 threshold
bri_thresh = 5 

# Start camera for the whole experiment
camera = PiCamera()
camera.resolution = (640, 480)

# low lighting mode
camera.iso = 1200
# camera.exposure_mode = 'night'
time.sleep(2) # let sensor settle

# Counters for non-events
count_too_bright = 0
count_no_light = 0

############################
# Hi there astronauts!
# anim.display_greeting() <-- UNCOMMENT LATER

#############################################
# Main loop
# looks at Bx,By,Bz and picture approx. every second



for i in range(x):
    print('ITERATION ',i, 'lightning so far:', n_li,'\n\n')
    # define timestamp for this loop
    right_now = dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S_%f")

    mag.save_magnet_data(right_now) # <-- WORKS!

    # capture image for current loop
    path_to_img = os.path.join(os.getcwd(),'cam/tmp/')
    image_name = path_to_img + right_now + '-' + str(i) + '.jpg'
    myimage = camera.capture(image_name)
    # check if it's too bright in daylight
    bri_s = ipro.brightness_score(image_name, debug=True)

    if bri_s > bri_thresh:
        # if the image is too bright, delete it.
        count_too_bright +=1
        os.remove(image_name)
        if i%120 == 0:
            # message to astronauts
            # every 120 loops (~2 min)
            anim.display_too_bright()
        print("that image was too bright")
        print("IMAGE DELETED")
    elif bri_s <= bri_thresh:
        # high_contrast = ipro.high_contrast_image(myimage)
        # <- DR FEITO WORKING on this
        print("it's a dark picture! hurray!")


        # Find positions of bright spots and save
        # image with their locations as yellow boxes
        bright_blobs, box_img_name = ipro.find_lightning_positions(image_name)


        
        if len(bright_blobs) > 0:
            # did it find at least one
            print('We have blobs')
            if len(bright_blobs) > 40:
                print('we have too many blobs')
                # likely too bright and crowded
                # Delete original and one with boxes
                os.remove(image_name)
                os.remove(box_img_name)
            elif len(bright_blobs) == 0:
                count_no_light += 1
                os.remove(image_name)
                print('Dark but no blobs')
                # no need to remove box image as
                # as it was not created.
                if count_no_light%100 ==0:
                    # a multiple of 100 times
                    # where we observed no lightning
                    anim.display_no_lightning()
            else: # A GOOD IMAGE AT LAST!! :)
                # do we have 2 previous ones?
                # yes -> compare
                # no -> wait
                print( 'Nr. of blobs --->', len(bright_blobs) )
                print('The blobs:', bright_blobs)
                anim.display_animation(n_li) # <<---- ENABLE LATER
                # Show the number of lightnings & a lightning animation on the display






