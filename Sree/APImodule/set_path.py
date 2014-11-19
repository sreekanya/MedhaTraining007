#! /usr/bin/python

import json

class GetRequest():

	def complete_path(self,configFilename):
		#print "configFileName  : ",configFilename
		with open(configFilename) as data_file:
			data = json.load(data_file)
		print data
		
		server=data[0]["server"]
		pathurl=data[0]["path"]
		port=data[0]["port"]
	
		print "server : ",server," port : ",port," path : ",pathurl
		if(port != ""):
			completeurl = server+':'+port+pathurl
		else:
			self.completeurl = server+pathurl

		return completeurl