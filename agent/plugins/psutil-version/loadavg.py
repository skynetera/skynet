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
@file: loadavg.py
@time: 2015-11-28 下午1:51
"""
import os

def monitor(frist_invoke=1):
    f = open('/proc/loadavg')
    load = f.read().split()
    f.close()

    value_dic = {
        'system.load.1min':load[0],
        'system.load.5min':load[1],
        'system.load.15min':load[2],
    }

    return value_dic

if __name__ == '__main__':
   print monitor()
