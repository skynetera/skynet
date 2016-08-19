#!/usr/bin/env python
# coding: utf-8
__author__ = 'whoami'

"""
@version: 1.0
@author: whoami
@license: Apache Licence 2.0
@contact: skynet@gmail.com
@site: http://www.itweet.cn
@software: PyCharm Community Edition
@file: log.py
@time: 2015-12-27 下午4:05
"""
import logging
import time

class skynetLog(logging.getLoggerClass()):

    def __init__(self,clevel = logging.DEBUG,Flevel = logging.DEBUG):
        self.path = '../../log/skynet_agent-%s.log' %(time.strftime('%Y%m%d'))
        self.logger = logging.getLogger(self.path)
        self.logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler('monitor.log')
        fh.setLevel(logging.INFO)

        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(threadName)s [%(module)s:%(funcName)s] - %(message)s', '%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def debug(self,message):
        self.logger.debug(message)

    def info(self,message):
        self.logger.info(message)

    def warn(self,message):
        self.logger.warn(message)

    def error(self,message):
        self.logger.error(message)

    def critical(self,message):
        self.logger.critical(message)




if __name__ == "__main__":
    log = skynetLog(logging.INFO,logging.DEBUG)
    log.info('debug.....')