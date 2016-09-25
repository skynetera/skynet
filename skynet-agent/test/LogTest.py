#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: LogTest.py
@time: 2016-09-14 10:03
"""


import logging
import threading
import time

def worker(arg):
    while not arg['stop']:
        logging.debug('Hi from myfunc')
        time.sleep(0.5)

def main():
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
    info = {'stop': False}
    thread = threading.Thread(target=worker, args=(info,))
    thread.start()
    while True:
        try:
            logging.debug('Hello from main')
            time.sleep(0.75)
        except KeyboardInterrupt:
            info['stop'] = True
            break
    thread.join()

def test_finnaly():
    try:
        t = open('abc.txt')
        return 'abc'
    except IOError,e:
        print e
    finally:
        if t is not None:
            print 'is not none'
            t.close()
        else:
            print 'is none'
        print 'return exec...'

if __name__ == '__main__':
    # main()
    print test_finnaly()