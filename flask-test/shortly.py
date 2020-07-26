#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import time
from werkzeug.wrappers import Request, Response


class Shortly:
    def __init__(self):
        pass

    def dispatch_request(self, request):
        print(request.path)
        if request.path == '/index':
            print(f'path:{request.path},start sleep for 15 s')
            time.sleep(15)
        else:
            print(f'path:{request.path},say hello now ')
        return Response('Hello World')

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ=environ, start_response=start_response)


def create_app():
    app = Shortly()
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple

    app = create_app()
    run_simple('127.0.0.1', 4000, app, threaded=True)
