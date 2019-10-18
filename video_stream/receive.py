# client to receive stuff from the socket

import socket
import math
import numpy as np
import cv2 as cv

addr_model = ("127.0.0.1", 3000)

# width and height of receiving video
width = 640
height = 480

# buffer to receive stuff into
buff = 512

# num of packets that make up one frame
# 640 * 480 * 3 = 921600 / 512 = 1800
num = (640 * 480 * 3) / buff

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(addr_model)

while(True):
  # store chunks of frame
  data = []
  
  for i in range(0, math.floor(num)):
    msg, _ = s.recvfrom(buff)
    data.append(msg)
  
  string_frame = b''.join(data)
  frame = np.frombuffer(string_frame, dtype=np.uint8).reshape(height, width, 3)
  frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
  cv.imshow('receive', frame)
  if cv.waitKey(25) & 0xFF == ord('q'):
    cv.destroyAllWindows()
    break

