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
@file: SkynetServer.py
@time: 2015-11-28 下午3:04
"""

from SkynetServerProtoImpl import SkynetServerProtoImpl
import time

class SkynetServer(object):

    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.skynet_proto = SkynetServerProtoImpl(ip,port)  # init starting rpc skynet-server

if __name__ == '__main__':
    ss = SkynetServer('0.0.0.0',50051)
    print '[INFO] Stoping skynet server %s' % time.time()