#Conditional Statements
#Indentation is always required in python progrmamming

#n= int(input("Number? "))
n=10
if n < 0:
    print("The absolute value of ", n, "is", -n)
    print("The absolute value of ", n, "is", -n)
    print("The absolute value of ", n, "is", -n)
else:
    print("The absolute value of ", n, "is", n)
    print("The absolute value of ", n, "is", n)
    print("The absolute value of ", n, "is", n)

sumofTwo= 50+60
print("Sum of Two num: ", sumofTwo)




#elif statement and nested if else statement

#name= input("Name? ")
name="indra"
if name=="indra":
    print("The name entered is ", name)
elif name=="john":
    print("The name entered is ", name)  
elif name=="jule":
    print("The name entered is ", name)
else:
     print("The name entered is not valid")


#Nested if else statement
     
name="animal"
animalName="cat"

if name=="animal":
    if animalName=="dog":
        print("Valid animal")
    else:
        print("animal name invalid")
    print("Name entered is animal")
else:
     print("The name entered is not valid")

