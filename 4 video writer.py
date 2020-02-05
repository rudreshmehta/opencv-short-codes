"""
Insta: @the_tech_lancers
@author: Rudresh Mehta
AIM) Video writer class(make sure you have enough memory to run)
"""

import cv2
cap = cv2.VideoCapture(0)#0 denote the camera(when have multiple so one can select between them)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')#can be written as *'XVID'
out = cv2.VideoWriter('X:\\rudresh\\AI\\try\\output.avi', fourcc, 20.0, (640,480))
while(cap.isOpened()):#isOpened() check for the file(file name right or wrong)
    ret, frame = cap.read()
    #ret will be true if frame is available 
    #frame will save the frame from the camera
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out.write(frame)#color video creation here store
        
    
        gsp = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gsp)
        if cv2.waitKey(1) == ord('q'):
            #press q to stop cam
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()