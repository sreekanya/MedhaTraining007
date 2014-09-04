listname=["geeta","shoba","himangi","sreekanya"]
fh = open("hello.log",'w')
fh.write("heoolo this is first write file")
for i in listname:
	fh.write("\n")
	fh.write(i)
fh.close()
