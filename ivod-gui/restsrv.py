#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext import restful

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
api = restful.Api(app)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/hello')
def hello():
    return 'Hello World'

class HelloWorld(restful.Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/hellores')

def flaskrun():
    app.run(host='0.0.0.0',port=8080)
    
if __name__ == '__main__':
    # util.py -u 'http://ivod.ly.gov.tw/Play/VOD/76394/300K'
    flaskrun()