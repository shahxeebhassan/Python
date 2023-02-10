import cv2 as cv
import numpy as np

img = cv.imread('/media/mysterious/Personal/Programming/Python/Resources/lamb.jpg')
print(img.shape) #Height,Width,Channel

imgresize = cv.resize(img,(1000,600))

croppedImg = img[0:600,100:1100]
print(imgresize.shape)
cv.imshow('Lamb', imgresize)
cv.imshow('Croped Image',croppedImg)
cv.waitKey(0)
