#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with

# resorce_fileds = {
#     'name': fields.String,
#     'address': fields.String,
#     'date_updated': fields.DateTime(dt_format='rfc822')
# }
#
#
# class Todo(Resource):
#     @marshal_with(resorce_fileds, envelope='resource')
#     def get(self, *kargs):
#         return db_get_todb()

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
