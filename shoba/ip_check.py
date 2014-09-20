# script to validate the ip address

#!/usr/bin/python
import re
import sys

print "the ip adress you entered is ", sys.argv[1]
ip_address = sys.argv[1]
pt = re.compile( '^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'	)
ip_check = pt.match(ip_address)
if ip_check != None:
	print ip_check
	print "valid"
else:
	print ip_check
	print "not valid"