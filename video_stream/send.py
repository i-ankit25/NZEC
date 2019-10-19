# python server
# send video stream to both server and CV model

import cv2 as cv
import numpy as np
import socket

# addresses to stream to
addr_model = ("127.0.0.1", 5000)
addr_stream = ("127.0.0.1", 3000)

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

# code to mark beginning of a frame : solving choppiness
code = 'start'
code = ('start' + (buff - len(code)) * 'a').encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret:
    # send start code to both model and stream
    s.sendto(code, addr_model)
    s.sendto(code, addr_stream)

    # frame is sending as a string
    data = frame.tostring()

    for i in range(0, len(data), buff):
      # send chunks to model and stream
      s.sendto(data[i : i + buff], addr_model)
      s.sendto(data[i : i + buff], addr_stream)

      # show the video
      cv.imshow('send', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
      cv.destroyAllWindows()
      break
  else:
    break