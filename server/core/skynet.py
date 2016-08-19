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
@file: skynet.py
@time: 2015-12-29 下午4:25
"""

import action_process
import serializer
import pickle
import threading,os
import global_settings
from graph import rrdtool

class skynet(object):

    def __init__(self):
        self.hosts = serializer.all_host_configs()
        self.rrd_path = '/home/whoami/py/SkynetEye/monitor/rrd'
        self.rrdtool = rrdtool.rrdtool(self.rrd_path)

    def handle(self,msg):
        # print 'recv:',msg
        # print '>> process data:: %s' % pickle.loads(msg)
        data = pickle.loads(msg)
        for k,msg in data.items():
            fun_name = k.split('::')[0]
            time = k.split('::')[1]
            action_process.action_process(self,fun_name,time,msg)
        print '---------waiting for new msg ---------'

        # received data
        for host,val in self.hosts['hosts'].items():
            if val:
                t = threading.Thread(target=self.process,args=[host,val])
                t.start()
            else:
                print '%s host monitor info is null...' %host

    def forward(self,msg):
        print '-------starting Processing data---------'
        self.handle(msg)

    def process(self,host,val):
        print 'Task %s runs pid %s' % (host,os.getpid())

        args = []
        data = ''
        for k in val.values():
            timestamp = k['timestamp']
            if len(k['data'].keys()) > 1:
                for s,e in k['data'].items():
                    args.append(s)
                    data += str(e)+':'
        else:
            if os.path.exists(self.rrd_path+'/%s.rrd' %host):
                pass
            else:
                try:
                    self.rrdtool.create(host,*args)
                except Exception,e:
                    print 'create rrd database fail...%s' % e.message

            data = timestamp+':'+data[:-1]
            print self.rrdtool.updatev(host,data,*args)

        for k,v in val.items():

            if len(v['data'].keys()) > 1:
                args = v['data'].keys()
                print self.rrdtool.graph(str(host),str(k),'服务器%s统计信息'%k,str(k),*args)