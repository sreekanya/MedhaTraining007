#wap to expalain how the try-except-else work
#in  following prg the prg trys to open the file input.txt with read permission if the file exits it perform command following 
#else statement if there is been an error like(file do not exist)in this case it will throw the error message following  the "except" block ie the it  throw the 
# message that we define and continues the script without stoping or exiting ,.. there is also an option to capture the sys throwing error msg and print the same in except command with syntax 
#( except Exception, e:
#		print str(e)
         

#fh=open("input.txt",'r')
#fh.close
try
	fh=open("input.txt",'r')
except 
		print "file not available"
else:
		print ("continue")