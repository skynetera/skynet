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
@file: templates.py
@time: 2015-11-26 下午8:35
"""

from services import linux
from services import network

class BaseTemplate(object):
    def __init__(self):
        self.name = 'YourTemplateName'
        self.group_name = 'YourGroupName'
        self.hosts = []
        self.services = []
        self.enabled = 'no'

class LinuxTemplate(BaseTemplate):
    def __init__(self):
        super(LinuxTemplate,self).__init__()
        self.name = 'LinuxTemplate'
        self.services = [
            linux.cpu,
            linux.memory,
            linux.disk,
            linux.load,
            linux.swap,
            linux.netstat,
            linux.iostat,
        ]
        self.enabled = 'yes'

class NetworkTemplate(BaseTemplate):
    def __init__(self):
        super(NetworkTemplate,self).__init__()
        self.name = 'NetworkTemplate'
        self.services = [
            network.nic,
            linux.cpu,
        ]
        self.enabled = 'yes'

if __name__ == '__main__':
    t = LinuxTemplate()
    t.hosts = ['127.0.0.1','192.168.2.125']

    for service in t.services:
        service = service()
        if service.name == 'linux_cpu':
            service.interval = 90
        print service.name,service.interval

    print '-------------t2 below-------------'
    t2 = LinuxTemplate()
    t2.hosts = ['127.0.0.1','192.168.2.125']

    for service in t2.services:
        service = service()
        print service.name,service.interval