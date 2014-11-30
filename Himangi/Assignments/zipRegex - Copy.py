import re
zipInput = raw_input("please enter US Postal code: ")
#zipInput = int(zipInput)
pat = re.compile('[0-9][0-9][0-9][1-9][1-9]$')
result = pat.match(zipInput)
print result



