#! /usr/bin/python

import urllib2
import re
import json
import sys
from pprint import pprint 
import os


# open config.json and read it and save it in list

class Get_data():
	expected_keys=''
	
	def open_expected(self,expectedDataFileName):
		
		with open('ExpectedDataFormat.json') as data_file:
			data = json.load(data_file)

		print data[0]
		for key in data[0]:
			print key
		expected_keys=data[0].keys()

		#print list(data[0].keys())

		print "expected data key list",expected_keys

	
	def get_method(self,baseURL,parameters,expectedDataFileName):
		getlist=[]
		self.open_expected(expectedDataFileName)
		fh=open(get.csv,'r')
		for i in fh:
			i=i.rstrip()
			getdata=i.split(',')
			print getdata
			getlist.append(getdata)
		print "parameter list : ",len(getlist)
		
		for i in range(0,len(getlist)):
			baseURL1=baseURL+"?"+"categoryname="+getlist[i][0]+"&"+"merchant="+getlist[i][1]
			print baseURL1
			f = urllib2.urlopen(baseURL1)
			responsedata = f.read()
			print "Response  ",responsedata
			
			
			fh = open('ResponseDataFile.json','a')
			fh.write(responsedata)
			fh.close()
		#print "Response  ",responsedata
		

		# this gives list having dicts

# trying to extract 2 dict and print their keys,from keylistsub....response of one request
	
with open('keylistsub.json') as data1_file:
 	data1 = json.load(data1_file)
print data1[0].keys()
for i in data1[0]:
	print i
print"trying second set", data1[1]
print data1[1].keys()
for i in data1[1]:
	print i
		



