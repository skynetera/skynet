#!/usr/bin/env python
# coding: utf-8
__author__ = 'whoami'

"""
@version: 1.0
@author: whoami
@license: Apache Licence 2.0
@contact: skutil@gmail.com
@site: http://www.itweet.cn
@software: PyCharm Community Edition
@file: netstats.py.py
@time: 2015-11-28 上午12:54
"""

import generic
from data_process import avg,hit,last

class nic(generic.BaseService):
    def __init__(self):
        super(nic, self).__init__()
        self.name = 'nic_network'
        self.interval = 120
        self.plugin_name = 'get_network_info'
        self.triggers ={
            'usage':{'func':avg,
                    'minutes':15,
                    'operator':'gt',
                    'warning':80,
                    'critical':90,
                    'data_type':'percentage'
                     },
        }