#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import socket
import sys
import time


class WSGIServer:
    def __init__(self):
        self.listener = socket.socket()
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listener.bind(('0.0.0.0', 4000))
        self.listener.listen(1024)
        print('Serving HTTP on 0.0.0.0 port 4000....')
        self.app = None
        self.headers_set = None

    def set_app(self, app):
        self.app = app

    def start_response(self, status, headers):
        self.headers_set = [status, headers]

    def server_forever(self):
        while True:
            listener = self.listener
            client_connection, client_address = listener.accept()
            print(f'server received connection from:{client_address}')
            request = client_connection.recv(1024)
            print(f'request we received:{request}')

            method, path, _ = request.split(b' ', 2)
            environ = {
                'wsgi.version': (1, 0),
                'wsgi.url_scheme': 'http',
                'wsgi.input': request,
                'wsgi.errors': sys.stderr,
                'wsgi.multithread': False,
                'wsgi.multiprocess': False,
                'wsgi.run_once': False,
                'REQUEST_METHOD': method.decode('utf-8'),
                'PATH_INFO': path.decode('utf-8'),
                'SERVER_NAME': '127.0.0.1',
                'SERVER_PORT': '4000',
            }

            app_result = self.app(environ, self.start_response)

            response_status, response_headers = self.headers_set
            response = f'HTTP/1.1 {response_status}\r\n'
            for header in response_headers:
                response += f'{header[0]}:{header[1]}\r\n'

            response += '\r\n'
            response = response.encode('utf-8')
            for data in app_result:
                response += data

            # print('sleep', response)
            # print('process')
            # time.sleep(5)
            client_connection.send(response)
            client_connection.close()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('Argv Error')
    app_path = sys.argv[1]
    module, app = app_path.split(":")
    module = __import__(module)
    app = getattr(module, app)

    server = WSGIServer()
    server.set_app(app)
    server.server_forever()
