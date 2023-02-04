#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np
import imutils
 


# Grab the image

img = cv2.imread(r"C:\Users\HPWIN10\Desktop\kareler\benim00001.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

kirmizi_alt_deger = np.array([105,100,100])
kirmizi_ust_deger = np.array([130, 255, 255])

mask = cv2.inRange(hsv,kirmizi_alt_deger,kirmizi_ust_deger)

cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

for c in cnts:
    alan = cv2.contourArea(c)
    print('Alan:  ', alan)
    
    cv2.drawContours(img,[c],-1,(0,255,0),3)
    
    
    key = cv2.waitKey(1)
    if key ==27:
        break
        
    cv2.imshow("Image",img)
    cv2waitKey(1)
    



# In[ ]:




