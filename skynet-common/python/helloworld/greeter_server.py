#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: greeter_server.py
@time: 2016-08-30 20:33
"""

from concurrent import futures

import time

import grpc

import helloworld_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
test = open('./workfile', 'r+')

class Greeter(helloworld_pb2.GreeterServicer):

    def SayHello(self, request, context):
        try:
            test.write('client msg: ' + request.name)
            return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)
        finally:
            if request.name is None:
                print '1'
                test.close()

def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=50))
    helloworld_pb2.add_GreeterServicer_to_server(Greeter(),server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    server()