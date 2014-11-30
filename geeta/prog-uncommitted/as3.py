# to check given no is betn 99 and 999 or no.
a=int(raw_input("Enter the number:"))
if ( a<999 ) :
	if ( a>99 ) :
		print "number is between 99 and 999"
	else :
		print "number is less than 99"
else :
	print "number is more than 999"
