import time
import picamera
from sense_hat import AstroPi
from PIL import Image
import os

camera = picamera.PiCamera()

# Function to check if image taken is mostly white, returns true if mostly white
def checkWhite(directory):
    im = Image.open(directory)
    # Splits image into pixels
    pixels = im.getdata()
    # RGB threshold at which pixel is defined as 'white'
    whiteThresh = 660
    # Number of white pixels in image
    nwhite = 0
    # Cycles through pixels, counting number of 'white' pixels
    for pixel in pixels:
   
        if sum(pixel) > whiteThresh:
            nwhite +=1
        
    n = len(pixels)
    # If more than 20% is white, discard image
    if (nwhite / float(n)) > 0.20:
        return True
    else:
        return False


def captureImage(camera):
    # Directory to save image - adds timestamp to end of image name
    timeStamp = time.strftime("%d-%m-%Y_%H:%M:%S")
    # Directory to save image to
    directory = ('raw/img_%s.jpg' % timeStamp)
    # Captures and saves image in raw directory
    camera.capture(directory)
    # Checks whether image is mostly black
    if checkWhite(directory):
        # Delete mostly black photo
        os.remove(directory)
        print('Mostly White')
    else:
        print('not white')


captureImage(camera)



