# python server
# send video stream to both server and CV model

import cv2 as cv
import numpy as np
import socket

# addresses to stream to
addr_model = ("127.0.0.1", 3000)
addr_stream = ("127.0.0.1", 5000)

width = 640
height = 480

# buffer size for one data packet
# bcoz otherwise one frame will be huge
buff = 512

# capture video now
cap = cv.VideoCapture(0)

# width and height for the video
cap.set(4, width)
cap.set(3, height)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# s.sendto(b'How you doin?', addr_model)

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret:
    data = frame.tostring()
    for i in range(0, len(data), buff):
      s.sendto(data[i : i + buff], addr_model)

    # s.sendto(data, addr_model)
    cv.imshow("frame", frame)
    if cv.waitKey(25) & 0xFF == ord('q'):
      cv.destroyAllWindows()
      break