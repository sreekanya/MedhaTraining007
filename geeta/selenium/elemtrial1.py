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
		yahooid=br.find_element_by_data[0](data[1])
	except:
		print data[0],"not found"
	else:
		print "able to find"
	