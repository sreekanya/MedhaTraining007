#python script to check if entered email id is valid or not
import re
#accepting email id from user


emailAddress = (raw_input("enter a  email id")

pt4 = re.compile('[a-z]+[0-9]*[a-z]*@[a-z]+\.com$')  ### shoba12srinath@gmail.com or shoba12@gmail.com or shoba@yahoo.com 

## shoba.srinath@gmail.com
## shoba_srinath@gmail.com
## shoba.srinath2003@gmail.com
## shoba_srinath2003@gmail.com


check4 = pt4.match(emailAddress)

if(check4 != None):
	print emailAddress," is a valid email adddress"



