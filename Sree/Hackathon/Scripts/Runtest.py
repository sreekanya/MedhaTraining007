#! /usr/bin/python

import os
import urllib2
import json
import re
import sys

#importing modules and their classes

import get_mod
import set_path
import post_mod
from get_mod import Get_data
from set_path import GetRequest
from post_mod import Post_data

commandLineInputs = sys.argv
expectedDataFileName = ""
configFileName = ""
parameters=""
method=""
env=""

def post_data(env,configFileName,method,parameters):

#Creating 'path' object for GetRequest class which is in set_path module
	path=GetRequest()
	
#calling complete_path method with the path object .
	url=path.complete_path(configFileName)
	print "final url  : ",url
	
#creating object 'p' for Post_data class in post_mod module
	p=Post_data()
	
#calling post_method method with object p
	p.post_method(url,parameters)

def get_req(env,configFileName,method,expectedDataFileName,parameters):
	print "Reading the get data............."
	print "expecteddatafile : ",expectedDataFileName
	print "configFileName  : ",configFileName
	print "parameters  :",parameters
	print "method  : ",method
	print "env  :",env

#Creating 'path' object for GetRequest class which is in set_path module	
	path=GetRequest()
	
#calling complete_path method with the path object .
	url=path.complete_path(configFileName)
	print "final url  : ",url
	
#creating object 'g' for Get_data class in get_mod module	
	g=Get_data()

#calling get_method method with object g	
	g.get_method(url,parameters,expectedDataFileName)

def checkInputs(commandLineInputs):
	if((len(commandLineInputs)==5)or(len(commandLineInputs)==6)):
		for i in commandLineInputs[1:]:
			inputs = i.split('=')
			if(inputs[0]=="-expected"):
				expectedDataFileName = inputs[1]
			elif(inputs[0]=="-config"):
				configFileName = inputs[1]
			elif(inputs[0]=="-env"):
				env=inputs[1]
			elif(inputs[0]=="-method"):
				method=inputs[1]
			elif(inputs[0]=="-parameter"):
				parameters=inputs[1]
			else:
				print "unknown parameter... "
				sys.exit()
	else:
			print """please enter nessasary inputs.. existing the test....!!!  
				-config='ConfigFileName'
				-env='test/dev/prod'
				-method='get/post'
				-parameter='parameter csv file'
				-expected='expected result file for get data' """
			sys.exit()
	
	print "processing your data and starting the test..."

	
	if(method=="get"):
		get_req(env,configFileName,method,expectedDataFileName,parameters)
	if(method=="post"):
		post_data(env,configFileName,method,parameters)
			
	sys.exit()
	
checkInputs(commandLineInputs)