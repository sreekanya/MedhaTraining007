import urllib2
#import json
baseURL="http://medhaws.cloupapp.net:3000"
getURL = baseURL+'/wines'

f=urllib2.urlopen(getURL)
print f.read()