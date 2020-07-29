#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket
import sys
import time

HOST, PORT = '0.0.0.0', 5000
# data = ''.join(sys.argv[1:])

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((HOST, PORT))

# socket_client.sendall(bytes(data, encoding='utf-8') + b'\n')
socket_client.sendall(bytes('1', encoding='utf-8') + b'\n')

# Receive data from the server and shut down
# while True:

received = socket_client.recv(1024)
print("Receive: ", received)

# socket_client.close()
