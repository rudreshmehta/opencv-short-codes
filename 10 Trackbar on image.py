"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM) How to Bind Trackbar To OpenCV Windows
"""
import numpy as np
import cv2 as c

def nothing(x):
    print(x)#to know the current value
def fonti(x):
    print(x)#to know current font size

c.namedWindow('image')

c.createTrackbar('CP', 'image', 10, 100, nothing)
c.createTrackbar('font_size', 'image', 1, 5, nothing)
switch = 'color/gray'
c.createTrackbar(switch,'image',0,1,nothing)
#toggle to convert to gray

while(1):
    img = c.imread('lena.jpg')
    pos = c.getTrackbarPos('CP', 'image')
    font = c.FONT_HERSHEY_PLAIN
    i = c.getTrackbarPos('font_size', 'image')
    c.putText(img,str(pos),(50,150),font,i,(255,255,255))
    
    k = c.waitKey(1) & 0xFF
    if k == 27: #only esc to exit this loop
        break
    s = c.getTrackbarPos(switch, 'image')
    
   
    
    if s == 0:
        pass
    else:
        img = c.cvtColor(img, c.COLOR_BGR2GRAY)
    c.imshow('image',img)
c.destroyAllWindows()