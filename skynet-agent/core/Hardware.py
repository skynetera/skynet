#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: Hardware.py
@time: 2016-09-15 11:15
"""
import os
import commands
from SkynetLog import SkynetLog

log = SkynetLog(__file__).log()

class Hardware():
    def __init__(self):
        self.hardware = {}

    def osdisks(self):
        value_dic = {
            'mounts':{

            }
        }

        """
        No such file or directory: '/etc/xxx' and return mount_dirs gt 50G mount_point
        """
        try:
            f = open('/etc/fstab')
            lines = f.readlines()
            f.close()
            for line in lines:
                if '#' not in line and 'ext' in line or 'xfs' in line:
                    mount_dir = line.split()[1]
                    type = line.split()[2]

                    disk = os.statvfs(mount_dir)
                    total = float(disk.f_bsize * disk.f_blocks / (1024 * 1024 * 1024))

                    # disk space > 50GB , push to skynet server.
                    if total > 50:

                        value_dic['mounts'][mount_dir] = {
                            'disk_total': total,
                        }

                    else:
                        pass
            return value_dic
        except IOError,e:
            log.error(e)

    def facterInfo(self):
        value_dic = {
            'hardware_specs': {

            }
        }

        """
        No such file or directory: '/etc/xxx'
        """

        try:
            mem = {}

            f_mem = open("/proc/meminfo")
            mem_lines = f_mem.readlines()
            f_mem.close()

            for line in mem_lines:
                if len(line) < 2: continue
                name = line.split(':')[0]
                var = line.split(':')[1].split()[0]
                mem[name] = long(var) / (1024.0*1024.0)   # memory Units GB

            # get cpu cores --> ls /sys/devices/system/cpu/|grep cpu[0-9]|wc -l
            status,result = commands.getstatusoutput('nproc --all')

            cpu_cores = None

            if status!=0:
                log.warn('get cpu_cores currently only works on X86/Power and some ARM CPUs. %s' %result)
            else:
                cpu_cores = result

            value_dic['hardware_specs'] = {
                'mem_total' : round(mem['MemTotal'], 2),
                'cpu_cores' : cpu_cores,
            }

            return value_dic

        except IOError, e:
            print(e)
        finally:
            if f_mem is not None:
                f_mem.close()

    def get(self):
        hardware_dic = {
            'hardware_specs'    :   self.facterInfo()['hardware_specs'],
            'osdisks'           :   self.osdisks()['mounts']
        }

        return hardware_dic

if __name__ == '__main__':
    hardware = Hardware()
    print hardware.get()
