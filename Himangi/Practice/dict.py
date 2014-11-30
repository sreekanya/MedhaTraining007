dict = open("dictCsv.csv")

myDict={}
for i in dict:
    i = i.rstrip()
    students = i.split(',')
    myDict[students[0]] = students[1] + ' ' + students[2]
print myDict
 
    


    
