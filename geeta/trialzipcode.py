zipInput = raw_input("please enter US Postal code: ")
#zipInput = int(zipInput)
def test(zipInput):
	y = 0
	for i in range(0, len(zipInput)):
		if zipInput[i].isdigit():
			y = y + 1
		else:
			break
	if(y==5):
		print "valid Zip"
	else:
		print "not valid zip"
test(zipInput)
