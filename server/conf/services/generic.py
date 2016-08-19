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
@file: generic.py
@time: 2015-11-26 下午8:38
"""

class BaseService(object):

    def __init__(self):
        self.name = 'BaseService'
        self.interval = 300
        self.last_time = 0
        self.plugin_name = 'your_plugin_name'
        self.triggers = {}