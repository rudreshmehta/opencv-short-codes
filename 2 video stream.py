"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM) Turn on camera and will be exited by pressing q and storing the frame at particular location 
"""

import cv2
cap = cv2.VideoCapture(0)#0 denote the camera(when have multiple so one can select between them)
while(True):
    ret, frame = cap.read()
    #ret will be true if frame is available 
    #frame will save the frame from the camera
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & OxFF == ord('q'):
        #0xFF mask for 64 bit if require
        print(frame)
        cv2.imwrite('X:\\rudresh\\AI\\try\\lena1.png',frame)
        #when q is press that frame is store as pic
        break
cap.release()
cv2.destroyAllWindows()