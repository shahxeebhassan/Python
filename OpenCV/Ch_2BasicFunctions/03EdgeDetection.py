import cv2 as cv

img = cv.imread('/media/mysterious/Personal/Programming/Python/Resources/1.png')

imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurimg=cv.GaussianBlur(img,(7,7),0)

blurimg1=cv.GaussianBlur(imggray,(7,7),0)

imgCanny=cv.Canny(img,150,200)

cv.imshow('Gray Image',imggray)
cv.imshow('Blur Image Gray',blurimg1)
cv.imshow('Canny Image',imgCanny)
cv.waitKey(0)