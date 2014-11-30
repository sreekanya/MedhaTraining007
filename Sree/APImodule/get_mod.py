#! /usr/bin/python

import urllib2
import re
import json
import sys 
import os
from urllib2 import Request, urlopen, URLError


class Get_data():

#This method opens the expectedDataFileName and saves the keys in the list called expected_keys
	def open_expected(self,expectedDataFileName):
		expected_keys=[]
		
		with open('ExpectedDataFormat.json') as data_file:
			data = json.load(data_file)

		print data[0]
		#for key in data[0]:
		#	print key
		expected_keys=list(data[0].keys())

		#print list(data[0].keys())

		print "expected data key list",expected_keys
		return expected_keys
		
	def get_method(self,baseURL,parameters,expectedDataFileName):
		getlist=[]
		expected_keys=[]
		expected_keys=self.open_expected(expectedDataFileName)
		
# opens parameters file and saves the data in getlist 
		fh=open(parameters,'r')
		for i in fh:
			i=i.rstrip()
			getdata=i.split(',')
			print getdata
			getlist.append(getdata)
		print "parameter list : ",len(getlist)
		
		print "Expected data key list lenght",expected_keys,len(expected_keys)
		
#Opening a ResponseDataFile in write mode
		fh = open('ResponseDataFile.json','w')
		for i in range(0,len(getlist)):

#constructs the url		
			baseURL1=baseURL+"?"+"categoryname="+getlist[i][0]+"&"+"merchant="+getlist[i][1]
			print baseURL1
			req = Request(baseURL1)
			
#Catches the Exception if any raised in connecting to the server
			try:
				response = urlopen(req)
			except URLError as e:
				if hasattr(e, 'reason'):
					print 'We failed to reach a server.'
					print 'Reason: ', e.reason
				elif hasattr(e, 'code'):
					print 'The server couldn\'t fulfill the request.'
					print 'Error code: ', e.code
			else:
			
#The URL and the response from server writes to the file ResponseDataFile which is already opened
				fh.write(baseURL1)
				
				responsedata = response.read()
				
				fh.write(responsedata)
				
#Converts the Json format string which is read from the server to a list
				result=json.loads(responsedata)
				print "Result : \n",responsedata
				print "Lenght of Response : ",len(result)
				
#Compares the data from result list with expected_keys and writes to the file Result passed or failed
				for i in range(0,len(result)):					
					result_keys=result[i].keys()
					print "result keys : \n",result_keys
					print len(expected_keys)
					count=0
					for j in range(0,len(expected_keys)):
						print "inside expected keys"
						flag=0
						
						for k in range(0,len(result_keys)):
							print "inside result keys"
							if(expected_keys[j]==result_keys[k]):
							   count=count+1
							   flag=1
							   break
						print "count and flag",count,flag
					if(count==len(expected_keys)):
						fh.write("Result Passed")
						print "Passed"
					else:
						fh.write("Result Failed")
			
		fh.close()
						

			
