"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM) Color Palette by open cv
"""
import numpy as np
import cv2 as c

def nothing(x):
    print(x)#to know the current value

img = np.zeros((300,512,3), np.uint8)
c.namedWindow('color palette')

switch = '0 : OFF\n 1: ON'
c.createTrackbar(switch,'color palette',0,1,nothing)
#switch on to use it

c.createTrackbar('B','color palette', 0, 255, nothing)#trackbar in image window
c.createTrackbar('G','color palette', 0, 255, nothing)
c.createTrackbar('R','color palette', 0, 255, nothing)



while(1):
    c.imshow('color palette', img)
    k = c.waitKey(1) & 0xFF
    if k == 27: #only esc to exit this loop
        break
    b = c.getTrackbarPos('B','color palette')
    g = c.getTrackbarPos('G','color palette')
    r = c.getTrackbarPos('R','color palette')
    s = c.getTrackbarPos(switch,'color palette')   
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
c.destroyAllWindows()