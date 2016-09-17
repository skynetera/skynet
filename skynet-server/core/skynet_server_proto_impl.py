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
@file: skynet_server_proto_impl.py
@time: 2015-12-27 下午1:35
"""

import skynet_core_pb2
import serializer
from data_process import DataProcess
import time
import grpc
from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class SkynetServerProto(skynet_core_pb2.SkynetProtoServicer):
    def __init__(self):
        self.conf = serializer.initialize_all_host_configs()
        self.data_process = DataProcess()
        print '[INFO] Init configs info...'

    def heartbeat(self, request, context):
        if request.request_msg is 'server1':
            return skynet_core_pb2.reply(reply_msg='server heartbeat success %s  %s' %(request.request_msg,time.time()))
        else:
            return skynet_core_pb2.reply(reply_msg='server heartbeat fail %s  %s' %(request.request_msg,time.time()))

    def configs(self, request, context):
        host_ip = request.request_msg
        for k,v in self.conf.items():
            host_config = v.get(host_ip)
            return skynet_core_pb2.reply(reply_msg=host_config)

    def push(self, request, context):
        message = request.request_msg
        if message is not None:
            self.data_process.forward(message)
            return skynet_core_pb2.reply(reply_msg='push data success. time %s' % time.time())
        else:
            return skynet_core_pb2.reply(reply_msg='push data fail. time %s' % time.time())

    def register(self, request, context):
        
        pass

class SkynetServerProtoImpl(object):
    def __init__(self, ip, port):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=50))
        skynet_core_pb2.add_SkynetProtoServicer_to_server(SkynetServerProto(), server)
        server.add_insecure_port('[::]:%s' % port)
        print '[INFO] Starting skynet server protoc listening port %s %s ' %(port,time.time())
        server.start()
        try:
            while True:
                time.sleep(_ONE_DAY_IN_SECONDS)
        except KeyboardInterrupt:
            server.stop(0)

if __name__ == '__main__':
    SkynetServerProtoImpl('0.0.0.0',50051)