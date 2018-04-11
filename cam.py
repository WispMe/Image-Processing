import cv2
import numpy as np
faces_class = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cam = cv2.VideoCapture(0)
Id = raw_input('enter your id : ')
sampleNum = 0

while True :
    rat, img = cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faces_class.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,225,0),2)
        sampleNum = sampleNum+1
        cv2.imwrite("Wajah/User. " +Id+ '.' + str(sampleNum) + ".jpg", gray[y:y+h,x:x+h])
    cv2.imshow("camera", img)
    key = cv2.waitKey(1)

    if key in [27,1048603]:
        cv2.destroyAllWindows()
        break;

    elif sampleNum > 50:
        cv2.destroyAllWindows()
        break

