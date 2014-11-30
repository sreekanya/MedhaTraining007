totalMarks = open("marksCsv.csv")
for i in totalMarks:
    studentRec = i.split()
    #print studentRec
    total = 0
    for j in range(1,len(studentRec)):
        total = total +  int(studentRec[j])

        
    studName = studentRec[0]
    print "total of ", studName,"is", total
    
        
    #names = studentRec [0]
    #listofnames = studentRec[0]
    
    #print listofnames[2]
    
    
   
    
    
 
totalMarks.close()
