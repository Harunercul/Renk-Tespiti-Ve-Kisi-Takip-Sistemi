#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Yüklenen görüntü üzerindeki rengin HSV kodunu yazdırma www.hbmacit.com
import cv2
import numpy as np

def TiklamaOlayi(olay, x, y, flags, param):
    if olay == cv2.EVENT_LBUTTONDOWN:
        h = hsv[y, x, 0]
        s = hsv[y, x, 1]
        v = hsv[y, x, 2]
        hsvUzayi = 'HSV: ' + str(h) + ' ' + str(s) + ' ' + str(v)
        cv2.putText(goruntu, hsvUzayi, (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (100,20,0),1 )
        cv2.imshow("Goruntu", goruntu)

goruntu = cv2.imread(r'C:\Users\HPWIN10\Desktop\mavi2.jpg') #Buraya istenen bir görüntünün adresini/adını giriniz.
hsv = cv2.cvtColor(goruntu, cv2.COLOR_BGR2HSV)
cv2.imshow("Goruntu", goruntu)
cv2.setMouseCallback('Goruntu',TiklamaOlayi)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




