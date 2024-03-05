#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import glob

face_haar_cascade = cv2.CascadeClassifier('./haar cascade xml/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("obama_face_train.yml")
test_images =glob.glob('./test-data/*.jpg')

for image in test_images:
    test=cv2.imread(image,0)
    test_color=cv2.imread(image)
    faces=face_haar_cascade.detectMultiScale(test,1.5,4)
    
    for x,y,w,h in faces:
        test_face = test[y:y+h,x:x+w]
        
        num,confidence = recognizer.predict(test_face)
        
        if confidence>=55 and confidence<=89:
            
            font=cv2.FONT_HERSHEY_SIMPLEX
            con=round(confidence,2)
            name='Obama: {}'.format(con)
            color=(0,255,60)
            cv2.putText(test_color,name,(x,y),font,1,color,2,cv2.LINE_AA)
            cv2.rectangle(test_color,(x,y),(x+w,y+h),(0,255,60),2)
    cv2.imwrite(image,test_color)


# In[ ]:




