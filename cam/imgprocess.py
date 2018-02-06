from picamera import PiCamera
import cv2 # computer vision library
# from skimage import measure # scikit-image library
import numpy as np # matrices and large numbers library
import math


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


# brightness_score('city_4.jpeg')


def find_lightning_positions(high_contrast_image):
    '''
    takes a pre-processed image which has been converted
    to high contrast and tries to find brigh spots inside of it
    `input`: the name of the file
    `output`: a list with the coordinates of the white spots which
              have been identified with Computer Vision.
    '''
    # Open image for processing (option zero makes it black and white)
    original = cv2.imread(high_contrast_image)
    gray_pic = cv2.imread(high_contrast_image,0)

    # gray_pic[gray_pic < 180] = 0


    # blur the spots, so we don't have single pixels or tiny spots
    blurred_pic = cv2.GaussianBlur(gray_pic,(9,9),0)

    # delte any small values, keeping only bright spots
    # pixels with values < 120 are made black (0)
    # pixels with values > 120 are made white (255)
    thresh_pic = cv2.threshold(blurred_pic, 100, 250, cv2.THRESH_BINARY)[1]

    # Erosion and dilation washes out tiny spots
    threshstretch = cv2.erode(thresh_pic, None, iterations=2)
    threshstretch = cv2.dilate(threshstretch, None, iterations=4)



    # Simple detector for blobs.
    
    #1) set parameters
    # Change thresholds
    params = cv2.SimpleBlobDetector_Params()
    # colour parameters
    params.minThreshold = 10
    params.maxThreshold = 255

    # Filter by Area.
    params.filterByArea = False
    # params.minArea = 1500

    # define detector
    detector = cv2.SimpleBlobDetector_create(params)
    # detect the blobs
    keypoints = detector.detect(threshstretch)

    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    # im_with_keypoints = cv2.drawKeypoints(original, keypoints, np.array([]), (0,255,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    print(keypoints)
    for kp in keypoints:
            x, y = kp.pt
            print(x,y) # so far it's returning [], empty :(
            cv2.circle(original, (int(x), int(y)), 2, color)


    cv2.imshow("Keypoints", original)
    cv2.waitKey(0)
    # ret, markers = cv2.connectedComponents(threshstretch)
    # mask = np.zeros(threshstretch, dtype='uint8')
    # labels = measure.label(threshstretch, neighbors=8, background=0)
    # mask = np.zeros(thresh.shape, dtype="uint8")
    
    cv2.imwrite('testing_testing.jpg', thresh_pic)
    
    # diff_img = cv2.absdiff(blur1,blur2)
    # # diffblur = cv2.blur(diff_img,(2,2))


    # diff_img[diff_img < 180] = 0


    # ret, markers = cv2.connectedComponents(diff_img)
    # markers = markers+1

    # print(ret)
    # for x in markers:
    #     print(x)
    
    # from http://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_contours/py_contour_features/py_contour_features.html
    # buff = np.fromstring(img, dtype=np.uint8)
    # image = cv2.imdecode(buff, 1)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # ret, thresh = cv2.threshold(diff_img, 177, 0)
    contours = cv2.findContours(thresh_pic, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    # https://docs.opencv.org/3.4.0/d9/d8b/tutorial_py_contours_hierarchy.html

    # NEXT STEP: https://www.pyimagesearch.com/2016/10/31/detecting-multiple-bright-spots-in-an-image-with-python-and-opencv/
    
    cnt = contours[0]
    hierarchy = contours[1][0]

    # For each contour, find the bounding rectangle and draw it
    # for component in zip(cnt, hierarchy):
    #     currentContour = component[0]
    #     currentHierarchy = component[1]
    #     x,y,w,h = cv2.boundingRect(currentContour)
    #     print(currentContour, 'hier: ', currentHierarchy, x,y,w,h)
    #     cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),3)

    # for component in cnt:
    #     currentContour = component
    #     x,y,w,h = cv2.boundingRect(currentContour)
    #     print(currentContour, x,y,w,h)
    #     cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),3)

    
    M = cv2.moments(cnt)  # Moment = distance x weight
    area = M['m00'] # cv2.contourArea(cnt)

    
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    length = math.sqrt(area)

    # (x,y),radius = cv2.minEnclosingCircle(cnt)
    # center = (int(x),int(y))
    # radius = int(radius)
    # img = cv2.circle(img,center,radius,(0,255,0),2)
    
    # print('contours, ----> ', area)
    
    # # Finally show the image
    # cv2.rectangle(gray,(cx,cy),(cx+int(length),cy+int(length)),255,3)
    # cv2.imshow('img',gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    
    # all_bright_spots = np.transpose(np.nonzero(gray)) 
    # first_row = ''

    # print(all_bright_spots)

    # for x in gray[6]:
    #     first_row += str(x)+'.'
    # print(first_row)
    # print(first_row)
    # print(len(img[0]), len(img))
    # # print('all->', all_bright_spots)
    # for x in all_bright_spots:
    #     print(x)

def draw_keypoints(vis, keypoints, color = (0, 255, 255)):
    for kp in keypoints:
            x, y = kp.pt
            cv2.circle(vis, (int(x), int(y)), 2, color)
    
# find_lightning_positions('city_1_HC.jpg', 'city_2_HC.jpg')
find_lightning_positions('city_1_HC.jpg')
