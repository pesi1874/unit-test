#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket

HOST = ''
PORT = 5007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(HOST, PORT)
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)

# Echo client program
# import socket
#
# HOST = '0.0.0.0'  # The remote host
# PORT = 50007  # The same port as used by the server
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b'Hello, world')
#     data = s.recv(1024)
# print('Received', repr(data))



