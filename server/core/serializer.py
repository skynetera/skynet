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
@file: serializer.py
@time: 2015-11-28 上午12:17
"""
import pickle
import time

import global_settings
from conf import hosts
from redishelper import RedisHelper


def host_config_serializer(host_ip):
    applied_services = []
    configs = {
        'services':{},
        #'refresh_config_interval':
    }
    for group in hosts.monitored_groups:
        if host_ip in group.hosts:
             #git all monitor plugins
            applied_services.extend(group.services)
    #去重插件,不同模板可能出现重复监控监控插件
    applied_services = set(applied_services)

    for service in applied_services:
        service = service()
        configs['services'][service.name] = [service.interval,
                                             service.plugin_name,
                                             0
                                             ]
    return configs

def flush_all_host_configs_into_redis():
    applied_hosts = []
    redis = RedisHelper()
    for group in hosts.monitored_groups:
        applied_hosts.extend(group.hosts)
    applied_hosts = set(applied_hosts)

    for host_ip in applied_hosts:
        host_config = host_config_serializer(host_ip)
        key = 'HostConfig::%s' %host_ip
        redis.set(key,pickle.dumps(host_config))
    return True

def init_all_host_configs_into_client():
    applied_hosts = []
    redis = RedisHelper()
    for group in hosts.monitored_groups:
        applied_hosts.extend(group.hosts)
    applied_hosts = set(applied_hosts)

    configs = {'configs':{}}
    for host_ip in applied_hosts:
        host_config = host_config_serializer(host_ip)
        key = 'HostConfig::%s' %host_ip

        configs['configs'][key] = pickle.dumps(host_config)

    return configs

def report_service_data(service_instance,msg):
    # print 'recv:',msg
    host_ip = msg['ip']
    service_status_data = msg['data']
    service_name = msg['service_name']
    timestamp = msg['timestamp']

    service_instance.hosts['hosts'][host_ip][service_name] = {
        'data':service_status_data,
        'timestamp':timestamp
    }

    key = 'StatusData::%s' % host_ip

    # waring data put redis 3 hour
    # service_instance.redis.set(key,pickle.dumps(service_instance.hosts['hosts'][host_ip]))

def all_host_configs():
    configs = {'hosts':{}}

    for group in hosts.monitored_groups:
        for host_ip in group.hosts:
            configs['hosts'][host_ip] = {}
    return configs

if __name__ == '__main__':
    # print host_config_serializer('192.168.2.125')
    #flush_all_host_configs_into_redis()
    print init_all_host_configs_into_client()