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
import psutil

def monitor(frist_invoke=1):

    swap = psutil.swap_memory()

    value_dic = {
        'system.swap.total': int(swap.total/(1024*1024)),
        'system.swap.free': int(swap.free/(1024*1024)),
        'system.swap.used': int(swap.used/(1024*1024)),
        'system.swap.percent':swap.percent,
    }

    return value_dic

if __name__ == '__main__':
    print monitor()