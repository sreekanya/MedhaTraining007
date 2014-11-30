#! /usr/bin/python

import os
import urllib2
import json
import re
import sys
import runtest1.py

commandLineInputs = sys.argv
expectedDataFileName = ""
configFileName = ""
parameters=""
method=""
env=""

def post_data():
	pass

def get_data(env,configFileName,method,expectedDataFileName,parameters):
	print "Reading the get data"
	print "expecteddatafile : ",expectedDataFileName
	print "configFileName  : ",configFileName
	print "parameters  :",parameters
	print "method  : ",method
	print "env  :",env
	
	with open('config.json') as data_file:
 	data = json.load(data_file)
	print data
	server=data[0]["server"]
	port=data[0]["port"]

	print "server :",server
	print "path :", path
	print "port : ",port

	with open('ExpectedDataFormat.json') as data1_file:
	 	data1 = json.load(data1_file)
	print data1
	_id=data1[0]["_id"]
	category=data1[0]["categoryname"]
	merchant=data1[0]["merchant"]
	print _id
	print category
	print merchant
	getlist=[]
	fh=open('get.csv','r')
	for i in fh:
		i=i.rstrip()
		getdata=i.split(',')
		print getdata

	
		
	#read_json()
	

def checkInputs(commandLineInputs):
	if(len(commandLineInputs)<6):
		print "please enter nessasary inputs.. existing the test....!!! "
		sys.exit()
	else:
		print "processing your data and starting the test..."

	for i in commandLineInputs[1:]:
		inputs = i.split('=')
		if(inputs[0]=="-expected"):
			expectedDataFileName = inputs[1]
		elif(inputs[0]=="-config"):
			configFileName = inputs[1]
			#print configFileName
		elif(inputs[0]=="-env"):
			env=inputs[1]
		elif(inputs[0]=="-method"):
			method=inputs[1]
		elif(inputs[0]=="-parameter"):
			parameters=inputs[1]
		else:
			print "unknow parameter... "
			sys.exit()
	if(method=="get"):
		get_data(env,configFileName,method,expectedDataFileName,parameters)
	if(method=="post"):
		post_data()
			
	sys.exit()
checkInputs(commandLineInputs)