#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from flask import Flask, Response, request, jsonify

app = Flask(__name__)


@app.route('/user/<int:user_id>', methods=['GET'])
def hello_world(user_id):
    req = request.json
    return jsonify({'user': user_id})
    # return Response(
    #     f'Get /user/{user_id} has been'
    #     f' processed in flask app\r\n',
    #     mimetype='text/plain'
    # )


if __name__ == '__main__':
    app.run()
