import numpy as np
import cv2
import sys

hand_cascade = cv2.CascadeClassifier('Opencv/haarcascade/palm.xml')

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    hand = hand_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in hand:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)
        print(f'{x} {y}')
        sys.stdout.flush()

    # Display the resulting frame
    cv2.imshow('notframelmao', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
