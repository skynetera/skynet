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

def monitor(frist_invoke=1):
    value_dic = {
        'mount':{},
    }

    f = open('/etc/fstab')
    lines = f.readlines()
    f.close()

    for line in lines:
        if '#' not in line and 'ext' in line:
            mount_dir = line.split()[1]
            type = line.split()[2]

            disk = os.statvfs(mount_dir)
            total = float(disk.f_bsize * disk.f_blocks/(1024*1024))
            used = total-float(disk.f_bsize * disk.f_bfree/(1024*1024))
            free = float(disk.f_bsize * disk.f_bavail/(1024*1024))

            value_dic['mount'][mount_dir] = {
                'disk_device':mount_dir,
                'disk_total':total,
                'disk_used':used,
                'disk_free':free,
                'disk_percent': round((float(used/total)*100),2),
                'disk_type':type,
            }
    return value_dic

if __name__ == '__main__':
    mount = monitor()
    print mount
    for m in mount['mount'].keys():
        print m,mount['mount'][m]