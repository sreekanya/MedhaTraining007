rows = raw_input("Please enter no. of rows")
columns = raw_input("Please enter no. of columns")
def printRC(rows,columns):
    #num = int(rows)*int(columns) to see how many numbers to print
    #print "$"*int(rows)
    for i in range(int(columns)):
        print "$ "*int(rows)
printRC(rows,columns)
    

