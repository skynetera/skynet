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
@file: plugin_api.py
@time: 2015-11-28 下午1:52
"""

import cpu,loadavg,memory,disk,netstats,swap,iostats

def get_load_info():
    return loadavg.monitor()

def get_cpu_status():
    return cpu.monitor()

def get_memory_info():
    return memory.monitor()

def get_swap_info():
    return swap.monitor()

def get_disk_info():
    return disk.monitor()

def get_network_info():
    return netstats.monitor()

def get_iostats_info():
    return iostats.monitor()


