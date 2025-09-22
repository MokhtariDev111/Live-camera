 
#importation 
#initialisation 
#read
#show 
#break 
#cam.release() destroyall 

import cv2

cam=cv2.VideoCapture(1)

while True: 
    ret , frame = cam.read()
    grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("mywebcam",grayframe)
    cv2.moveWindow("mywebcam",900,540)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows

 