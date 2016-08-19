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
@file: linux.py
@time: 2015-11-26 下午8:47
"""

import generic
from data_process import avg,hit,last,capacity,size

'''
    python operator models (lt,le,eq,ne,ge,gt)
'''

class cpu(generic.BaseService):
    def __init__(self):
        super(cpu,self).__init__()
        self.name = 'linux_cpu'
        self.interval = 60
        self.plugin_name = 'get_cpu_status'
        self.triggers = {
            'idle':{'func':avg,
                    'minutes':15,
                    'operator':'lt',
                    'warning':20,
                    'critical':5,
                    'data_type':'percentage'
                    },
            'iowait':{'func':hit,
                      'minutes' : 10,
                      'operator' : 'gt',
                      'threshold' : 3,
                      'warning' : 50,
                      'critical' : 80,
                      'data_type' : 'int'
                      },
                        }

class memory(generic.BaseService):
    def __init__(self):
        super(memory, self).__init__()
        self.name = 'linux_memory'
        self.interval = 60
        self.plugin_name = 'get_memory_info'
        self.triggers ={
            'usage':{'func':avg,
                    'minutes':15,
                    'operator':'gt',
                    'warning':80,
                    'critical':90,
                    'data_type':'percentage'
                     },
        }

class disk(generic.BaseService):
    def __init__(self):
        super(disk, self).__init__()
        self.name = 'linux_disk'
        self.interval = 900
        self.plugin_name = 'get_disk_info'
        self.triggers ={
            'usage':{'func':capacity,
                    'minutes':15,
                    'operator':'gt',
                    'warning':80,
                    'critical':90,
                    'data_type':'percentage'
                     },
        }

class load(generic.BaseService):
    def __init__(self):
        super(load, self).__init__()
        self.name = 'linux_load'
        self.interval = 60
        self.plugin_name = 'get_load_info'
        self.triggers ={
            'usage':{'func':avg,
                    'minutes':15,
                    'operator':'gt',
                    'warning':0.85,
                    'critical':0.95,
                    'data_type':'float'
                     },
        }

class swap(generic.BaseService):
    def __init__(self):
        super(swap, self).__init__()
        self.name = 'linux_swap'
        self.interval = 60
        self.plugin_name = 'get_swap_info'
        self.triggers ={
            'usage':{'func':capacity,
                    'minutes':900,
                    'operator':'gt',
                    'warning':85,
                    'critical':95,
                    'data_type':'percentage'
                     },
        }

class netstat(generic.BaseService):
    def __init__(self):
        super(netstat, self).__init__()
        self.name = 'linux_netstat'
        self.interval = 60
        self.plugin_name = 'get_network_info'
        self.triggers ={
            'usage':{'func':size,
                    'minutes':900,
                    'operator':'gt',
                    'warning':1000,
                    'critical':1500,
                    'data_type':'permb'
                     },
        }

class iostat(generic.BaseService):
    def __init__(self):
        super(iostat, self).__init__()
        self.name = 'linux_iostat'
        self.interval = 60
        self.plugin_name = 'get_iostats_info'
        self.triggers ={
            'usage':{'func':size,
                    'minutes':900,
                    'operator':'gt',
                    'warning':1000,
                    'critical':1500,
                    'data_type':'permb'
                     },
        }

if __name__ == '__main__':
    c = cpu()
    print c.name,c.interval,c.plugin_name
