import cv2 as cv
img = cv.imread('/media/mysterious/Personal/Programming/Python/Resources/1.png')
#cvtColor() function is used to convert an image from one color space to another color space.
imggray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',imggray)
cv.waitKey(0)