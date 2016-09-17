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
@file: SkynetLog.py
@time: 2015-12-27 下午4:05
"""
import logging
import time
import os

class SkynetLog(object):

    def __init__(self,object_name='skynetLog',file_log_level=logging.ERROR,console_log_level=logging.DEBUG,log_path='logs/',log_filename='skynet-sm-server'):
        self.logger = logging.getLogger(os.path.basename(object_name))
        self.logger.setLevel(logging.DEBUG)

        # create file handler which logs even debug messages
        fh = logging.FileHandler('%s%s-%s.log' %(log_path,log_filename,time.strftime('%Y%m%d')))
        fh.setLevel(file_log_level)

        # create console handler with a higher log level
        ch = logging.StreamHandler()
        ch.setLevel(console_log_level)

        # create formatter and add it to the handlers
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter(
            '[%(asctime)s] %(name)s [%(levelname)s] %(threadName)s-%(relativeCreated)d [%(module)s:%(funcName)s] - %(message)s',
            '%Y-%m-%d %H:%M:%S')

        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # add the handlers to logger
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def log(self):
        return self.logger

if __name__ == "__main__":

    logger = SkynetLog(object_name='examples_test').log()

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')