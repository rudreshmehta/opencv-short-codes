"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM)  Bitwise Operators (bitwise_and, bitwise_or, bitwise_xor, bitwise_not) On Images
"""
import cv2
import numpy as np

img1 = np.zeros((500, 500, 3), np.uint8)
img1 = cv2.rectangle(img1,(200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("lena.jpg")
img2 = cv2.resize(img2,(500,500))
bitAnd = cv2.bitwise_and(img2, img1)
bitOr = cv2.bitwise_or(img2, img1)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.imshow('img11', img1)
cv2.imshow('img22', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()