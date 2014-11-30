

    #nextrow = raw_input("Please enter number of rows to print: ")
    #char = raw_input("Please enter a charactor to print: ")
def order():
    nextrow = 1
    while(nextrow>0):
        char = raw_input("Please enter a charactor to print: ")
        nextrow = raw_input("Please enter number of rows to print or 0 to Exit: ")
        nextrow = int(nextrow)
        for i in range(1, nextrow+1):            
            print char*i                         
       
order()
