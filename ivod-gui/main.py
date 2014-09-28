#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from dl import download_video
from restsrv import flaskapp

if __name__ == '__main__':
    flaskapp.run(host='0.0.0.0',port=9680)