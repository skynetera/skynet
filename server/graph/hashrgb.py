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
@file: hashrgb.py
@time: 2016-01-08 上午2:37
"""

import hashlib

def hsv2rgb(h, s, v):
    h += 0.618033988749895
    h %= 1
    h_i = int(h*6)
    f = h*6 - h_i
    p = v * (1 - s)
    q = v * (1 - f*s)
    t = v * (1 - (1 - f) * s)

    if h_i == 0:
        r, g, b = v, t, p
    elif h_i == 1:
        r, g, b = q, v, p
    elif h_i == 2:
        r, g, b = p, v, t
    elif h_i == 3:
        r, g, b = p, q, v
    elif h_i == 4:
        r, g, b = t, p, v
    elif h_i == 5:
        r, g, b = v, p, q
    else:
        r = g = b = 0
    return [int(r*256), int(g*256), int(b*256)]


def str2rgb(obj):
    digest = hashlib.sha384(str(obj).encode('utf-8')).hexdigest()

    sub_size = int(len(digest) / 3)
    max_value = float(int("f" * sub_size, 16))
    digests = [digest[i * sub_size: (i + 1) * sub_size] for i in range(3)]

    rgb = (((int(d, 16) / max_value)+0.618033988749895) % 1 for d in digests)

    return '#' + ''.join(["%02x" % int(c*255 + 0.5 - 0.0000005) for c in rgb])


def str2rgb2(obj):
    digest = hashlib.sha384(str(obj).encode('utf-8')).hexdigest()

    obj_value = int(digest, 16)
    max_value = float(int("f" * len(digest), 16))

    rgb = hsv2rgb(obj_value/max_value, 0.5, 0.95)

    return '#' + ''.join(["%02x" % c for c in rgb])