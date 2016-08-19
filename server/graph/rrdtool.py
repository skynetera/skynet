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
@file: rrdtool.py
@time: 2016-01-05 上午9:31
"""
import commands
import time
import random

import hashrgb


class rrdtool(object):

    def __init__(self,rrd_path):
        self.rrd_path = rrd_path
        self.heartbeat = 120
        self.min = 0
        self.max = 'U'
        self.dst_type='GAUGE'
        self.step = 60
        #1min -- 30*(60/60)=30min -- 60*(60/60)/60=1h -- 120*(60/60)/60=2h -- 6h -- 12h -- 1d -- 7d -- 30d [average、max、min、last]

        self.rra_avg = ('RRA:AVERAGE:0.5:1:600' ,'RRA:AVERAGE:0.5:30:600','RRA:AVERAGE:0.5:60:600' ,'RRA:AVERAGE:0.5:120:600' ,'RRA:AVERAGE:0.5:360:600','RRA:AVERAGE:0.5:3600:600','RRA:AVERAGE:0.5:36000:600','RRA:AVERAGE:0.5:10080:600','RRA:AVERAGE:0.5:43200:730')
        self.rra_max = ('RRA:MAX:0.5:1:600' ,'RRA:MAX:0.5:30:600','RRA:MAX:0.5:60:600' ,'RRA:MAX:0.5:120:600' ,'RRA:MAX:0.5:360:600','RRA:MAX:0.5:3600:600','RRA:MAX:0.5:36000:600','RRA:MAX:0.5:10080:600','RRA:MAX:0.5:43200:730')
        self.rra_min = ('RRA:MIN:0.5:1:600' ,'RRA:MIN:0.5:6:600','RRA:MIN:0.5:12:600' ,'RRA:MIN:0.5:120:600' ,'RRA:MIN:0.5:360:600','RRA:MIN:0.5:3600:600','RRA:MIN:0.5:36000:600','RRA:MIN:0.5:10080:600','RRA:MIN:0.5:43200:730',)
        self.rra_last = ('RRA:LAST:0.5:1:600' ,'RRA:LAST:0.5:6:600','RRA:LAST:0.5:12:600' ,'RRA:LAST:0.5:120:600' ,'RRA:LAST:0.5:360:600','RRA:LAST:0.5:3600:600','RRA:LAST:0.5:36000:600','RRA:LAST:0.5:10080:600','RRA:LAST:0.5:43200:730',)

    def create(self,host_ip, *args):
        ds_info = []
        for ds in args:
            ds_info.append('DS:%s:%s:%s:%s:%s' %(ds,self.dst_type,self.heartbeat,self.min,self.max))
        else:
            body = ' '.join(ds_info)+' '+' '.join(self.rra_avg) +' '+' '.join(self.rra_max)+' '+' '.join(self.rra_min)+' '+' '.join(self.rra_last)

            print '---------%s' %('rrdtool create %s/%s.rrd --step %s %s' %(self.rrd_path,host_ip,self.step,body))

            (status, output) = commands.getstatusoutput('rrdtool create %s/%s.rrd --step %s %s' %(self.rrd_path,host_ip,self.step,body))

            if status!=0:
                return status,output

    def updatev(self,host_ip,data,*args):
        ds_info = []
        for ds in args:
            ds_info.append(ds)
        else:
            result = commands.getstatusoutput("rrdtool updatev %s/%s.rrd --template '%s' %s"%(self.rrd_path,host_ip,':'.join(ds_info),data))
            return result

    def fetch(self,data_type):
        pass
    '''
    1. case 1
    rrdtool fetch 192.168.2.1.rrd AVERAGE --start end-10m --end now

    1. case 2
    rrdtool fetch 192.168.2.1.rrd AVERAGE --start 1452184860 --end now
                cpu_user          cpu_system

    1452184920: 1.0568355950e+00 1.1061702857e+00
    1452184980: 8.9745708892e-01 8.8610856761e-01
    1452185040: 9.4660744581e-01 9.8394254046e-01

    '''

    def rrdtune(self):
        pass
    '''
    rrdtool tune filename
		[--heartbeat|-h ds-name:heartbeat]
		[--data-source-type|-d ds-name:DST]
		[--data-source-rename|-r old-name:new-name]
		[--minimum|-i ds-name:min] [--maximum|-a ds-name:max]
		[--deltapos scale-value] [--deltaneg scale-value]
		[--failure-threshold integer]
		[--window-length integer]
		[--alpha adaptation-parameter]

		[--beta adaptation-parameter]
		[--gamma adaptation-parameter]
		[--gamma-deviation adaptation-parameter]
		[--aberrant-reset ds-name]
    '''

    def graph(self,host_ip,png_name,t,v,*args):

        i =0
        defv = []
        defb = []
        for arg in args:
            i+=1
            defv.append('DEF:value%s=%s.rrd:%s:AVERAGE ' %(i,self.rrd_path+'/'+host_ip,arg))
            defb.append('LINE2:'+'value'+str(i)+''+ hashrgb.str2rgb2(str(arg))+':" ' +arg+ ' "  GPRINT:value1:LAST:"当前\:%8.0lf" GPRINT:value1:AVERAGE:"平均\:%8.0lf" GPRINT:value1:MAX:"最大\:%8.0lf"  GPRINT:value1:MIN:"最小\:%8.0lf"  COMMENT:" \\n" '.replace('value1','value'+str(i)))
        else:
            result_1h = commands.getstatusoutput('rrdtool graph '+str(self.rrd_path+'/'+host_ip+'_'+png_name)+'_1h.png -c SHADEA#DDDDDD -c SHADEB#808080 -c FRAME#006600 -c FONT#555555 -c ARROW#bfbfbf -c AXIS#bfbfbf -c BACK#ffffff -c CANVAS#ffffff ' \
                  '-c MGRID#f5caca -c GRID#d6d6d6    --start now-1h --title "System Load Average" --upper-limit 1 --lower-limit 2 --x-grid MINUTE:1:MINUTE:20:MINUTE:20:0:"%H:%M" -Y -X 0 ' \
                  '--vertical-label "LOAD AVERAGE" --height 300 --width 700 --slope-mode --alt-autoscale -t " '+t+' " -v " '+v+' " '+' '.join(defv)+'  '+' COMMENT:" \\n" '+' '.join(defb)+' HRULE:1#ff0000:"报警值" ' \
                'COMMENT:" \\n" COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t最后更新 \:$(date "+%Y-%m-%d %H\:%M")\\n" -Y COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tskynet监控中心\\n"')

            result_2h = commands.getstatusoutput('rrdtool graph '+str(self.rrd_path+'/'+host_ip+'_'+png_name)+'_2h.png -c SHADEA#DDDDDD -c SHADEB#808080 -c FRAME#006600 -c FONT#555555 -c ARROW#bfbfbf -c AXIS#bfbfbf -c BACK#ffffff -c CANVAS#ffffff ' \
                  '-c MGRID#f5caca -c GRID#d6d6d6    --start now-2h --title "System Load Average" --upper-limit 1 --lower-limit 2 --x-grid MINUTE:5:MINUTE:15:MINUTE:30:0:"%H:%M" -Y -X 0 ' \
                  '--vertical-label "LOAD AVERAGE" --height 300 --width 700 --slope-mode --alt-autoscale -t " '+t+' " -v " '+v+' " '+' '.join(defv)+'  '+' COMMENT:" \\n" '+' '.join(defb)+' HRULE:1#ff0000:"报警值" ' \
                'COMMENT:" \\n" COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t最后更新 \:$(date "+%Y-%m-%d %H\:%M")\\n" -Y COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tskynet监控中心\\n"')

            result_3h = commands.getstatusoutput('rrdtool graph '+str(self.rrd_path+'/'+host_ip+'_'+png_name)+'_3h.png -c SHADEA#DDDDDD -c SHADEB#808080 -c FRAME#006600 -c FONT#555555 -c ARROW#bfbfbf -c AXIS#bfbfbf -c BACK#ffffff -c CANVAS#ffffff ' \
                  '-c MGRID#f5caca -c GRID#d6d6d6    --start now-3h --title "System Load Average" --upper-limit 1 --lower-limit 2 --x-grid MINUTE:5:MINUTE:30:MINUTE:30:0:"%H:%M" -Y -X 0 ' \
                  '--vertical-label "LOAD AVERAGE" --height 300 --width 700 --slope-mode --alt-autoscale -t " '+t+' " -v " '+v+' " '+' '.join(defv)+'  '+' COMMENT:" \\n" '+' '.join(defb)+' HRULE:1#ff0000:"报警值" ' \
                'COMMENT:" \\n" COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t最后更新 \:$(date "+%Y-%m-%d %H\:%M")\\n" -Y COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tskynet监控中心\\n"')

            result_6h = commands.getstatusoutput('rrdtool graph '+str(self.rrd_path+'/'+host_ip+'_'+png_name)+'_6h.png -c SHADEA#DDDDDD -c SHADEB#808080 -c FRAME#006600 -c FONT#555555 -c ARROW#bfbfbf -c AXIS#bfbfbf -c BACK#ffffff -c CANVAS#ffffff ' \
                  '-c MGRID#f5caca -c GRID#d6d6d6    --start now-6h --title "System Load Average" --upper-limit 1 --lower-limit 2 --x-grid MINUTE:10:HOUR:1:HOUR:1:0:"%H:%M" -Y -X 0 ' \
                  '--vertical-label "LOAD AVERAGE" --height 300 --width 700 --slope-mode --alt-autoscale -t " '+t+' " -v " '+v+' " '+' '.join(defv)+'  '+' COMMENT:" \\n" '+' '.join(defb)+' HRULE:1#ff0000:"报警值" ' \
                'COMMENT:" \\n" COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t最后更新 \:$(date "+%Y-%m-%d %H\:%M")\\n" -Y COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tskynet监控中心\\n"')

            result_12h = commands.getstatusoutput('rrdtool graph '+str(self.rrd_path+'/'+host_ip+'_'+png_name)+'_12h.png -c SHADEA#DDDDDD -c SHADEB#808080 -c FRAME#006600 -c FONT#555555 -c ARROW#bfbfbf -c AXIS#bfbfbf -c BACK#ffffff -c CANVAS#ffffff ' \
                  '-c MGRID#f5caca -c GRID#d6d6d6    --start now-12h --title "System Load Average" --upper-limit 1 --lower-limit 2 --x-grid MINUTE:20:HOUR:2:HOUR:2:0:"%H:%M" -Y -X 0 ' \
                  '--vertical-label "LOAD AVERAGE" --height 300 --width 700 --slope-mode --alt-autoscale -t " '+t+' " -v " '+v+' " '+' '.join(defv)+'  '+' COMMENT:" \\n" '+' '.join(defb)+' HRULE:1#ff0000:"报警值" ' \
                'COMMENT:" \\n" COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t最后更新 \:$(date "+%Y-%m-%d %H\:%M")\\n" -Y COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tskynet监控中心\\n"')

            result_1d = commands.getstatusoutput('rrdtool graph '+str(self.rrd_path+'/'+host_ip+'_'+png_name)+'_1d.png -c SHADEA#DDDDDD -c SHADEB#808080 -c FRAME#006600 -c FONT#555555 -c ARROW#bfbfbf -c AXIS#bfbfbf -c BACK#ffffff -c CANVAS#ffffff ' \
                  '-c MGRID#f5caca -c GRID#d6d6d6    --start now-1d --title "System Load Average" --upper-limit 1 --lower-limit 2 --x-grid MINUTE:30:HOUR:2:HOUR:2:0:"%H:%M" -Y -X 0 ' \
                  '--vertical-label "LOAD AVERAGE" --height 300 --width 700 --slope-mode --alt-autoscale -t " '+t+' " -v " '+v+' " '+' '.join(defv)+'  '+' COMMENT:" \\n" '+' '.join(defb)+' HRULE:1#ff0000:"报警值" ' \
                'COMMENT:" \\n" COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t最后更新 \:$(date "+%Y-%m-%d %H\:%M")\\n" -Y COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tskynet监控中心\\n"')

            result_7d = commands.getstatusoutput('rrdtool graph '+str(self.rrd_path+'/'+host_ip+'_'+png_name)+'_7d.png -c SHADEA#DDDDDD -c SHADEB#808080 -c FRAME#006600 -c FONT#555555 -c ARROW#bfbfbf -c AXIS#bfbfbf -c BACK#ffffff -c CANVAS#ffffff ' \
                  '-c MGRID#f5caca -c GRID#d6d6d6    --start now-7d --title "System Load Average" --upper-limit 1 --lower-limit 2 --x-grid DAY:1:DAY:1:DAY:1:0:"星期%a" -Y -X 0 ' \
                  '--vertical-label "LOAD AVERAGE" --height 300 --width 700 --slope-mode --alt-autoscale -t " '+t+' " -v " '+v+' " '+' '.join(defv)+'  '+' COMMENT:" \\n" '+' '.join(defb)+' HRULE:1#ff0000:"报警值" ' \
                'COMMENT:" \\n" COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t最后更新 \:$(date "+%Y-%m-%d %H\:%M")\\n" -Y COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tskynet监控中心\\n"')

            result_30d = commands.getstatusoutput('rrdtool graph '+str(self.rrd_path+'/'+host_ip+'_'+png_name)+'_30d.png -c SHADEA#DDDDDD -c SHADEB#808080 -c FRAME#006600 -c FONT#555555 -c ARROW#bfbfbf -c AXIS#bfbfbf -c BACK#ffffff -c CANVAS#ffffff ' \
                  '-c MGRID#f5caca -c GRID#d6d6d6    --start now-30d --title "System Load Average" --upper-limit 1 --lower-limit 2 --x-grid DAY:5:DAY:5:DAY:5:0:"%b%d日" -Y -X 0 ' \
                  '--vertical-label "LOAD AVERAGE" --height 300 --width 700 --slope-mode --alt-autoscale -t " '+t+' " -v " '+v+' " '+' '.join(defv)+'  '+' COMMENT:" \\n" '+' '.join(defb)+' HRULE:1#ff0000:"报警值" ' \
                'COMMENT:" \\n" COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t最后更新 \:$(date "+%Y-%m-%d %H\:%M")\\n" -Y COMMENT:"\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t\\tskynet监控中心\\n"')

            print result_1h,result_2h,result_3h,result_6h,result_12h,result_1d,result_7d,result_30d


if __name__ == '__main__':
    rrdtool = rrdtool(rrd_path='/home/whoami/py/SkynetEye/monitor/rrd')
    args = 'cpu_user','cpu_system'
    # rrdtool.create('192.168.2.2',*args)
    while 1:
        starttime=time.time()
        a = random.uniform(0,1.1)
        b = random.uniform(0,1.1)
        print a,b
        data = '%s:%s:%s'%(starttime,a,b)
        print rrdtool.updatev('192.168.2.1',data,*args)
        starttime+=60
        time.sleep(2)

        rrdtool.graph('192.168.2.1','cpu','服务器CPU统计信息','cpu load',*args)