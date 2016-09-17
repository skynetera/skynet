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
        self.path = path
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)

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
            self.cf.write(open(self.path, 'w'))
        except:
            return False
        return True

if __name__ == '__main__':
    config_file_path = '../conf/skynet-site.ini'
    sc = SkynetConfig(path=config_file_path)
    print sc.get('server','skynet_server_ip')
    print sc.set('agent','logdir','/var/log/skynet-agent')

    print sc.cf.sections()     # ['server', 'agent']
    print sc.cf.options("server")
    print sc.cf.items('server')
