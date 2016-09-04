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

def monitor(frist_invoke=2):
    # net rx/tx stat
    f1 = open('/proc/net/dev')
    f2 = open('/proc/net/dev')
    content1 = f1.read()
    time.sleep(frist_invoke)
    content2 = f2.read()
    f1.close()
    f2.close()

    sep = ':'
    stats1 = {}
    for line in content1.splitlines():
        if sep in line:
            i = line.split(':')[0].strip()
            data = line.split(':')[1].split()
            rx_bytes1, tx_bytes1 = (int(data[0]), int(data[8]))
            rx_pack1, tx_pack1 = (int(data[1]), int(data[9]))
            stats1[i] = [rx_bytes1, tx_bytes1, rx_pack1, tx_pack1]

    stats2 = {}
    for line in content2.splitlines():
        if sep in line:
            i = line.split(':')[0].strip()
            data = line.split(':')[1].split()
            rx_bytes2, tx_bytes2 = (int(data[0]), int(data[8]))
            rx_pack2, tx_pack2 = (int(data[1]), int(data[9]))
            stats2[i] = [rx_bytes2, tx_bytes2, rx_pack2, tx_pack2]

    value_dic = {'face':{}}

    for i in stats1.keys():
        rx_bytes_ps = (stats2[i][0] - stats1[i][0]) / frist_invoke
        tx_bytes_ps = (stats2[i][1] - stats1[i][1]) / frist_invoke
        rx_pps = (stats2[i][2] - stats1[i][2]) / frist_invoke
        tx_pps = (stats2[i][3] - stats1[i][3]) / frist_invoke

        if i.strip()!='lo':
            value_dic['face'][i] = {
                'network_nic':i,
                'network_bytes_recv':rx_bytes_ps/(1024*1024),
                'network_bytes_sent':tx_bytes_ps/(1024*1024),
                'network_packet_recv':rx_pps,
                'network_packet_sent':tx_pps,
            }

    return value_dic

if __name__ == '__main__':

    m = monitor()
    print m