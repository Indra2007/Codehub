#Recursion:

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    print("Factorial is: ", n)


def factorial_fun_with_while(n):
    fact = 1
    if n == 0:
        return 1
    else:
        while (n > 0):
            fact = fact*n
            n -= 1
    print('The factorial is ', fact)


def factorial_fun_with_for(n):
    fact = 1
    if n == 0:
        return 1
    else:
        for i in range(1, n):
            fact = fact*n
            n -= 1
    print('The factorial is ', fact)
