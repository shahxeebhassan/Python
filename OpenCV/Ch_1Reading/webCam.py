import cv2
# VideoCapture function to read a webcam 
cap = cv2.VideoCapture(0) # 0 is the default camera
cap.set(3, 640) # 3 is the width
cap.set(4, 480) # 4 is the height
cap.set(10, 100) # 10 is the brightness
# while loop to read frames from the webcam one by one
while True:
    # read function to read the frames
    ret, frame = cap.read()
    # imshow function to display the frames
    cv2.imshow('Webcam', frame)
    # waitkey() function to display the frames for a particular time
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break