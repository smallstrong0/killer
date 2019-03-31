#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/31 11:16
# @Author  : SmallStrong
# @Des     : settings
# @File    : settings.py
# @Software: PyCharm

PROJECT_NAME = "SS_TEST"  # 项目名称
SERVER_NAME = "www.smallstrong.wang"  # 服务器域名或者IP地址
PID = 6000  # 跑uwsgi进程的端口号
WORKERS_NUM = 2  # uwsgi子进程进程数量
APPLICATION_PATH = "{}{}{}".format("/usr/share/nginx/html/", PROJECT_NAME, "/")  # APP项目地址
