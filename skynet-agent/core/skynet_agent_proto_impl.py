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
@file: skynet_agent_proto_impl.py
@time: 2015-12-27 下午2:06
"""


import grpc
import skynet_core_pb2

class SkynetAgentProtoImpl(object):

    def __init__(self,master_ip,master_port):
        self.channel = grpc.insecure_channel('%s:%s' %(master_ip,master_port))
        self.stub = skynet_core_pb2.SkynetProtoStub(self.channel)

    def getConfigs(self,host_ip):
        try:
            response = self.stub.configs(skynet_core_pb2.call(request_msg=host_ip))
            return response.reply_msg
        except Exception,e:
            print e,'connect skynet server timeout'

    def push(self,msg):
        try:
            self.stub.push(skynet_core_pb2.call(request_msg=msg))
        except Exception,e:
            print e.message,'connect skynet server timeout'

    def jobs(self,task):
        pass

    def register(self):
        pass

if __name__ == '__main__':
    sap = SkynetAgentProtoImpl()
    print sap.getConfigs('HostConfig::127.0.0.1')
    # channel = grpc.insecure_channel('localhost:50051')
    # stub = skynet_core_pb2.SkynetProtoStub(channel)
    # response = stub.configs(skynet_core_pb2.call(request_msg='HostConfig::127.0.0.1'))
    # print response