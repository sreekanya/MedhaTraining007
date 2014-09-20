#python script to check if the given user id is valid or not

import re
id_name= raw_input("enter a user id ")
pt = re.compile('^[a-z|A-Z|_]\w*')
match1 = pt.match(id_name)
if match1 != None:
	print ("valid user id")
else: 
	print ("invalid user id")