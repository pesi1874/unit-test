#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket
import sys
import time

HOST, PORT = '0.0.0.0', 9999
data = ''.join(sys.argv[1:])

print(data)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    s_t = time.time()
    s.connect((HOST, PORT))
    s.sendall(bytes(data, encoding='utf-8') + b'\n')

    # Receive data from the server and shut down
    received = s.recv(1024)
    print(time.time() - s_t)
finally:
    s.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))
