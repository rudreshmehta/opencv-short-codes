"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM) Threshold on image in opencv,python
"""
import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg',0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)#in this type after threshold value pixel value will remain same
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)#when pixel value < threshold then pixel is 0
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

#threshold(img_object,threshold,max_value_for_the_threshold,threshold_type)

cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()