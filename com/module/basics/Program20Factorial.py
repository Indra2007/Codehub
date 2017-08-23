def factorial(inpVal):
    if isinstance(inpVal, float):
        if inpVal.is_integer() == True:
            fact = calculate(inpVal)
            print('The factorial of number ', inpVal, 'is ', fact)
        else:
            raise ValueError ('factorial() only accepts integral values')
        
    elif isinstance(inpVal, int):
        fact = calculate(inpVal)
        print('The factorial of number ', inpVal, 'is ', fact)

    elif(inpVal.isnumeric() == True) or (inpVal.isdigit() == True):
        print(inpVal)
        inpVar = int(inpVal) + 0
        fact = calculate(inpVar)
        print('The factorial of number ', inpVar, 'is ', fact)

    elif (isinstance(inpVal, str) == True):

        if (inpVal.isalnum() == True):
            raise AttributeError('an int object has no attribute isalpha')
        else:
            inpVar = int(inpVal) + 0
            fact = calculate(inpVar)
            print('The factorial of number ', inpVar, 'is ', fact)
    else:         
         return

#Factorial Calculation      
def calculate(inpVar):
    fact = 1
    if inpVar < 0:
        raise ValueError('Sorry, Factorial does not calculate for negative number')
    elif inpVar <= 1:
        return fact
    else:
        fact = inpVar * calculate(inpVar -1)
        return fact
    
