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
@file: memory.py
@time: 2015-11-28 下午1:51
"""
import psutil

def monitor(frist_invoke=1):

    mem = psutil.virtual_memory()

    value_dic = {
        'system.mem.total': int(mem.total/(1024*1024)),
        'system.mem.free': int(mem.free/(1024*1024)),
        'system.mem.buffers': int(mem.buffers/(1024*1024)),
        'system.mem.cache': int(mem.cached/(1024*1024)),
        'system.mem.used': int(mem.used/(1024*1024)),
        'system.mem.percent': mem.percent
    }

    return value_dic

if __name__ == '__main__':
    print monitor()