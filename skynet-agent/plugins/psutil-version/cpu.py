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
@file: cpu.py
@time: 2015-11-28 下午1:51
"""
import time
import psutil

def monitor(frist_invoke=2):
        cpu = psutil.cpu_times_percent(interval=frist_invoke, percpu=False)
        cpu_percent = psutil.cpu_percent(interval=frist_invoke)

        value_dic = {
            'system.cpu.user': cpu.user,
            'system.cpu.nice': cpu.nice,
            'system.cpu.system':cpu.system,
            'system.cpu.idle':cpu.idle,
            'system.cpu.iowait': cpu.iowait,
            'system.cpu.irq': cpu.irq,
            'system.cpu.softirq': cpu.softirq,
            'system.cpu.steal': cpu.steal,
            'system.cpu.guest': cpu.guest,
            'system.cpu.percent': cpu_percent
        }

        return value_dic

if __name__ == '__main__':
    print monitor()