#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: whoami
@license: Apache Licence 2.0
@contact: skynet199@foxmail.com
@site: http://www.itweet.cn
@software: PyCharm
@file: HostInfo.py
@time: 2016-09-15 07:07
"""
import socket
import platform
from SkynetLog import skynetLog

log = skynetLog(object_name=__file__).log()

class HostInfo(object):

    os_kernel = platform.release()
    os_name = platform.linux_distribution()[0]
    os_type = platform.system()
    os_version = platform.linux_distribution()[1]
    platform_type = platform.uname()[4]

    def checkReverseLookup(self):
        """
        Check if host fqdn resolves to current host ip and host_name
        """
        try:
            host_name = socket.gethostname().lower()
            host_ip = socket.gethostbyname(host_name)
            host_fqdn = socket.getfqdn().lower()
            fqdn_ip = socket.gethostbyname(host_fqdn)
            if host_ip == fqdn_ip and host_name == host_fqdn:
                return host_name,host_ip
        except socket.error:
            log.error('Check if host fqdn resolves to current host ip and host_name fail.')
            pass
        return None,None

    def get_os_info(self):
        """
        platform system supported_dists: ('SuSE', 'debian', 'fedora', 'redhat', 'centos', 'mandrake',
        'mandriva', 'rocks', 'slackware', 'yellowdog', 'gentoo',) x86 and power
        'UnitedLinux', 'turbolinux'
        http://echorand.me/site/notes/articles/python_linux/article.html
        """

        os_info = {
            'os_kernel'     : self.os_kernel,
            'os_type'       : self.os_type,
            'os_name'       : self.os_name,
            'os_version'    : self.os_version,
            'platform_type'      : self.platform_type,
        }

        return os_info

if __name__ == '__main__':
    host_info = HostInfo()
    print host_info.checkReverseLookup()
    print host_info.get_os_info()