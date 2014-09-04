listnames = ['geeta','Himangi','Shoba']



fh = open("hello, log",'w')
fh.write("this is my file.")
fh.write("iam adding something")
fh.write( "\n")
for i in listnames:
    fh.write(i)
    fh.write("\n")
fh.close()


