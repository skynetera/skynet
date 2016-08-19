#!/usr/bin/env python
# coding: utf-8
__author__ = 'whoami'

"""
@version: 1.0
@author: whoami
@license: Apache Licence 2.0
@contact: skutil@gmail.com
@site: http://www.itweet.cn
@software: PyCharm Community Edition
@file: main_server.py
@time: 2015-11-28 下午3:04
"""

from redishelper import RedisHelper
from rpcserver import RpcMain
import serializer

import action_process

class MonitorServer(object):

    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.rpc = RpcMain(ip,port)  # init starting rpc server

if __name__ == '__main__':
    # serializer.flush_all_host_configs_into_redis()
    ms = MonitorServer('0.0.0.0',18800)
    print '-------starting monitor server---------'
    ms.run()