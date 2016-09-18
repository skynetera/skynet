#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: Register.py
@time: 2016-09-14 23:23
"""

import time
from Hardware import Hardware
from HostInfo import HostInfo

class Register(object):
  """ Registering with the server. Get the hardware profile and
  declare success for now """
  def __init__(self, config):
    self.hardware = Hardware()
    self.host_info = HostInfo()
    self.config = config

  def build(self, version, id='-1'):
    timestamp = int(time.time()*1000)

    host_ip,host_name = self.host_info.checkReverseLookup()

    current_ping_port = self.config.get('agent','ping_port')

    register = { 'responseId'        : int(id),
                 'timestamp'         : timestamp,
                 'hostname'          : host_name,
                 'hostip'            : host_ip,
                 'currentPingPort'   : int(current_ping_port),
                 'hardwareProfile'   : self.hardware.get(),
                 'agentVersion'      : version,
                 'hostInfo'           : self.host_info.get_os_info(),
               }

    return register

if __name__ == '__main__':
    reg = Register(config='abc')
    print reg.build(version='0.0.1')