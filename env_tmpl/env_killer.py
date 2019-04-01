#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/23 16:23
# @Author  : SmallStrong
# @Des     : 
# @File    : env_killer.py
# @Software: PyCharm


import sys, os
import writer
import time
from settings import *


def ssh(cmd):
    os.system(cmd)


def run():
    writer.nginx_writer()
    writer.uwsgi_writer()
    writer.shell_writer()
    time.sleep(2)
    ssh('sudo chkconfig --add /etc/init.d/uwsgi_{}'.format(PROJECT_NAME))
    time.sleep(0.5)
    ssh('sudo chkconfig /etc/init.d/uwsgi_{} on'.format(PROJECT_NAME))
    time.sleep(0.5)
    ssh('sudo chmod 777 /etc/init.d/uwsgi_{}'.format(PROJECT_NAME))
    time.sleep(0.5)
    ssh('sudo service uwsgi_{} start'.format(PROJECT_NAME))
    time.sleep(1)
    ssh('sudo nginx -s reload')
    time.sleep(1)
    ssh('ps aux | grep uwsgi_{}'.format(PROJECT_NAME))


def destroy():
    ssh('sudo service uwsgi_{} stop'.format(PROJECT_NAME))
    for path in writer.get_path():
        ssh('sudo rm -rf {}'.format(path))


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) > 1:
        if argv[1] == "rm":
            destroy()
    else:
        run()
