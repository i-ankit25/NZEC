# python server
# send video stream to both server and CV model

import cv2 as cv
import socket

addr_model = ("127.0.0.1", 3000)
addr_stream = ("127.0.0.1", 5000)

width = 640
height = 480

# capture video now
cap = cv.VideoCapture(0)

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret:
    cv.imshow("frame", frame)
    if cv.waitKey(25) & 0xFF == ord('q'):
      cv.destroyAllWindows()
      break