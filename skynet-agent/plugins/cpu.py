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

def round_percentage(number,ndigits):
    return round(number*100,2)

def monitor(frist_invoke=2):

        interval=frist_invoke

        f = open('/proc/stat')
        cpu_t1 = f.readline().split()
        f.close()

        time.sleep(interval)

        f = open('/proc/stat')
        cpu_t2 = f.readline().split()
        f.close()

        cpu_total_t1 = float(eval(('+'.join(cpu_t1)).split('cpu+')[1]))
        cpu_idle_t1 = float(cpu_t1[4])


        cpu_total_t2 = float(eval(('+'.join(cpu_t2)).split('cpu+')[1]))
        cpu_idle_t2 = float(cpu_t2[4])

        cpu_idle = cpu_idle_t2-cpu_idle_t1
        cpu_total = cpu_total_t2-cpu_total_t1

        cpu_percent = (cpu_total-cpu_idle)/cpu_total

        cpu_total_tmp = cpu_total_t1+cpu_total_t2/2
        cpu_user_tmp = (int(cpu_t1[1])+int(cpu_t2[1]))/2
        cpu_nice_tmp = (int(cpu_t1[2])+int(cpu_t2[2]))/2
        cpu_system_tmp = (int(cpu_t1[3])+int(cpu_t2[3]))/2
        cpu_idle_tmp = (int(cpu_t1[4])+int(cpu_t2[4]))/2
        cpu_iowait_tmp = (int(cpu_t1[5])+int(cpu_t2[5]))/2
        cpu_irq_tmp = (int(cpu_t1[6])+int(cpu_t2[6]))/2
        cpu_softirq_tmp = (int(cpu_t1[7])+int(cpu_t2[7]))/2
        cpu_steal_tmp = (int(cpu_t1[8])+int(cpu_t2[8]))/2
        cpu_guest_tmp = (int(cpu_t1[9])+int(cpu_t2[9]))/2

        value_dic = {
            'cpu_user': round_percentage(cpu_user_tmp/cpu_total_tmp,2),
            'cpu_nice': round_percentage(cpu_nice_tmp/cpu_total_tmp,2),
            'cpu_system': round_percentage(cpu_system_tmp/cpu_total_tmp,2),
            'cpu_idle': round_percentage(cpu_idle_tmp/cpu_total_tmp,2),
            'cpu_iowait': round_percentage(cpu_iowait_tmp/cpu_total_tmp,2),
            'cpu_irq': round_percentage(cpu_irq_tmp/cpu_total_tmp,2),
            'cpu_softirq': round_percentage(cpu_softirq_tmp/cpu_total_tmp,2),
            'cpu_steal': round_percentage(cpu_steal_tmp/cpu_total_tmp,2),
            'cpu_guest': round_percentage(cpu_guest_tmp/cpu_total_tmp,2),
            'cpu_percent': round_percentage(cpu_percent,2),
        }

        return value_dic


if __name__ == '__main__':
    print monitor()