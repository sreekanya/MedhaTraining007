import urllib2
import json
#import requests
import os

# open config.json and read it and save it in list


class Post_data():
	def post_method(self,baseURL,parameters):
		fh=open(parameters,'r')
		for i in fh:
			i=i.rstrip()
			getdata=i.split(',')
			print getdata
			getlist.append(getdata)
		print "parameter list : ",len(getlist)
		
		print baseURL
		for i in range(0,len(getlist)):
			data= {"name":"testwine","year":"1560"}
			r = requests.post(url,data=data)
			baseURL1=baseURL+"?"+"category="+getlist[i][0]+"&"+"merchantId="+getlist[i][1]
			print baseURL1
			f = urllib2.urlopen(baseURL1)
			responsedata = f.read()
			print "Response  ",responsedata
		

