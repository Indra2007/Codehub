# In built function

type(32)
# Output: <class 'int'>
type('Indra')
# Output: <class 'str'>
type(45.00)
# Output: <class 'float'>
type('c')
# Output: <class 'str'>
type(True)
# Output: <class 'bool'>
type(False)
# Output: <class 'bool'>
type(object)
# Output: <class 'type'>



# Type conversion functions

import random

for i in range (10):
	x = random.random()
	print(x)





def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

print()

repeat_lyrics()


def add_two(a, b):
    added = a + b
    return added

x = add_two(3, 5)
print(x)

def sub_two(a, b):
    if a > b:
        subtracted = a - b
    else:
        subtracted = b - a
    return subtracted

x = sub_two(8, 9)
print(x)

def fred():
    print("Zap")
    
def jane():
    print("ABC")

jane()
fred()
jane()
