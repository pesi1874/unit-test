#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket

HOST = ''
PORT = 5000


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print('socket server listening {} ...'.format((HOST, PORT)))

while True:
    print('Waiting connect ...')
    conn, addr = server_socket.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        print("Receive: ", data)
        if not data:
            break
        conn.sendall(data)



