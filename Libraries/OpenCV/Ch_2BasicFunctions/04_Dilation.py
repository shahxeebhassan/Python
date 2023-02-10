import cv2 as cv
import numpy as np
img = cv.imread('/media/mysterious/Personal/Programming/Python/Resources/1.png')
kernel = np.ones((5,5),np.uint8) # kernel is a matrix of 1's of size 5x5 and data type is unsigned integer of 8 bits which is 0-255 range of values 
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurimg=cv.GaussianBlur(img,(7,7),0)

# blurimg1=cv.GaussianBlur(imggray,(7,7),0)

imgCanny=cv.Canny(img,150,200)

imgDilation=cv.dilate(imgCanny,kernel,iterations=3)

# cv.imshow('Gray Image',imggray)
# cv.imshow('Blur Image Gray',blurimg1)
cv.imshow('Canny Image',imgCanny)
cv.imshow('Dilation Image',imgDilation)
cv.waitKey(0)