#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket
import sys
import time

HOST, PORT = '0.0.0.0', 5000

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((HOST, PORT))


while True:
    data = input('Input: ')

    socket_client.sendall(bytes(data, encoding='utf-8'))

    received = socket_client.recv(1024)
    print("Receive: ", received)


