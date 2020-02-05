"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM) convert stream to grayscale n print height n width
"""

import cv2
cap = cv2.VideoCapture(0)#0 denote the camera(when have multiple so one can select between them)
print(cap.isOpened())
while(cap.isOpened()):#isOpened() check for the file(file name right or wrong)
    ret, frame = cap.read()
    #ret will be true if frame is available 
    #frame will save the frame from the camera
    
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    gsp = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gsp)
    if cv2.waitKey(1) & OxFF == ord('q'):
        #0xFF mask for 64 bit if require
        cv2.imwrite('X:\\rudresh\\AI\\try\\lena1.png',frame)
        #when q is press that frame is store as pic
        break
cap.release()
cv2.destroyAllWindows()