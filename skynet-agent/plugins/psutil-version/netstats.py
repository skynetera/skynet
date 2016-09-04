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
@file: netstats.py
@time: 2015-11-28 下午2:49
"""
import time
import psutil

def monitor(frist_invoke=2):

        value_dic={'face':{}}

        tot_before, tot_after, pnic_before, pnic_after = poll(frist_invoke)

        for key in pnic_after.keys():
            sent = (pnic_after[key].bytes_sent-pnic_before[key].bytes_sent)/(1024*1024)
            recv = (pnic_after[key].bytes_recv-pnic_before[key].bytes_recv)/(1024*1024)
            packets_sent = (pnic_after[key].packets_sent-pnic_before[key].packets_sent)
            packets_recv = (pnic_after[key].packets_recv-pnic_before[key].packets_recv)

        if key.strip()!='lo':
            value_dic['face'][key] = {
                'system.network.nic':key,
                'system.network.bytes_sent':sent/frist_invoke,
                'system.network.bytes_recv':recv/frist_invoke,
                'system.network.packets_sent': packets_sent,
                'system.network.packets_recv': packets_recv,
            }

        return value_dic

def poll(interval):
    """
    Retrieve raw stats within an interval window.
    """
    tot_before = psutil.net_io_counters()
    pnic_before = psutil.net_io_counters(pernic=True)
    # sleep some time
    time.sleep(interval)
    tot_after = psutil.net_io_counters()
    pnic_after = psutil.net_io_counters(pernic=True)
    return (tot_before, tot_after, pnic_before, pnic_after)

if __name__ == '__main__':

    m = monitor()
    print m