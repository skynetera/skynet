#!/usr/bin/env python
# coding: utf-8
__author__ = 'whoami'

"""
@version: 1.0
@author: whoami
@license: Apache Licence 2.0
@contact: skyneteye@gmail.com
@site: http://www.itweet.cn
@software: PyCharm Community Edition
@file: skynet_agent.py
@time: 2015-11-28 下午12:44
"""

import pickle
import threading
import time
from SkynetConfig import SkynetConfig
from SkynetLog import skynetLog
from SkynetAgentProtoImpl import SkynetAgentProtoImpl
import global_settings
from plugins import plugin_api

log = skynetLog(object_name=__file__).log()

class SkynetAgent(object):

    def __init__(self,server_ip,server_port,skynet_config_path):
        self.server_ip = server_ip
        self.skynet_config = SkynetConfig(skynet_config_path)
        self.plugins_configs = {}
        self.skynet_agent = SkynetAgentProtoImpl(server_ip,server_port)

    def get_configs(self):
        config = self.skynet_agent.getConfigs('HostConfig::%s' % self.server_ip)
        if config:
            self.plugins_configs = pickle.loads(config)  # pickle serializer
            return True

    def format_msg(self,key,value):
        msg = {key: value}
        return pickle.dumps(msg)

    def handle(self):
        self.report_service_data = {}

        if self.get_configs():
            #print 'going to monitor services--',self.configs
            while True:
                after = time.time()
                for service_name,val in self.plugins_configs['services'].items():

                    interval,plugin_name,last_check_time = val

                    if time.time() - last_check_time >= interval:
                        #need to check off the next run
                        t = threading.Thread(target=self.task,args=[service_name,plugin_name])
                        t.start()

                        #update last check time
                        self.plugins_configs['services'][service_name][2] = time.time()

                    else:
                        next_run_time = interval-(time.time() - last_check_time)
                        log.info('\033[32;1m%s \033[0m will be run in next \033[32;1m %s \033[0m seconds' %(service_name,next_run_time))

                time.sleep(5)

                if self.report_service_data:

                    # print {'report_service_data::%s' %time.strftime('%Y%m%d%H%M') : self.report_service_data.values()}
                    # msg = self.format_msg('report_service_data::%s' %time.strftime('%Y%m%d%H%M'),self.report_service_data.values())
                    msg = self.format_msg('report_service_data::%s' %time.time(),self.report_service_data.values())
                    flag = self.skynet_agent.push(msg)

                    try:
                        if flag:
                            log.info('\033[0;31;1m push>> push data success \033[0m')
                            self.report_service_data.clear()
                    except Exception,e:
                        log.error('%s ==> %s' %('push data fail',e.message))
        else:
            log.warn('could not found any configurations for this host....')

    def task(self,service_name,plugin_name):
        log.info('going to run service: %s %s ' %(service_name,plugin_name))
        func = getattr(plugin_api,plugin_name)
        result = func()

        self.report_service_data[service_name]={
                                'ip':self.server_ip,
                                'service_name':service_name,
                                'data':result
                                }

    def run(self):
        self.handle()

    def register(self):
        print self.skynet_config.get('server','skynet_server_ip')

if __name__ == '__main__':

    skynet_server_ip = '127.0.0.1'
    skynet_server_port = 50051

    config_file_path = '../conf/skynet-site.ini'

    agent = SkynetAgent(skynet_server_ip,skynet_server_port,config_file_path)
    agent.register()
    agent.run()
