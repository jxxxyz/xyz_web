# -*- encoding: utf-8 -*-
"""
@author: jiaxinxin
@license: (C) Copyright 2015-2019, Palmax Corporation Limited.
@contact:jiaxinxin@palmax.cn
@software: PyCharm
@file: app.py
@time: 2019-06-06 14:12
@desc:
"""
import logging
import asyncio
import os
import json
import time
from datetime import datetime
from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>Hello, skr</h1>', headers={'content-type':'text/html'})


def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    web.run_app(app, host='127.0.0.1', port=9000)
    logging.info('server started at http://127.0.0.1:9000...')


if __name__ == '__main__':
    init()
