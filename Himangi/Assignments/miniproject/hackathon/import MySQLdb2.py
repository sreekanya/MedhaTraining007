import MySQLdb
import urllib
import requests
import csv
import sys
import collections
from pprint import pprint
import os
#sys.path.insert(0, 'python{0}/'.format(sys.version_info[0])) 
import mysql.connector
from mysql.connector import errorcode
#import numpy
def fetchCofig():
	configFile="dbConfig.csv"
	fh=open(configFile, 'r')
	#configData=fh.read()
	for i in fh:
		i=i.rstrip()
		configData=i.split(',')
		return configData

a=fetchCofig()
host=a[0]
user=a[1]
password=a[2]
name=a[3]

#print "Server: ",host
#print "User: ",user
#print "password: ",password
#print "name: ",name

try:
	dbvar = MySQLdb.connect(host,user,password,name)
  
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print "Something is wrong with your user name or password"
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print "Database does not exists"
else:
	print(err)
#dbvar = MySQLdb.connect(host,user,password,name)
tablepointer = dbvar.cursor()
#if dbvar:
#	print "connected"
#else:
#	print "not connected"
tablepointer.execute("show global variables like 'port'")
dbs=tablepointer.fetchall()
print "port: ",dbs
#myServerData={}

tablepointer.execute("SELECT table_name, column_name, is_nullable, data_type, column_type, column_key, extra FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'profile'")
schemas=tablepointer.fetchall()
#myschemas=numpy.asarray(schemas)
#print schemas
myDataList=["table_name","column_name","is_nullable","data_type","column_type","column_key","extra"]
serverData={}
for params in schemas:
	#print  params
	tmp.append(params)
	for eachVal in params:
		for colName in myDataList:

	#	print eachVal

#print '\n'
#print (serverData)
print tmp
myCsv = csv.DictReader(open('dbinput.csv','rb'), delimiter=',', quotechar='"')
for i in myCsv:
	myDict = {}
	myDict = i
	print (myDict)

inputFile="dbInput1.csv"
fh = open("dbInput1.csv",'r')
inputData=fh.readlines()
print len(inputData)
tmp1=[]
cnt=0
for h in inputData:
	#print h
	splitH=h.split(',')
	cnt=0
	for s in splitH:
		s=s.rstrip('\n')
		#print s

		tmp1.append(s)
	

#print tmp1
#if tmp in tmp1:
#	print "Elements found"
#else:
#	print "not found"
#tmp2=tmp1
#t=set(tmp1) & set(tmp)
#print t
		#for params in schemas:
			#print  params
		#	for eachVal in params:
				#print eachVal

		#		if eachVal!=s:
		#			print "not matched", eachVal

		#print s
#	for i in schemas:
#		if h[1]==i[8]:
#			print "found",i

#inputData=list(inputData)
#print inputData

#print schemas.length

#for i in range(0,10):
	#print schemas[8]
#	if schemas[i]==inputData[i]:
#		print schemas[i],"found"



#for i in schemas:
#	for params in i:
		

	#print '\n'
#		for eachVal in inputData:
			#print eachVal
#			a=0
#			while a==0:
#				if params == eachVal:
#					print "matched"
#					print params,eachVal
#					a=1
#					break 
			
		#	else:
		#		print "not matched" 
	#print i
#		print '\n'
#if schemas[7]==inputData:
#	print "matched"
#else:
#	print "Not Matched"

tablepointer.execute("show global variables like 'port'")
dbs=tablepointer.fetchall()
print dbs
#tablepointer.execute("show tables")
#tables=tablepointer.fetchall()
#print tables
#tablepointer.execute("select * from profile where name like 'Ryan'")
#data = tablepointer.fetchall()
#print data
