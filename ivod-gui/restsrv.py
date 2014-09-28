#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext import restful

# set the project root directory as the static folder, you can set others.
flaskapp = Flask(__name__, static_url_path='')
api = restful.Api(flaskapp)

@flaskapp.route('/')
def index():
    return flaskapp.send_static_file('index.html')

@flaskapp.route('/hello')
def hello():
    return 'Hello World'

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hellores')
    
if __name__ == '__main__':
    #flaskrun()
    pass