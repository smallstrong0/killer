#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 10:40
# @Author  : SmallStrong
# @Des     : 
# @File    : index.py
# @Software: PyCharm


from flask import Flask
from flask import make_response

app = Flask(__name__)


@app.route('/api/<func>', methods=['GET', 'POST'])
def go(func):
    exec 'import app.' + func
    data = eval('app.' + func + '.go()')
    response = make_response(data)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == '__main__':
    app.run()
