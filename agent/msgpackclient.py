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
@file: msgpackclient.py
@time: 2015-12-27 下午2:06
"""


import msgpackrpc

class MsgpackClient:

    def __init__(self):
        self.client = msgpackrpc.Client(msgpackrpc.Address("localhost", 18800),timeout=10)

    def getConfig(self,host_ip):
        try:
            return self.client.call('configs',host_ip)
        except Exception,e:
            print e.message,'connect server timeout'

    def push(self,msg):
        try:

            self.client.call('push',msg)
            return True
        except Exception,e:
            print e.message,'connect server timeout'

    def jobs(self,task):
        pass

if __name__ == '__main__':
    msg = MsgpackClient()
    print msg.getConfig('HostConfig::127.0.0.1')





