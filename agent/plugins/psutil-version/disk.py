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
        'mount':{}
    }

    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        mount_path = part.mountpoint
        usage = psutil.disk_usage(part.mountpoint)

        value_dic['mount'][mount_path] = {
            'system.disk.device':mount_path,
            'system.disk.total':usage.total/(1024*1024),
            'system.disk.used':usage.used/(1024*1024),
            'system.disk.free':usage.free/(1024*1024),
            'system.disk.percent': usage.percent,
            'system.disk.type':part.fstype,
        }

    return value_dic

if __name__ == '__main__':
    mount = monitor()
    for m in mount['mount'].keys():
        print m,mount['mount'][m]