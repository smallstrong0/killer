#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 16:51
# @Author  : SmallStrong
# @Des     : 
# @File    : writer.py
# @Software: PyCharm


import os
from string import Template
from env_killer import *
from settings import *


# Template使用参考 https://www.cnblogs.com/subic/p/6552752.html
def nginx_writer():
    lines = []
    class_file = open("/etc/nginx/conf.d/{}.conf".format(PROJECT_NAME), "wt")
    template_file = open(os.getcwd() + '/nginx.txt', 'r')
    lines.append(Template(template_file.read()).safe_substitute
        (
        server_name=SERVER_NAME,
        path=PROJECT_NAME,
        pid=PID,
    ))
    class_file.writelines(lines)
    class_file.close()


def uwsgi_writer():
    lines = []
    class_file = open("/etc/uwsgi_{}.ini".format(PROJECT_NAME), "wt")
    template_file = open(os.getcwd() + '/uwsgi.txt', 'r')
    lines.append(Template(template_file.read()).safe_substitute
        (
        name=PROJECT_NAME,
        path=APPLICATION_PATH,
        pid=PID,
        workers_num=WORKERS_NUM,
    ))
    class_file.writelines(lines)
    class_file.close()


def shell_writer():
    lines = []
    class_file = open("/etc/init.d/uwsgi_{}".format(PROJECT_NAME), "wt")
    template_file = open(os.getcwd() + '/shell.txt', 'r')
    lines.append(Template(template_file.read()).safe_substitute
        (
        name=PROJECT_NAME,
    ))
    class_file.writelines(lines)
    class_file.close()
