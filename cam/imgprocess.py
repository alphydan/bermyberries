from picamera import PiCamera
import cv2
import numpy as np

# camera = PiCamera()
# str_time = dt.datetime.now().strftime("%Y_%m_%d-%H_%M_%S")

# camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
# sleep(2)

# # take a picture with the camera
# myimage = camera.capture(str_time + '.jpg')
# # myimage=camera.capture("physics"+ '.jpg')
# camera.stop_preview()
# img=cv2.imread("physics.jpg")
# img=cv2.imread(str_time + '.jpg')

# img[img < 220] = 0
# cv2.imwrite("editedimg5.jpg",img)

def brightness_score(someimage):
    '''
    Calculates a brightness score for the picture
    '''
    # Open image with Computer Vision library
    img = cv2.imread(someimage)
    # reset all pixels which were a bit dark to zero
    img[img < 200] = 0
    high_contrast_name = someimage.split('.')[0]+'_HC'+'.jpg'
    cv2.imwrite(high_contrast_name, img)

    # once all dark pixels are zero,
    # how many bright ones are left?
    # numpy has fast functions to do that
    nr_nonzero = np.count_nonzero(img)
    print('nr-non-zero ', nr_nonzero)
    print('Brightness calculator running')
    print('...')
    return nr_nonzero

'''
similar we are going to do the reverse
we are seeing the earth and keep all the bright spots
'''

def find_lightning_positions(high_contrast_photo):
    '''
    takes a pre-processed image which has been converted
    to high contrast and tries to find brigh spots inside of it
    ''' 
