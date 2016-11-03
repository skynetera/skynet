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
    sdiskio = psutil.disk_io_counters()
    # sleep some time

    value_dic = {
        'iostats': {
            'io.disks_read': sdiskio.read_bytes/(1024*1024),
            'io.disks_write': sdiskio.write_bytes/(1024*1024),
            'io.disks_read_count': sdiskio.read_count/(1024 * 1024),
            'io.disks_write_count': sdiskio.write_count/(1024 * 1024),
            'io.disks_read_time': sdiskio.read_time/1000,
            'io.disks_write_time': sdiskio.write_time/1000,
            'io.disks_busy_time': sdiskio.write_time/1000,
        }
    }

    return value_dic

if __name__ == '__main__':
    print monitor()
