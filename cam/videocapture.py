import numpy as np
import cv2

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret == False: 
    print("Frame is empty")
    
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#960 - 45 frames per second 107.5 frames records 1.5 seconds
