from picamera import PiCamera
import cv2 # computer vision library
from skimage import measure # scikit-image library
import numpy as np # matrices and large numbers library
import math


def brightness_score(someimage):
    '''
    Calculates a brightness score for the picture
    `input`:image name
    `output`: percentage of pixels which are bright
    '''
    # Open image with Computer Vision library
    img = cv2.imread(someimage,0)
    # reset all pixels which were a bit dark to zero
    img[img < 180] = 0
    high_contrast_name = someimage.split('.')[0]+'_HC'+'.jpg'
    cv2.imwrite(high_contrast_name, img)

    # once all dark pixels are zero,
    # how many bright ones are left?
    # numpy has fast functions to do that
    nr_nonzero = np.count_nonzero(img) #it counts the bright pixels
    # how_many_pixels = float(480*640) #
    how_many_pixels = float(img.shape[0]*img.shape[1]) # 
    print('bright %', round(nr_nonzero/how_many_pixels*100,1))
    print('Brightness calculator running')
    print('...')
    return nr_nonzero


# brightness_score('city_4.jpeg')


def find_lightning_positions(someimage, verbose = False):
    '''
    takes an image which is processed and converted into
    to high contrast and tries to find brigh spots inside of it
    `input`: the name of the file
    `output`: a list with the coordinates of the white spots which
              have been identified with Computer Vision.
    Mostly based on: 
    www.pyimagesearch.com/2016/10/31/detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/
    '''

    # Open image for processing (option zero makes it black and white)


    original = cv2.imread(someimage)        
    gray_pic = cv2.imread(someimage,0)
    # if the pixel is dim, make it zero (black)
    gray_pic[ gray_pic < 175 ] = 0
    # if the pixel is bright, make it 255 (white)
    gray_pic[ gray_pic >= 175 ] = 255

 
    # blur the spots, so we don't have single pixels or tiny spots
    blurred_pic = cv2.GaussianBlur(gray_pic,(5,5),0)

    # delte any small values, keeping only bright spots
    # pixels with values < 100 are made black (0)
    # pixels with values > 100 are made white (255)
    thresh_pic = cv2.threshold(blurred_pic, 100, 255, cv2.THRESH_BINARY)[1]

    # contours = cv2.findContours(thresh_pic, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours = cv2.findContours(thresh_pic, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    list_of_bright_spots = [] # we will store lightnings here
    for cnt in contours[1]:
        bx,by,bw,bh = cv2.boundingRect(cnt)
        if verbose:
            print(bx,by,bw,bh)
        list_of_bright_spots.append([bx+bw/2.0, by+bh/2.0, bw, bh])
        # (cx,cy),radius = cv2.minEnclosingCircle(cnt)
        # cv2.drawContours(original,[cnt],0,(0,255,0),1)   # draw contours in green color
        # cv2.circle(original,(int(cx),int(cy)),int(radius),(0,0,255),2)   # draw circle in red color
        if bw > 4 and bh > 4:
            margin = 3
            box_colour = (0,255,255)
            box_width = 2
            cv2.rectangle(original,(bx-margin,by-margin),
                          (bx+bw+margin,by+bh+margin),box_colour,1) # draw yellow rectangle 


    if verbose:
        print( list_of_bright_spots)
        cv2.imshow('output',original)
        cv2.waitKey(0)
    analysis_name = someimage.split('.')[0]+'WITH_BOX'+'.jpg'    
    cv2.imwrite(analysis_name, original)



brightness_score('physics.jpg')
find_lightning_positions('physics.jpg', verbose=True)


## RESOURCES
# https://www.learnopencv.com/blob-detection-using-opencv-python-c/
# https://www.pyimagesearch.com/2016/10/31/detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/
# https://docs.opencv.org/3.4.0/d9/d8b/tutorial_py_contours_hierarchy.html
# from http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html
