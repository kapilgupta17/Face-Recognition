#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2
import numpy as np
import glob

face_haar_cascade = cv2.CascadeClassifier('./haar cascade xml/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_images=glob.glob('./obama_images/*.jpg')

face_train=[]
face_label=[]

for image in face_images:
    obama_image = cv2.imread(image,0)
    size=(500,500)
    obama_image = cv2.resize(obama_image,size,interpolation=cv2.INTER_AREA)
    obama_image = np.array(obama_image,"uint8")
    faces=face_haar_cascade.detectMultiScale(obama_image,1.5,4)
    
    for x,y,w,h in faces:
        mug = obama_image[y:y+h,x:x+w]
        face_train.append(mug)
        face_label.append(0)

recognizer.train(face_train,np.array(face_label))
recognizer.save("obama_face_train.yml")


# In[ ]:




