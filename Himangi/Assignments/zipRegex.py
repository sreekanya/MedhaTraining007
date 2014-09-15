import re
zipInput = raw_input("please enter US Postal code: ")
#zipInput = int(zipInput)
pat = re.compile('^(0000[1-9]|000[1-9][0-9]|00[1-9][0-9][0-9]|0[1-9][0-9][0-9][0-9]|[1-9][0-9][0-9][0-9][0-9])$')
result = pat.match(zipInput)
if result:
    print "Valid Zip"
else:
    print "invalid Zip"



