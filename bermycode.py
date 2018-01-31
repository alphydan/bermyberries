import time
from display import animation as anim

'''
This file brings together all the elements of our experiment:

(1) Detect lightnings
(2) Store data about lightnings [(position, time), ...]
(3) Save magnetic data [(magnetic field, time)]

'''
display_greeting()

if brightness > 50:
    display_too_bright()

# Show the number of lightnings & a lightning animation on the display
anim.display_animation(1063)

#
