# client to receive stuff from the socket

import socket
import math
import numpy as np
import cv2 as cv

addr_model = ("127.0.0.1", 8000)

# width and height of receiving video
width = 640
height = 480

# buffer to receive stuff into
buff = 512

# num of packets that make up one frame
# 640 * 480 * 3 = 921600 / 512 = 1800
num = (640 * 480 * 3) / buff

# start code
code = b'start'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(addr_model)

while True:
  # hold chunks of a frame
  chunks = []
  # did we get the start buff signal thing
  start = False
  while len(chunks) < num:
    chunk, _ = s.recvfrom(buff)
    # if start signal already received then append to chunks
    chunks.append(chunk)
  # join the chunks
  byte_frame = b''.join(chunks)

  # rebuild the frame
  frame = np.frombuffer(byte_frame, dtype=np.uint8).reshape(height, width, 3)

  # show the frame
  cv.imshow('recv', frame)
  if cv.waitKey(1) & 0xFF == ord('q'):
    break
