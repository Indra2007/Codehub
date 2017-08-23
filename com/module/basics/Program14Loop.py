#Loops

# while loop
# for loop

a = 0
while a<5:
	print(a)
	a+=1 # a=a+1

a=1
s=0
print("Enter num")
print("Enter 0 to exit ")
while a!=0:
    print('Current sum: ', s)
    a = float(input('Number? '))
    a = float(a)
    s += a
print('Total sum: ', s)

#for loop

b = [3, 4,5,6,7,8,9,1,2]

for num in b:
    print("Number ", num)
