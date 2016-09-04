#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: greeter_client.py
@time: 2016-08-30 20:41
"""

from __future__ import print_function
import grpc
import helloworld_pb2
import time
import threading

def task(stub,i):
    response = stub.SayHello(helloworld_pb2.HelloRequest(name='you task %s' % i + ""))
    # print("Greeter client received %s: " %i)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = helloworld_pb2.GreeterStub(channel)
    startTime = time.time()
    threads = []
    for i in range(1,10000):
        t = threading.Thread(target=task,args=(stub,"Thread - %s" % i))
        threads.append(t)
        t.start()

    endTime = time.time()

    print (endTime-startTime)

if __name__ == '__main__':
    run()
