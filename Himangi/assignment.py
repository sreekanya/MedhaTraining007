### Its always good to write in comments what we are planning to do with this script
### this script is to print multiplication table for number which is passed from command line

import sys

num = sys.argv[1]   # update this line as we are converting to integer before calling writeTab function
# num1 = sys.argv[2]   # we can remove as we are not using this 

print "printing multiplication table for ",num   
#print num1

def writeTab(num):
    for i in range(1,11):
        print num, "*",i, " =", num*i

#num=raw_input("Please type in a number")

num = int(num)
writeTab(num)


