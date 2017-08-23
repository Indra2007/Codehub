def factorial(number):
    if number==0:
        fact = 1
        print("The factorial of", number, "is", fact)
    else:
        fact = number * (number-1)
        print("The factorial of", number, "is", fact)

def show_tree(t):
    if not t:
        return
    print (t[0])
    print (t[1])
    print (t[2])
    print (t[3])
    
