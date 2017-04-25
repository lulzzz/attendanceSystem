#!/usr/bin/env python
#-*- coding: utf-8 -*-
import datetime

def return_time_in_normal_form(time):
	i = 0
	temp = []
	parsed_time = ""
	while i < len(time):
		temp.append(time[i])
		if i == 3:
			temp.append('/')
		elif i == 5:
			temp.append('/')
		elif i == 7:
			temp.append('/')
		elif i == 9:
			temp.append(':')
		i += 1

	for t in temp:
		parsed_time += t

	return parsed_time

def calc_day_time(arg1, arg2, arg3, arg4):
	
	arg1 = str(arg1)
	arg2 = str(arg2)
	arg3 = str(arg3)
	arg4 = str(arg4)

	arg1 = ((int(arg1[8:10])*60) + (int(arg1[10:12])))*60
	arg2 = ((int(arg2[8:10])*60) + (int(arg2[10:12])))*60
	arg3 = ((int(arg3[8:10])*60) + (int(arg3[10:12])))*60
	arg4 = ((int(arg4[8:10])*60) + (int(arg4[10:12])))*60

	day_time = arg4 - arg1
	lunch = arg3 - arg2
	day_time -= lunch
	
	time_parsed = []
	if day_time < 28800:
		time_parsed.append(day_time)
		time_parsed.append('low')
	else:
		time_parsed.append(day_time)
		time_parsed.append('high')

	#day_time = str(datetime.timedelta(seconds=day_time))
	time_parsed[0] = str(datetime.timedelta(seconds=time_parsed[0]))

	print day_time

	return time_parsed

print calc_day_time(201704230800, 201704231200, 201704231330, 201704231920)
#print return_time_in_normal_form('20170424141025')
