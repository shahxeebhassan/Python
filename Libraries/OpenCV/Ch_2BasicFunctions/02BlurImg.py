import cv2 as cv
img = cv.imread('/media/mysterious/Personal/Programming/Python/Resources/1.png')
#cvtColor() function is used to convert an image from one color space to another color space.
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#Blur the image using Gaussian Blur
blurimg=cv.GaussianBlur(img,(7,7),0)
blurimg1=cv.GaussianBlur(imggray,(7,7),0)

#Gaussion Blur is used to reduce the noise in the image. 
# IT takes 3 parameters: image, kernel size and sigmaX.
# Kernel size is the size of the matrix. 
# SigmaX is the standard deviation in the X direction.
# Kernel size should be odd and positive.
# cv.imshow('Gray Image',imggray)
cv.imshow('Gray Image',imggray)
cv.imshow('Blur Image Gray',blurimg1)
cv.waitKey(0)