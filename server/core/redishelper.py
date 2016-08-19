#!/usr/bin/env python
# coding: utf-8
__author__ = 'whoami'

"""
@version: 1.0
@author: whoami
@license: Apache Licence 2.0
@contact: skynetEye@gmail.com
@site: http://www.itweet.cn
@software: PyCharm Community Edition
@file: redishelper.py
@time: 2015-11-25 下午11:11
"""
import redis

class RedisHelper:

    def __init__(self):
        self.__conn = redis.Redis(host='127.0.0.1')
        self.chan_sub = 'fm188'
        self.chan_pub = 'fm188'

    def get(self,key):
        return self.__conn.get(key)

    def set(self,key,value):
        return self.__conn.set(key,value)

    def publish(self,msg):
        self.__conn.publish(self.chan_pub,msg)
        return True

    def subscribe(self):
        pub = self.__conn.pubsub()
        pub.subscribe(self.chan_sub)
        pub.parse_response()
        return pub

if __name__ == '__main__':
    t = RedisHelper()
    t.publish('whoami')
