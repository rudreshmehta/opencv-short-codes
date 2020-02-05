"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM) Basic function
"""
import cv2
import numpy as n

img = cv2.imread('lena.jpg')
img2 = cv2.imread('opencv-logo.png')
print(img.shape)#row,column,channel
print(img.size)#pixwl total access
print(img.dtype)#image datatype obtain
b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))
print(b.shape)#only one channel
piece = img[280:340, 330:390]
img[273:333, 100:160] = piece

img = cv2.resize(img, (512,512))
img2 = cv2.resize(img2, (512,512))

#img11 = cv2.add(img, img2)

img11 = cv2.addWeighted(img,0.9,img2,.9,0)#both . value + = 1 here 0.9+0.9 = 1.8 so not right

cv2.imshow('image',img11)#image in function = here
cv2.waitKey(0)
cv2.destroyAllWindows()