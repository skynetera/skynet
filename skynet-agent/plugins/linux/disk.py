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
@file: disk.py
@time: 2015-11-28 下午1:53
"""
import os
import psutil

def monitor(frist_invoke=1):
    value_dic = {
            'disk': {}
    }

    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        mount_point = part.mountpoint
        device =  part.device
        usage = psutil.disk_usage(part.mountpoint)
        value_dic['disk'][mount_point] = {
            'disk.device':device,
            'disk.mount_point':mount_point,
            'disk.total':usage.total/(1024*1024),
            'disk.used':usage.used/(1024*1024),
            'disk.free':usage.free/(1024*1024),
            'disk.percent': usage.percent,
            'disk.type':part.fstype,
        }

    return value_dic

if __name__ == '__main__':
    mount = monitor()
    for m in mount['disk'].keys():
        print m,mount['disk'][m]