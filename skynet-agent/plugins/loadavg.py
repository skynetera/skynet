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

def monitor(frist_invoke=1):
    f = open('/proc/loadavg')
    load = f.read().split()
    f.close()

    value_dic = {
        'load_1min':load[0],
        'load_5min':load[1],
        'load_15min':load[2],
    }

    return value_dic

if __name__ == '__main__':
   print monitor()
