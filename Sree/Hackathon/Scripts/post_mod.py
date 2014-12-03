import urllib2
import urllib
import json
#import requests
import os
from urllib2 import Request, urlopen, URLError

# open config.json and read it and save it in list


class Post_data():

#post the data from parameters file to server
	def post_method(self,baseURL,parameters):
		getlist=[]
		fh=open(parameters,'r')
		for i in fh:
			i=i.rstrip()
			getdata=i.split(',')
			print getdata
			getlist.append(getdata)
		print "parameter list : ",len(getlist)
		
		print baseURL
		for i in range(0,len(getlist)):
			post_data_dictionary={'categoryname':getlist[i][0],'merchant':getlist[i][1]}
			print post_data_dictionary
			post_data_encoded = urllib.urlencode(post_data_dictionary)
			#baseURL1=baseURL+"?"+"categoryname="+getlist[i][0]+"&"+"merchant="+getlist[i][1]
			#print baseURL
			request_object = urllib2.Request(baseURL,post_data_encoded)
			try:
				response=urllib2.urlopen(request_object)
			except URLError as e:
							if hasattr(e, 'reason'):
								print 'We failed to reach a server.'
								print 'Reason: ', e.reason
							elif hasattr(e, 'code'):
								print 'The server couldn\'t fulfill the request.'
								print 'Error code: ', e.code
			else: 
				html_string = response.read()
				print "Posted the data to Server : \n",html_string
		

