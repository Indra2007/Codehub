#Creating empty list
numList = []

#Creating variable that will control number of countries we can enter
count = 0

biggest_num, smallest_num = 0,0

#Creating the while loop
while count < 5: 
    next = int(input("Please enter a number you've been to >  " ))
    if next > 0 or next <= 0:
        #next = int(inp)
        numList.append(next)
        count = count + 1

print(numList)
length = len(numList)
tempSmallList = [0]
tempBigList = [0]
numTempList = [0]
for i in range(0, len(numList)-1):
    
    if(numList[i] < 0):
        tempSmallList.append(numList.pop(i))
        numTempList = numList
        print("tempSmallList ", tempSmallList)
        print("numList.sort() ", numTempList)
    else:
        if(numList[i] < numList[i+1]):
        #numList.sort()
        #numTempList.sort()
        #print("numList ", numList)
        #print("numTempList ", numTempList)
        #print("numList.sort() ", numList.sort())
    #else:
        #tempBigList = numList.sort()
         
#print("tempSmallList ", tempSmallList, "numTempList ", numTempList , "tempBigList", tempBigList)
        
    
