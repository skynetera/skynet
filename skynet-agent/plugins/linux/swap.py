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
@file: swap.py
@time: 2015-12-03 下午3:16
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
        mem[name] = float(var) / (1024.0)

    swap_used = mem['SwapTotal']-mem['SwapFree']-mem['SwapCached']

    value_dic = {
        'swap_total':round(mem['SwapTotal'],2),
        'swap_cached':round(mem['SwapCached'],2),
        'swap_free':round(mem['SwapFree'],2),
        'swap_used':swap_used,
        'swap_percent':round(swap_used/mem['SwapTotal'],2)
    }

    return value_dic

if __name__ == '__main__':
    print monitor()