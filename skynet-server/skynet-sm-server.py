#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: skynet-sm-server.py
@time: 2016-09-14 12:02
"""

from core.skynet_server import SkynetServer
import time

if __name__ == '__main__':

    skynet_master_ip,skynet_master_port='0.0.0.0',50051

    SkynetServer(skynet_master_ip,skynet_master_port)

    print '[INFO] Stoping skynet server %s' % time.time()