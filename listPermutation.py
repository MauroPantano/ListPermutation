x=0
y=1
z=0
n=0
myList = [x,y,z]
newList = [0,0,0]
finalList = []
counter = 0
exit = False
if(x == 0 and y == 0 and z == 0 and n == 0):
    print(finalList)
elif(x == 0 and y == 1 and z == 0 and n == 0):
    finalList.append(myList)
    print(finalList)
else:
    if(n != x+y+z):
        newListCopy = newList.copy()
        finalList.append(newListCopy)
        while(exit == False):
            if(newList[2] < z):
                newList[2] += 1
                newListCopy = newList.copy()
                finalList.append(newListCopy)
                if(newList[2] == z):
                    if(newList[2] == z and newList[1] == y):
                        if(newList[2] == z and newList[1] == y and newList[0] == x):
                            exit = True
                        else: 
                            newList[2] = 0
                            newList[1] = 0
                            newList[0] += 1
                            newListCopy = newList.copy()
                            finalList.append(newListCopy)
                    else:
                        newList[2] = 0
                        newList[1] += 1
                        newListCopy = newList.copy()
                        finalList.append(newListCopy)
        validList = []
        for perm in finalList:
            if perm[0] >= 0 and perm[0] <= x and perm[1] >= 0 and perm[1] <= y and perm[2] >= 0 and perm[2] <= z:
                validList.append(perm)
        
        sumList = []
        for perm in validList:
            if sum(perm) != n:
                sumList.append(perm)
        
        print(sumList)