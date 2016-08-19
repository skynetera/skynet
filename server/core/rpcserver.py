#!/usr/bin/env python
# coding: utf-8
__author__ = 'whoami'

"""
@version: 1.0
@author: whoami
@license: Apache Licence 2.0
@contact: skynet@gmail.com
@site: http://www.itweet.cn
@software: PyCharm Community Edition
@file: rpcserver.py
@time: 2015-12-27 下午1:35
"""

import msgpackrpc
import serializer
from skynet import skynet

class RpcServer(object):
    def __init__(self):
        self.conf = serializer.init_all_host_configs_into_client()
        self.sk = skynet()
        print '---init configs info---'

    def heartbeat(self,heartbeat):
        pass

    def configs(self,host_ip):
        for k,v in self.conf.items():
            return v.get(host_ip)

    def push(self,msg):
        self.sk.forward(msg)

    def jobs(self,task):
        pass

class RpcMain(object):
    def __init__(self,ip,port):

        server = msgpackrpc.Server(RpcServer())
        server.listen(msgpackrpc.Address(ip, port))
        print '-------starting rpc server listening port:18800---------'
        server.start()