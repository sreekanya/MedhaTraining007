# this script to check if a number is even or odd

def oddEven():
    if(int(numInput)%2!= 0):
        print numInput," is an odd number"
    else:
        print numInput," is an even number"

numInput = raw_input("Please type in a number: ")   
oddEven(numInput)
