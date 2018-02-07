import time
import os # to name files and directories
import csv

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

# How many seconds/loops does the experiment last?
x = 11000

# Number of lightnings so far
n_li = 0

# Brightness Threshold
# percentage of pixels above 180 threshold
bri_thresh = 10

# Start camera for the whole experiment
camera = PiCamera()
camera.resolution = (640, 480)

# low lighting mode
camera.iso = 1200
camera.exposure_mode = 'night'
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
    # define timestamp for this loop
    right_now = dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S_%f")

    # save magnet data and timestamp
    mag.save_magnet_data(right_now) 

    # capture image for current loop
    path_to_img = os.path.join(os.getcwd(),'cam/pics/')
    image_name = path_to_img + right_now + '-' + str(i) + '.jpg'
    myimage = camera.capture(image_name)
    # check if it's too bright (daylight)
    bri_s = ipro.brightness_score(image_name, debug=False)

    if bri_s > bri_thresh:
        # if the image is too bright, delete it.
        count_too_bright +=1
        os.remove(image_name)
        if i%200 == 0:
            # message to astronauts
            # every 200 loops (~3 min)
            anim.display_too_bright()
    elif bri_s <= bri_thresh:
        # it is a dark image
        # Find positions of bright spots and save
        # image with their locations as yellow boxes
        bright_blobs, box_img_name = \
        ipro.find_lightning_positions(image_name, i, right_now)
        # a small copy of the image has been saved
        # delete original
        os.remove(image_name)
        if len(bright_blobs) > 0:
            # did it find at least one?
            if len(bright_blobs) > 40:
                # too many blobs
                # likely too bright and crowded
                # Delete original and one with boxes
                os.remove(box_img_name)
            elif len(bright_blobs) == 0:
                count_no_light += 1
                # Dark but no blobs
                # no need to remove box image as
                # as it was not created.
                if count_no_light%100 ==0:
                    # a multiple of 100 times
                    # where we observed no lightning
                    anim.display_no_lightning()
            else: # A GOOD IMAGE AT LAST!! :)
                # do we have 2 previous ones?
                # yes -> compare (unfinished)
                # no -> wait (unfinished)
                # Update nr of lightnings (could overestimate)
                n_li += len(bright_blobs)
                # Keep astronauts updated now and again:
                # Show the number of lightnings & a lightning animation on the display
                if i > 100 and i < 200:
                    anim.display_animation(n_li)
                if i > 1000 and i < 1050:
                    anim.display_animation(n_li)
                if i > 2000 and i < 2050:
                    anim.display_animation(n_li)
                if i > 3000 and i < 3050:
                    anim.display_animation(n_li)
                if i > 5000 and i < 5050:
                    anim.display_animation(n_li)

    # save data mid-way in the experiment
    if i == 5000:
        mid_row = [count_too_bright, count_no_light, n_li]
        with open("lightning_data.csv","a") as lightningdata:
            writer = csv.writer(lightningdata)
            writer.writerow(mid_row)



last_row = [count_too_bright, count_no_light, n_li]
with open("lightning_data.csv","a") as lightningdata:
    writer = csv.writer(lightningdata)
    writer.writerow(last_row)
