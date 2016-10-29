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

def monitor(frist_invoke=2):
    """
    Return (inbytes, outbytes, in_num, out_num, ioms) of disk.
    """
    f1 = open('/proc/diskstats')
    f2 = open('/proc/diskstats')
    content1 = f1.read()
    time.sleep(frist_invoke)
    content2 = f2.read()
    f1.close()
    f2.close()
    ds1 = {}
    for l in content1.splitlines():
        d = l.strip().split()
        if d[2].startswith('loop') or d[2].startswith('ram') or \
           d[2].startswith('dm-') or \
           d[2].startswith('fd') or d[2].startswith('sr'):
           continue
        ds1[d[2]] = [d[3], d[7], d[4], d[8], d[12]]
    ds2 = {}
    for l in content2.splitlines():
        d = l.strip().split()
        if d[2].startswith('loop') or d[2].startswith('ram') or \
           d[2].startswith('fd') or d[2].startswith('sr'):
           continue
        ds2[d[2]] = [d[3], d[7], d[4], d[8], d[12]]
    ds = {}
    for d in ds1.keys():
        rnum = float(int(ds2[d][0]) - int(ds1[d][0])) / frist_invoke
        wnum = float(int(ds2[d][1]) - int(ds1[d][1])) / frist_invoke
        blm_read = float(int(ds2[d][2]) - int(ds1[d][2])) / frist_invoke / 1024
        blm_wrtn = float(int(ds2[d][3]) - int(ds1[d][3])) / frist_invoke / 1024
        util = 100 * (float(int(ds2[d][4]) - int(ds1[d][4]))/(frist_invoke * 1000))

        ds[d] = [blm_read, blm_wrtn, rnum, wnum, util]

    for i in ds.keys():
        blm_read += round(ds.get(i)[0],2)
        blm_wrtn += round(ds.get(i)[1],2)
        rnum += round(ds.get(i)[2],2)
        wnum += round(ds.get(i)[3],2)
        util += round(ds.get(i)[4],2)

    value_dic = {
        'disks_io_read':blm_read,
        'disks_io_write':blm_wrtn,
        'disks_io_read_num': rnum,
        'disks_io_write_num': wnum,
        'disks_io_util': util
    }

    return value_dic

if __name__ == '__main__':
    print monitor()
