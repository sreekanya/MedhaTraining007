
zipInput = raw_input("please enter US Postal code: ")
#zipInput = int(zipInput)
def test(zipInput):
	y = 0
	for i in range(0, 5):
		if zipInput[i].isdigit():
			y = y + 1
		else:
			break
	if(y==5):
		print "valid Zip"
	else:
		print "not valid zip"
test(zipInput)

# himangi script copied

# it takes more than 5 digits....all digit zero also says valid.