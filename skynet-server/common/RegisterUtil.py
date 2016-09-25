#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: RegisterUtil.py
@time: 2016-09-14 23:12
"""
import json
from SkynetLog import SkynetLog
import os

log = SkynetLog(__file__).log()

def get(hostip):
    with open('/opt/rrd_data/registory.json', 'r') as reg_data:
        data = json.load(reg_data)
        try:
            value = data['host_list'][hostip]
            return value
        except KeyError,e:
            log.error('Your registory hostip not exist. %s' % e)
        finally:
            if reg_data is not None:
                reg_data.close()

def exists_reg(hostip):
    log.warn('Your registory hostip already exists.')
    pass

def set(register_data):
    try:
        init_json = {
            "host_list": {

            }
        }

        if os.path.exists('/opt/rrd_data/registory.json'):
            pass
        else:
            reg = open('/opt/rrd_data/registory.json', 'w')
            json.dump(init_json, reg)
            reg.close()

        with open('/opt/rrd_data/registory.json', 'r') as reg_data:
            data = json.load(reg_data)

            data['host_list'][register_data['hostip']] = register_data

            with open('/opt/rrd_data/registory.json', 'w') as f:
                json.dump(data, f)

            return True

        return False

    except IOError,e:
        log.error(e)
    finally:
        if reg_data is not None:
            reg_data.close()
        elif f is not None:
            f.close()

def get_all_reg_host():
    with open('/opt/rrd_data/registory.json', 'r') as reg_data:
        data = json.load(reg_data)
        reg_data.close()
        return data['host_list'].keys()

if __name__ == '__main__':
    test = {"hostip":"127.0.0.1","hostname": "whoami-virtual-machine", "responseId": -1}

    # print set(test)
    print get('127.0.1.1')
    print get_all_reg_host()