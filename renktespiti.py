#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import cv2 


webcam = cv2.VideoCapture(r'C:\Users\HPWIN10\Desktop\proje1.mp4') 


while(1): 

	_, imageFrame = webcam.read() 


	hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV) 
    
#renkleri maskeleme
#blue color
	blue_lower = np.array([105, 100, 100], np.uint8) 
	blue_upper = np.array([130, 255, 255], np.uint8) 
	blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper) 
    #red color
	red_lower = np.array([136, 87, 111], np.uint8) 
	red_upper = np.array([180, 255, 255], np.uint8) 
	red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 
    #pink color
	pink_lower = np.array([173, 100, 120], np.uint8) 
	pink_upper = np.array([178, 180, 220], np.uint8) 
	pink_mask = cv2.inRange(hsvFrame, pink_lower, pink_upper)    
    #yellow color
	yellow_lower = np.array([13, 100, 100], np.uint8) 
	yellow_upper = np.array([21, 245, 245], np.uint8) 
	yellow_mask = cv2.inRange(hsvFrame, yellow_lower, yellow_upper) 
    #orange color
	orange_lower = np.array([0, 100, 100], np.uint8) 
	orange_upper = np.array([12, 245, 245], np.uint8) 
	orange_mask = cv2.inRange(hsvFrame, orange_lower, orange_upper) 
    #green color
	green_lower = np.array([40, 100, 100], np.uint8) 
	green_upper = np.array([65, 245, 245], np.uint8) 
	green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 

	kernal = np.ones((5, 5), "uint8") 

	# For blue color 
	blue_mask = cv2.dilate(blue_mask, kernal) 
	res_blue = cv2.bitwise_and(imageFrame, imageFrame, 
							mask = blue_mask) 
    #for red color
	red_mask = cv2.dilate(red_mask, kernal) 
	res_red = cv2.bitwise_and(imageFrame, imageFrame, 
							mask = red_mask) 
    #for pink color
	pink_mask = cv2.dilate(pink_mask, kernal) 
	res_pink = cv2.bitwise_and(imageFrame, imageFrame, 
							mask = pink_mask) 
    #for yellow color
	yellow_mask = cv2.dilate(yellow_mask, kernal) 
	res_yellow = cv2.bitwise_and(imageFrame, imageFrame, 
							mask = yellow_mask) 
    #for orange color
	orange_mask = cv2.dilate(orange_mask, kernal) 
	res_orange = cv2.bitwise_and(imageFrame, imageFrame, 
							mask = orange_mask) 
    #for green color
	green_mask = cv2.dilate(green_mask, kernal) 
	res_green = cv2.bitwise_and(imageFrame, imageFrame, 
							mask = green_mask) 

#Contour kavramını kullanarak renk tespiti
	# Creating contour to track blue color 
	contours, hierarchy = cv2.findContours(blue_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 4000):    
			x, y, w, h = cv2.boundingRect(contour) 
			imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(255, 0, 0), 2) 
			
			cv2.putText(imageFrame, "blue", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (255, 0, 0)) 
			
#creating contour to track red color
	contours, hierarchy = cv2.findContours(red_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 4000):    
			x, y, w, h = cv2.boundingRect(contour) 
			imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(0, 0, 255), 2) 
			
			cv2.putText(imageFrame, "red", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (0, 0, 255)) 
		
	# Creating contour to track pink color 
	contours, hierarchy = cv2.findContours(pink_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 4000):    
			x, y, w, h = cv2.boundingRect(contour) 
			imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(255, 209, 220), 2) 
			
			cv2.putText(imageFrame, "pink", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (255, 209, 220)) 
			
	# Creating contour to track yellow color 
	contours, hierarchy = cv2.findContours(yellow_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 4000):    
			x, y, w, h = cv2.boundingRect(contour) 
			imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(0, 255, 255), 2) 
			
			cv2.putText(imageFrame, "yellow", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (0, 255, 255)) 
			
	# Creating contour to track orange color 
	contours, hierarchy = cv2.findContours(orange_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 4000):    
			x, y, w, h = cv2.boundingRect(contour) 
			imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(255, 95, 31), 2) 
			
			cv2.putText(imageFrame, "orange", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (255, 95, 31)) 
			
	# Creating contour to track green color 
	contours, hierarchy = cv2.findContours(green_mask, 
										cv2.RETR_TREE, 
										cv2.CHAIN_APPROX_SIMPLE) 
	for pic, contour in enumerate(contours): 
		area = cv2.contourArea(contour) 
		if(area > 4000):    
			x, y, w, h = cv2.boundingRect(contour) 
			imageFrame = cv2.rectangle(imageFrame, (x, y), 
									(x + w, y + h), 
									(255, 95, 31), 2) 
			
			cv2.putText(imageFrame, "green", (x, y), 
						cv2.FONT_HERSHEY_SIMPLEX, 
						1.0, (255, 95, 31)) 
			


	# çalıştırma
	cv2.imshow("Birden Çok Renk Tespiti", imageFrame) 
	if cv2.waitKey(10) & 0xFF == ord('q'): 
		cap.release() 
		cv2.destroyAllWindows() 
		break


# In[ ]:




