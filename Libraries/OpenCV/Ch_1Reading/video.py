import cv2

# VideoCapture function to read a video
cap = cv2.VideoCapture('/media/mysterious/Personal/Programming/Python/Resources/v.mp4')

# while loop to read frames from the video one by one 
while True:
    # read function to read the frames
    ret, frame = cap.read()
    # imshow function to display the frames
    cv2.imshow('Video', frame)
    # waitkey() function to display the frames for a particular time
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break