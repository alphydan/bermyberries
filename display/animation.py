from sense_hat import SenseHat
sense = SenseHat()
sense.set_rotation(270)
import time

# sense.show_message(current_lg_n)

def display_animation(n_li):
    
    o = (255, 173, 65)
    b = (102,215,255)
    e = (0,0,0)

    current_lg_n = str(n_li)
    
    sense.show_message(current_lg_n)


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

    #lightning bolt flash
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

    #the counter number

#messages to astronauts
    
def display_greeting():
    
    sense.show_message("Hello we are the Berry Berries! Lets log some lighting!")

def display_too_bright():   
    
    sense.show_message("Oops! its too bright for us to see! We'll be back when we reach the dark side...")

def display_no_lightning():   
    
    sense.show_message("We havent seen any strikes for a while. Don't worry, we're still looking!")

    

