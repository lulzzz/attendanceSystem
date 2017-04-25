#!/usr/bin/env python
#-*- coding: utf-8 -*-

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
		elif i == 11:
			temp.append(':')	
		i += 1

	for t in temp:
		parsed_time += t

	return parsed_time
	
#print return_time_in_normal_form('20170424141025')
