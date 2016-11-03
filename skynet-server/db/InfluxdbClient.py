#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: InfluxdbClient.py
@time: 2016-11-02 下午2:30
"""
from influxdb import InfluxDBClient

username = 'root'
password = 'root'
database = 'skm'
infuxdb_port = 8086
infuxdb_ip = 'localhost'

class InfluxdbClient(object):

    def __init__(self):
        self.username = username
        self.password = password
        self.database = database
        self.infuxdb_port = infuxdb_port
        self.infuxdb_ip = infuxdb_ip
        self.client = InfluxDBClient(self.infuxdb_ip, self.infuxdb_port, self.username, self.password, self.database)
        self.client.create_database(self.database)

    def wirte_points(self,tags,measurement,time,data):

        if type(data.values()[0])==dict:
            json_body = []
            for v in data.values():
                json_obj = {
                        "measurement": "%s" % measurement,
                        "tags": tags,
                        "time": "%s" % time,
                        "fields": v
                    }
                json_body.append(json_obj)
            self.client.write_points(json_body)
        else:
            json_body = [
                {
                    "measurement": "%s" % measurement,
                    "tags": tags,
                    "time": "%s" %time,
                    "fields": data
                }
            ]
            self.client.write_points(json_body)

if __name__ == '__main__':
    json_body = [
        {
            "measurement": "cpu_load",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2008-11-10T23:00:00Z",
            "fields": {
                "value": 0.64
            }
        },
        {
            "measurement": "cpu_load",
            "tags": {
                "host": "server01",
                "region": "us-west"
            },
            "time": "2007-11-10T23:00:00Z",
            "fields": {
                "value": 0.64
            }
        }
    ]
    db = InfluxDBClient()
    db.write_points(points=json_body,database='example')