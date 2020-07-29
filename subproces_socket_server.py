#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# mode = 'r', 'w', 'w'
# print(set(mode))
# if not set(mode) <= {"r", "w", "b"}:
#     raise ValueError("invalid mode %r (only r, w, b allowed)" % (mode,))

# a = 'a'
# print(a.split(','))

# import os
# if hasattr(os, "fork"):
#     print(1)


import socket
import subprocess

HOST = ''
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print('socket server listening {} ...'.format((HOST, PORT)))

cmd = "python -m http.server".split()

global process

process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE,
                           bufsize=1, universal_newlines=True)
pid = process.pid
print(pid)

while True:
    print('Waiting connect ...')
    conn, addr = server_socket.accept()
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        print("Receive: ", type(data), data)
        if not data:
            break
        if int(data.decode('utf-8')) == 0:
            process.kill()
            print("down ", pid)
            conn.send(b'down')
        if int(data.decode('utf-8')) == 1:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE,
                                       bufsize=1, universal_newlines=True)
            print('up: ', process.pid)
            conn.send(b'up')


