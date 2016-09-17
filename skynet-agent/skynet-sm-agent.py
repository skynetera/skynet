#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: skynet-sm-agent.py
@time: 2016-09-14 11:47
"""

from core.skynet_agent import SkynetAgent

if __name__ == '__main__':

    skynet_server_ip = '127.0.0.1'
    skynet_server_port = 50051

    config_file_path = '../conf/skynet-site.ini'

    agent = SkynetAgent(skynet_server_ip,skynet_server_port,config_file_path)
    agent.run()
