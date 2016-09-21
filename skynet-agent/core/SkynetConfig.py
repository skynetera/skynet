#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: SkynetConfig.py
@time: 2016-09-17 16:13
"""

import ConfigParser

class SkynetConfig():

    def __init__(self,path):
        self.__path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.__path)

    def get(self,field,key):
        result =""
        try:
            result = self.cf.get(field,key)
        except:
            result = ""

        return result

    def set(self, filed, key, value):
        try:
            self.cf.set(filed, key, value)
            self.cf.write(open(self.__path, 'w'))
        except:
            return False
        return True

if __name__ == '__main__':
    config_file_path = '../conf/config.ini'
    sc = SkynetConfig(path=config_file_path)
    print sc.get('General','server_host')
    # print sc.set('General','server_thread_pool_max_workers','60')

    print sc.cf.sections()     # ['server', 'agent']
    print sc.cf.options("General")
    print sc.cf.items('General')
