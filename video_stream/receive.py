# client to receive stuff from the socket

import socket

addr_model = ("127.0.0.1", 3000)

# buffer to receive stuff into
buff = 512

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(addr_model)
msg, _ = s.recvfrom(buff)

print(msg)