import sys

# getting inputs from commond line arguments 
# hello I'm making some changes here
num = int(sys.argv[1])
num1 = int(sys.argv[2])

print num
print num1

def writeTab(num):
    for i in range(1,11):
        print num, "*",i, " =", num*i

#num=raw_input("Please type in a number")

num = int(num)
writeTab(num)









