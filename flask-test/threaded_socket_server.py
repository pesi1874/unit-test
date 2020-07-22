#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket
import threading
import socketserver
import time


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = f"{cur_thread.name}:{data}"

        # 模拟阻塞
        print(f"{cur_thread.name}收到数据{data}:模拟阻塞")
        time.sleep(5)
        print(f"{cur_thread.name}模拟阻塞完成")
        self.request.sendall(bytes(response, encoding='utf-8'))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == '__main__':
    Host, Port = "0.0.0.0", 9999

    server = ThreadedTCPServer((Host, Port), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    server.serve_forever()
