import cv2
# imread function to read an image

img = cv2.imread('/media/mysterious/Personal/Programming/Python/Resources/1.png')

# imshow function to display an image

# It takes two arguments: the window name and the image to be displayed in the window 

cv2.imshow('Output', img)


#waitkey() function of Python OpenCV allows users to display a window for given milliseconds or until any key is pressed. It takes time in milliseconds as a parameter and waits for the given time to destroy the window, if 0 is passed in the argument it waits till any key is pressed.
cv2.waitKey(0)
