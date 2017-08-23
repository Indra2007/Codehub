try:
    f = open("foo")
except IOError:
    print ("Couldn't open 'foo', sorry")

#The raise Statement
def factorial(n):
    if n < 0:
        raise ValueError("Exepected non-negative number")
    if (n <= 1):
        return 1
    else:
        return n*factorial(n-1)
    

print("Factorial of ", factorial(5))
print("Factorial of ", factorial(-5))
