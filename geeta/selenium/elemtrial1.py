
	# finding elements using csv file.
fh=open("elem1.csv",'r')
for i in fh:
	newi = i.rstrip()
	data=newi.split(',')

	import selenium
	from selenium import webdriver
	br=webdriver.Firefox()
	br.get("https://login.yahoo.com")
	br.implicitly_wait(8)
	try:
		result="br."+"find_elements_by_"+data[0]+"("+data[1]+")"
		
	except:
		print data[0],"not found","using",data[1]
	else:
		print data[0],"able to find","using",data[1]