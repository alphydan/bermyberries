from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
import time

o = (255, 173, 65)
b = (102,215,255)
e = (0,0,0)

current_lightning_number = str(123)

#I think yulia puts the counter here
sense.show_message(current_lightning_number)

#the list of screens which make the animation
lg1 = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ]

lg2 = [
    e, e, e, e, e, b, e, e,
    e, e, e, e, b, e, e, e,
    e, e, e, b, e, e, e, e,
    e, e, b, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ]

lg3 = [
    e, e, e, e, e, b, b, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, b, e, e, e, e,
    e, e, e, b, e, e, e, e,
    e, e, e, e, b, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ]

lg4 = [
    e, e, e, e, e, b, b, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, b, e, e, e, e,
    e, e, e, b, b, e, e, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, e, e, e, e,
    e, e, b, e, e, e, e, e,
    ]

lg5 = [
    e, e, e, e, e, b, b, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, b, e, e, e, e,
    e, e, e, b, b, e, e, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, b, e, e, e, e,
    ]

lg6 = [
    e, e, e, e, e, b, b, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, b, e, e, e, e,
    e, e, e, b, b, e, e, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    o, o, b, b, o, o, o, o,
    ]

lg7 = [
    e, e, e, e, e, b, b, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, b, e, e, e, e,
    e, e, e, b, b, e, e, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    o, o, o, o, o, o, o, o,
    ]

lg8 = [
    e, e, e, e, e, b, b, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, b, e, e, e, e,
    e, e, e, b, b, e, e, e,
    e, e, e, e, b, b, e, e,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ]

lg9 = [
    e, e, e, e, e, b, b, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, b, e, e, e, e,
    e, e, e, b, b, e, e, e,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ]

lg10 = [
    e, e, e, e, e, b, b, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    e, e, b, b, e, e, e, e,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ]

lg11 = [
    e, e, e, e, e, b, b, e,
    e, e, e, e, b, b, e, e,
    e, e, e, b, b, e, e, e,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    ]

lg12 = [
    e, e, e, e, e, b, b, e,
    e, e, e, e, b, b, e, e,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e,
    ]

lg13 = [
    e, e, e, e, e, b, b, e,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ]

lg14 = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ]

lg15 = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ]

lg16 = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ]


lg17 = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ]

lg18 = [
    o, o, o, o, o, o, o, o,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ]

lg19 = [
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    e, e, e, e, e, e, e, e,
    ]

#code to run the animation
sense.set_pixels(lg1)
time.sleep(0.1)
sense.set_pixels(lg2)
time.sleep(0.1)
sense.set_pixels(lg3)
time.sleep(0.1)
sense.set_pixels(lg4)
time.sleep(0.1)
sense.set_pixels(lg5)
time.sleep(0.1)
sense.set_pixels(lg1)
time.sleep(0.1)
sense.set_pixels(lg5)
time.sleep(0.1)
sense.set_pixels(lg1)
time.sleep(0.1)
sense.set_pixels(lg5)
time.sleep(0.15)

# orange starts sliding up
sense.set_pixels(lg6)
time.sleep(0.1)
sense.set_pixels(lg7)
time.sleep(0.15)
sense.set_pixels(lg8)
time.sleep(0.15)
sense.set_pixels(lg9)
time.sleep(0.2)
sense.set_pixels(lg10)
time.sleep(0.2)
sense.set_pixels(lg11)
time.sleep(0.2)
sense.set_pixels(lg12)
time.sleep(0.2)
sense.set_pixels(lg13)
time.sleep(0.2)
sense.set_pixels(lg14)
time.sleep(0.2)
sense.set_pixels(lg15)
time.sleep(0.2)
sense.set_pixels(lg16)
time.sleep(0.2)
sense.set_pixels(lg17)
time.sleep(0.2)
sense.set_pixels(lg18)
time.sleep(0.2)
sense.set_pixels(lg19)
time.sleep(0.2)
sense.set_pixels(lg1)
time.sleep(0.2)

#the counter number increases​
