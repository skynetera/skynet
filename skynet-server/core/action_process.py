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
@file: action_process.py
@time: 2015-11-28 下午3:06
"""

import pickle
import serializer

def action_process(server_instance,func_name,time,data):

    for msg in data:
        msg['timestamp'] = time

        func = getattr(serializer,func_name)

        func(server_instance,msg)