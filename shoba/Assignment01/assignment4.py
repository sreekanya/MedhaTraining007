#Create python script to check if a zip code is valid USA zip code or not?
#condition - zipcode lenght should be 5 integers,no alphha
# 1. valid zipcode should be 5 digits,
# 2. it should be numbers no alphabets
# 3. should begin with 9.... "this one is not working yet"




import re
def check(zipcode):
	
	if len(zipcode) != 5:
		print "zipcode is not 5 digit"
	else:
		print "valid"



zipcode = raw_input("please enter US Postal code: ")

pt = re.compile('^[1-9]+')
result = pt.match(zipcode)
if result !=None:
    check(zipcode)
else:
    print "invalid zipcode"
	
     

