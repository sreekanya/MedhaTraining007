import urllib2
import json
import re
baseURL = "http://medhaws.cloudapp.net:3000"
getURL = baseURL +'/wines'
f = urllib2.urlopen("http://medhaws.cloudapp.net:3000/wines")
responseData = f.read()
fh = open('response.txt','w')
fh.write(responseData)
fh.close()
pt = re.compile("\s*\"(_id)\":\s*\"(\w*)\"\s*")
#pat = re.compile("\s*\"(\w*)\":\s*\"([\w\s.]*)\"")
#patP = re.compile("\s*\{\s*[\s*\"\w*\":\s\"\w*\/*\.*\",\s*]*\s*\}\s*")
patP = re.compile('\s+\"(.*?)\":\s+\"(.*?)\"')
#patparaR = re.compile("\s*\{\s*")
rf = open('response.txt','r')
tmp = {}
#data = rf.read()
#data=str(data)
#m=0
catValue = 'France'
cat = 'country'
#matchId=patP.match(data)
for line in rf:
	matchId=pt.match(line)
	if matchId:
		if cat in tmp.keys():
			if(tmp[cat] == catValue):
				for key in tmp:
					print key,tmp[key]
				print "___________________________________"
				print "\n"		
		tmp = {}

		tmp[matchId.groups()[0]]=matchId.groups()[1]
	matchNext = patP.match(line)
	if matchNext:
		tmp[matchNext.groups()[0]]=matchNext.groups()[1]	
		
		





			


