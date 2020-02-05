"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM) Geometry shape n write text
"""
import cv2
import numpy as n
#img = cv2.imread('X:\\rudresh\\AI\\openCv\\opencv-master\\opencv-master\\doc\\js_tutorials\\js_assets\\lena.jpg',1)

img = n.zeros([512,512,3],n.uint8)#create image with numpy n then show art

#(img_object,(x1,y1),(x2,y2),(b,g,r),thickness)
img = cv2.line(img,(0,0),(255,255),(255,255,255),5)# B G R

img = cv2.arrowedLine(img,(50,90),(200,100),(5,55,255),10)#(img object,(x1,y1),(x2,y2),(b,g,r),thickness)

#(img_object,(x1,y1),(x2,y2),(b,g,r),thickness)
img = cv2.rectangle(img, (111,159),(333,390),(200,200,200),5)

#(img_object,(x,y),radius,(b,g,r),thickness)
img = cv2.circle(img,(55,55),50,(255,255,255),5)

#(img_object,text,(x1,y1),font_face,font_size,(b,g,r),thickness,line_type)
img = cv2.putText(img,'rudresh',(378,378),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),1,cv2.LINE_8)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()