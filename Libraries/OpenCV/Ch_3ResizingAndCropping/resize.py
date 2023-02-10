import cv2 as cv
import numpy as np

img = cv.imread('/media/mysterious/Personal/Programming/Python/Resources/lamb.jpg')
print(img.shape) #Height,Widtth,Channel

imgresize = cv.resize(img,(1000,600))
print(imgresize.shape)
cv.imshow('Lamb', imgresize)
# cv.imshow('Lamb', img)
cv.waitKey(0)
