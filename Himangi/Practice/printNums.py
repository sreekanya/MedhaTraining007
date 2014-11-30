rows = raw_input("Please enter no. of rows")
columns = raw_input("Please enter no. of columns")

def printRC(rows,columns):
    num = int(rows)*int(columns) #to see how many numbers to print
    print num
    s = '' 
    #print "$"*int(rows)
    #for i in range(int(rows)):
        #Def getNum():
            #for i in range(int(columns)):
            #s = s+1
            #print s
    for i in range(1, num+1):
        s = s+str(i)+' '
        if(i%int(columns)==0):
            print s
            s=''

            
    
        
            
printRC(rows,columns)
    

