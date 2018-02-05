from picamera import PiCamera
import cv2
import numpy as np

def brightness_score(someimage):
    '''
    Calculates a brightness score for the picture
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
    how_many_pixels = float(1920*931) # 
    print('bright %', round(nr_nonzero/how_many_pixels*100,1))
    print('Brightness calculator running')
    print('...')
    return nr_nonzero


brightness_score('city_4.jpeg')

'''
similar we are going to do the reverse
we are seeing the earth and keep all the bright spots
'''

def find_lightning_positions(high_contrast_photo):
    '''
    takes a pre-processed image which has been converted
    to high contrast and tries to find brigh spots inside of it
    '''
    img = cv2.imread(high_contrast_photo)
    all_bright_spots = np.nonzero(img)[0] # the return is a little funny so I use the [0]
    for x in all_bright_spots:
        print(x)


    
find_lightning_positions('city_4_HC.jpg')
