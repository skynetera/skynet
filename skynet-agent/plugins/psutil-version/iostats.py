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
import time
import psutil

def monitor(frist_invoke=2):
    """
    Return (inbytes, outbytes, in_num, out_num, ioms) of disk.
    """
    disks_before = psutil.disk_io_counters()

    # sleep some time
    time.sleep(frist_invoke)

    disks_after = psutil.disk_io_counters()

    disks_read_per_sec = disks_after.read_bytes - disks_before.read_bytes
    disks_write_per_sec = disks_after.write_bytes - disks_before.write_bytes


    value_dic = {
        'system.io.disks_read': disks_read_per_sec/frist_invoke/(1024*1024),
        'system.io.disks_write': disks_write_per_sec/frist_invoke/(1024*1024),
    }

    return value_dic

if __name__ == '__main__':
    print monitor()
