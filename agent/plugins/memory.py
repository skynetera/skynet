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

def monitor(frist_invoke=1):
    mem = {}

    f = open("/proc/meminfo")
    lines = f.readlines()
    f.close()
    for line in lines:
        if len(line) < 2: continue
        name = line.split(':')[0]
        var = line.split(':')[1].split()[0]
        mem[name] = long(var) / (1024.0)

    mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']

    value_dic = {
        'mem_total':round(mem['MemTotal'],2),
        'mem_free':round(mem['MemFree'],2),
        'mem_buffers':round(mem['Buffers'],2),
        'mem_cache':round(mem['Cached'],2),
        'mem_used':round((mem['MemTotal'] - mem['MemFree']),2),
        'mem_percent': round((mem['MemUsed'])/(mem['MemTotal']),2)*100
    }

    return value_dic

if __name__ == '__main__':
    print monitor()