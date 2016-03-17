#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import time

# tick 是什么, 时间间隔为浮点数为秒为单位的数字. 在特定的时间瞬间自上午12时00分, 1970年1月1日(纪元)表示, 单位秒
# Python 中可用的流行时间模块, 它提供功能转换. 该功能 time.time() 返回当前时间, 因为上午 12点, 1970年1月1日(时代)

ticks = time.time()

print "Number of ticks since 12:00am,January 1, 1970 :", ticks

# 日期计算是很容易. 不过当日的时代之前, 不能以这种形式来表示. 在遥远的将来的日期也不能表示这种方式-分界点是一段 2038年 在UNIX 和 Windows


# 什么事TimeTuple
# Python 的时间函数处理时间为 9个数字的元组, 索引代表 0 年 1 月 2 日期 3 小时 4 分钟 5 秒 6 星期 7 一年中的第几天 8 夏时令  

# 属性: tm_year, tm_mom, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst

localtime = time.localtime(time.time())

print "Local current time :", localtime

# Local current time : time.struct_time(tm_year=2016, tm_mon=3, tm_mday=17, tm_hour=17, tm_min=17, tm_sec=30, tm_wday=3, tm_yday=77, tm_isdst=0)


# 获取格式化的时间:
# 可以随时根据要求格式化, 但简单的方法来获取时间, 可读的格式是 asctime()

newlocaltime = time.asctime(localtime)

print "New Local current time :", newlocaltime
# New Local current time : Thu Mar 17 17:21:16 2016 

# 获取日历月份 

import calendar

print localtime[0]; print localtime[1]

year = localtime[0]

mon = localtime[1]
print "Here is the calendar:"
while mon <= 12:
	cal = calendar.month(year,mon)
	print year,mon
	print cal
	mon += 1
	if (mon == 13):
		mon = 1
		year += 1
		while year == 2018:
			exit()	








