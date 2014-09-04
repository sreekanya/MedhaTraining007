rows = raw_input("Please Enter Number of Rows ")
cols = raw_input("Please Enter Number of columns ")
rows =int(rows)
cols=int(cols)



a=1
for i in range(1, rows+1):
    count = ''
    for i in range(1, cols+1):
       
        count = count+str(a)+' '
        a = a+1
    print count

        
      
            
        
    

