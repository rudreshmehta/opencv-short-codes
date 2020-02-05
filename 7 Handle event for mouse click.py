"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM) Handle event for mouse key
"""
import cv2
import numpy as n
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
# to read all event incv2

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' ', y)
        font = cv2.FONT_HERSHEY_PLAIN
        s = 'x = ' + str(x) + '   ' + 'y = ' + str(y)
        cv2.putText(img,s,(x, y), font, 1, (255,255,255), 1)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]
        g= img[y, x, 1]
        r = img[y, x, 2]
        font = cv2.FONT_HERSHEY_PLAIN
        s = str(b) + ' ' + str(g) + ' ' + str(r)
        cv2.putText(img, s, (x, y), font, 1, (255,255,255), 1)
        cv2.imshow('image',img)
#img = n.zeros((512,512,3), n.uint8)
img = cv2.imread('X:\\rudresh\\AI\\openCv\\opencv-master\\opencv-master\\doc\\js_tutorials\\js_assets\\lena.jpg')
cv2.imshow('image',img)#image in function = here

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()