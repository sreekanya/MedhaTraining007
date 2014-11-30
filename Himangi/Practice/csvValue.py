fileName = raw_input("Please enter the name of CSV file")
fileHandle = open(fileName, 'r')

for i in fileHandle:
   
    myList = i.split(',')
    print myList[2],myList[3]
fileHandle.close()

