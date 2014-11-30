
#print a

def getMin(mylist):
    small = mylist[0]
    smallIndex = 0
    for i in range(len(mylist)):
        if(small>mylist[i]):
            small = mylist[i]
            smallIndex = i
    return(small,smallIndex)

mylist=[1,10,8746,7634,4,-74,-75,-24,7464,746,8738928,736,62,19,784,6466]    

getMin(mylist)
def sort(mylist):
    mySort = []
    for i in range(0,len(mylist)):
        minSort = getMin(mylist)
        mySort.append(minSort[0])
        del mylist[minSort[1]]
    return mySort

print sort(mylist)
        
    

