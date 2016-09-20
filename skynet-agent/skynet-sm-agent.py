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

from core.SkynetAgent import SkynetAgent
from core.SkynetConfig import SkynetConfig

if __name__ == '__main__':

    config_file_path = 'conf/skynet-site.ini'

    skynet_config = SkynetConfig(config_file_path)

    agent = SkynetAgent(skynet_config)
    agent.register()
    agent.run()
