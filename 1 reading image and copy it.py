"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM) press s to copy the photo on particular position n esc to discard

"""
import cv2
img = cv2.imread('X:\\rudresh\\AI\\openCv\\opencv-master\\opencv-master\\doc\\js_tutorials\\js_assets\\lena.jpg',1)
# parameter in above syntax
#0 for grayscale
#-1 for including alpha channel
#1color image

cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF #0 denote no delay, after certain time as mention as a parameter it will run out

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('X:\\rudresh\\AI\\try\\me.png',img)
    cv2.destroyAllWindows()
#only use esc n s key as we have not put else here to show esc, youll get in upcoming with the learning
print('hello', img)#get matrix for the image(vector)