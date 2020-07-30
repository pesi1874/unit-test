#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import select

tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind(("127.0.0.1", 8001))
tcp_server_socket.listen(1)
tcp_server_socket.setblocking(True)

e = select.epoll()
e.register(tcp_server_socket.fileno(), select.EPOLLIN)

fd_event_dict = {}

while True:
    print("epoll waiting ...")
    fd_event_list = e.poll()

    for fd, event in fd_event_list:
        if fd == tcp_server_socket.fileno():
            new_socket, client_addr = tcp_server_socket.accept()
            print(new_socket, client_addr)
            e.register(new_socket.fileno(), select.EPOLLIN)
            fd_event_dict[new_socket.fileno()] = new_socket
        elif event == select.EPOLLIN:
            print(2)
            recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
            print(recv_data)

            if recv_data:
                print(fd_event_dict[fd], recv_data)
            else:
                fd_event_dict[fd].close()
                e.unregister(fd)
                del fd_event_dict

# tcp_server_socket.close()