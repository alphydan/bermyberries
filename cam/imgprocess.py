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
    # Open image for processing (option zero makes it black and white)
    gray = cv2.imread(high_contrast_photo,0)
    # delte any small values, keeping only bright spots
    gray[gray < 100] = 0

    cv2.imwrite('testing_testing.jpg', gray)

    # from http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html
    # buff = np.fromstring(img, dtype=np.uint8)
    # image = cv2.imdecode(buff, 1)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 177, 255, 0)
    # cnts = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    contours = cv2.findContours(thresh, 1,2) # cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    cnt = contours[0] 
    M = cv2.moments(cnt)  # Moment = distance x weight

    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    
    print('contours, ----> ', contours)
    
    
    all_bright_spots = np.transpose(np.nonzero(gray)) 
    first_row = ''

    # print(all_bright_spots)

    # for x in gray[6]:
    #     first_row += str(x)+'.'
    # print(first_row)
    # print(first_row)
    # print(len(img[0]), len(img))
    # # print('all->', all_bright_spots)
    # for x in all_bright_spots:
    #     print(x)


    
find_lightning_positions('city_3_HC.jpg')
