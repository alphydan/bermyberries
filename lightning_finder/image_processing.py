
import matplotlib.pyplot as plt
import cv2, matplotlib
import numpy as np

img = cv2.imread('EnviroPi_20160223_110953.jpg')

#convert image to grayscale
gray_imh = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#show image with plotlib
plt.imshow(img)
