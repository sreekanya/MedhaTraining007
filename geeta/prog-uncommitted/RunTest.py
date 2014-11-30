#/usr/bin/python
import urllib2
import re
import json
import sys


commandLineInputs = sys.argv
expectedDataFileName = ""
configFileName = ""
parameters=""
def checkInputs(commandLineInputs):
	if(len(commandLineInputs)<3):
		print "please enter nessasary inputs.. existing the test....!!! "
		sys.exit()
	else:
		print "processing your data and starting the test..."
	for i in commandLineInputs:
		inputs = i.split('=')
		if(inputs[0]=="expecteddatafile"):
			expectedDataFileName = inputs[1]
		elif(inputs[0]=="config"):
			configFileName = inputs[1]
		else:
			print "unknow parameter... "
		sys.exit()
checkInputs(commandLineInputs)