largest = 0
smallest = 0
while True:
    try:
        num = input("Enter a number: ")
        if num == "done":
            break
        print (num)

        num = int(num)

        #for number in range(num):

        if largest == 0 or largest < num:
            largest = num
            #continue
        elif smallest == 0 or smallest > num:
            smallest = num       
    except ValueError:
        print("Please, enter only numbers.")

print ("Maximum", largest)
print ("Minimum", smallest)
