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
@file: DataProcess.py
@time: 2015-12-29 下午4:25
"""

import ActionProcess
import Serializer
import pickle
import threading,os
import datetime
import global_settings
from db import InfluxdbClient

class DataProcess(object):

    def __init__(self):
        self.hosts = Serializer.all_host_configs()
        self.db = InfluxdbClient.InfluxdbClient()

    def handle(self,msg):
        # print 'recv:',msg
        # print '>> process data:: %s' % pickle.loads(msg)
        data = pickle.loads(msg)
        for k,msg in data.items():
            fun_name = k.split('::')[0]
            time = k.split('::')[1]
            ActionProcess.action_process(self, fun_name, time, msg)
        print '---------waiting for new msg ---------'

        # received data
        for host,val in self.hosts['hosts'].items():
            if val:
                t = threading.Thread(target=self.process,args=[host,val])
                t.start()
            else:
                print '%s host monitor info is null...' % host

    def forward(self,msg):
        print '-------starting Processing data---------'
        self.handle(msg)

    def process(self,host,val):

        print 'Task %s runs pid %s' % (host,os.getpid())

        tags = {
                    "host": "%s" % host,
                    "region": "us-west"
        }

        for v in val.values():
            timestamp = float(v['timestamp'])
            time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            measurement = v['data'].keys()[0]
            data = v['data'].values()[0]
            self.db.wirte_points(tags,measurement,time,data)

        # clear service_instance data object
        self.hosts['hosts'][host].clear()
