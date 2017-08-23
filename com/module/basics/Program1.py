# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
# Type "copyright", "credits" or "license()" for more information.
# >>> print ("Indra is Good Person")
# Indra is Good Person
# >>> names {}
# SyntaxError: invalid syntax
# >>> names ['Indra', 'Rashmi', 'Rachit']
# Traceback (most recent call last):
#   File "<pyshell#2>", line 1, in <module>
#     names ['Indra', 'Rashmi', 'Rachit']
# NameError: name 'names' is not defined
# >>> names = ['Indra', 'Rashmi', 'Rachit']
# >>> print (names)
# ['Indra', 'Rashmi', 'Rachit']
# >>> print names.sorted
# SyntaxError: Missing parentheses in call to 'print'
# >>> print names.sort()
# SyntaxError: invalid syntax
# >>> print (names.sort())
# None
# >>> print("Names: ", names)
# Names:  ['Indra', 'Rachit', 'Rashmi']
# >>> name.sort()
# Traceback (most recent call last):
#   File "<pyshell#9>", line 1, in <module>
#     name.sort()
# NameError: name 'name' is not defined
# >>> names.sort()
# >>> print ("Names: "
#
#        , names);
# Names:  ['Indra', 'Rachit', 'Rashmi']
# >>> 3 + 5
# 8
# >>> 3 _ 2
# SyntaxError: invalid syntax
# >>> 3-2
# 1
# >>> 3*4
# 12
# >>> 3**2
# 9
# >>> 3***3
# SyntaxError: invalid syntax
# >>> 3**3
# 27
# >>> 4+9*(27)
# 247
# >>> names.sort(key=lambda x: x[1:])
# print("Names: ", names)
# SyntaxError: multiple statements found while compiling a single statement
# >>> names.sort(key=lambda x: x[1:])
# >>> print("Names: ", names)
# Names:  ['Rachit', 'Rashmi', 'Indra']
# >>> 'Hello ' + 'India'
# 'Hello India'
# >>> 'Hello\n ' + 'India'
# 'Hello\n India'
# >>> 'Hello' + \n'India'
# SyntaxError: unexpected character after line continuation character
# >>> 'Hello' + \t'India'
# SyntaxError: unexpected character after line continuation character
# >>> 'Hello' +'\tIndia'
# 'Hello\tIndia'
# >>> a = 4<< 3
# >>> b= a * 4.5
# >>> c = (a + b)/2.5
# >>> str = 'hello india'
# >>> #compute maximum of z
# >>> #compute maximum z of a and b
# >>> if(a < b):
# 	z = b
# else:
# 	z = a
#
#
# >>> if (a < b):
# 	pass
# else:
# 	z = a
#
#
# >>> print z
# SyntaxError: Missing parentheses in call to 'print'
# >>> print(z)
# 144.0
# >>> print(c)
# 70.4
# >>> print(a)
# 32
# >>> print(b)
# 144.0
# >>> if (a < b):
# 	pass
# 	print("Do nothing")
# 	else:
#
# SyntaxError: invalid syntax
# >>> a = 3
# >>> b = 6
# >>> if(a < b):
# 	pass
# else:
# 	print("Do something")
# 	print("Not in above blocks")
#
#
# >>> print(a)
# 3
# >>> ds
# Traceback (most recent call last):
#   File "<pyshell#64>", line 1, in <module>
#     ds
# NameError: name 'ds' is not defined
# >>> if a == '+'
# SyntaxError: invalid syntax
# >>> if a == '+':
# 	op = PLUS
# 	elseif a == '-'
#
# SyntaxError: invalid syntax
# >>> if a == '+': op = PLUS
# elif a == '-': op = MINUS
# elif a == '*': op = MULTIPLY
# elif a == '/': op = DIVISION
# else op = UNKNOWN
# SyntaxError: invalid syntax
# >>> if a == '+': op = PLUS
# elif a == '-': op = MINUS
# elif a == '*': op = MULTIPLY
# elif a == '/': op = DIVISION
# else: op = UNKNOWN
#
# Traceback (most recent call last):
#   File "<pyshell#78>", line 5, in <module>
#     else: op = UNKNOWN
# NameError: name 'UNKNOWN' is not defined
# >>>
# # There is no switch condition
# >>>
# >>>
# >>> if (b >=a and b <= c):
# 	print "b is between a and c"
#     if not (b < a or b > c):
#
# SyntaxError: Missing parentheses in call to 'print'
# >>> if (b >=a and b <= c):
# 	print("b is between a and c")
#     if not (b < a or b > c):
#
# SyntaxError: unindent does not match any outer indentation level
# >>> if (b >=a and b <= c):
# 	print("b is between a and c")
#     if not (b < a or b > c):
#
# SyntaxError: unindent does not match any outer indentation level
# >>> if (b >=a and b <= c):
# 	print("b is between a and c")
# 	    if not (b < a or b > c):
#
# SyntaxError: unexpected indent
# >>> if (b >=a and b <= c):
# 	print("b is between a and c")
# 	if not (b < a or b > c):
# 		print("b is still between a & c")
#
#
# b is between a and c
# b is still between a & c
# >>> if a == '+': op = PLUS
# elif a == '-': op = MINUS
# elif a == '*': op = MULTIPLY
# elif a == '*': op = MULTIPLY
# else: op = UNKNOWN
#
# Traceback (most recent call last):
#   File "<pyshell#98>", line 5, in <module>
#     else: op = UNKNOWN
# NameError: name 'UNKNOWN' is not defined
# >>> if a == '+': op = PLUS
# elif a == '-': op = MINUS
# elif a == '*': op = MULTIPLY
# elif a == '*': op = MULTIPLY
# else: op = UNKNOWN
# print("Not evalauted")
# SyntaxError: invalid syntax
# >>>
# >>>
# >>>
# >>>
# >>> a = 3
# >>> b = 6.4
# >>> c = 517288833333L
# SyntaxError: invalid syntax
# >>> c = 517288833333
# >>> d = 3 + 4j
# >>>
# >>>
# >>> # Strings Example
# >>>
# >>> a = 'Indra'
# >>> b = " is human"
# >>> c = "I am a 'software engineer' "
# >>> d = ''' A triple quoted string strig
# can span multiple line
# like this'''
# >>> e = """Also works for double quotes"""
# >>> print(e)
# Also works for double quotes
# >>> f = 'f'
# >>> print f
# SyntaxError: Missing parentheses in call to 'print'
# >>> print 'f'
# SyntaxError: Missing parentheses in call to 'print'
# >>> print ('f')
# f
# >>> f = 'foo'
# >>> print(f)
# foo
# >>> q = Queen
# Traceback (most recent call last):
#   File "<pyshell#128>", line 1, in <module>
#     q = Queen
# NameError: name 'Queen' is not defined
# >>> q = 'Queen'
# >>> print('Alizabedh is a ', q)
# Alizabedh is a  Queen
# >>> # List of arbitrary objects
# >>> a = [1, 2, 3] # lists of integers
# >>> b = [1, 2, 3, 'Indra', 'c', "Gupta", "is a software engineer"]
# >>> C = []
# >>> d = [c, [a, b]]
# >>> d = [c, [a, b]] # A list containing a list
# >>> e = a + b
# >>> e = a + b # Join two lists or arrays
# >>> # A list manipulation
# >>> x = a [1]
# >>> print (x)
# 2
# >>> y = b[1:3]
# >>> print(y)
# [2, 3]
# >>> y = b[1:3] # Return a sublist
# >>> print (y)
# [2, 3]
# >>> y = b[2:4]
# >>> print (y)
# [3, 'Indra']
# >>> y = b[0:2]
# >>> print (y)
# [1, 2]
# >>> y = [0:3]
# SyntaxError: invalid syntax
# >>> y = b[0:3]
# >>> print (y)
# [1, 2, 3]
# >>> y = b[2:7]
# >>> print (y)
# [3, 'Indra', 'c', 'Gupta', 'is a software engineer']
# >>> y = b [4:7]
# >>> print (y)
# ['c', 'Gupta', 'is a software engineer']
# >>> y = b[3:7]
# >>> print (y)
# ['Indra', 'c', 'Gupta', 'is a software engineer']
# >>> b[0] = 42
# >>> print (b)
# [42, 2, 3, 'Indra', 'c', 'Gupta', 'is a software engineer']
# >>> # tuples
# >>> f = (2, 3, 4, 5)
# >>> g = (,)
# SyntaxError: invalid syntax
# >>> g = ()
# >>> g = () #empty tuples
# >>> h = (2, [4, 4], (10, 11, 13)) # A tuple containing mixed objects
# >>> x = f[1]
# >>> print (x)
# 3
# >>> y = f [1:3]
# >>> print (y)
# (3, 4)
# >>> z = h [1][1]
# >>> print(z)
# 4
# >>> z1  = h [1][2]
# Traceback (most recent call last):
#   File "<pyshell#173>", line 1, in <module>
#     z1  = h [1][2]
# IndexError: list index out of range
# >>> w = h [1][2]
# Traceback (most recent call last):
#   File "<pyshell#174>", line 1, in <module>
#     w = h [1][2]
# IndexError: list index out of range
# >>> w = h [2][1]
# >>> print w
# SyntaxError: Missing parentheses in call to 'print'
# >>> print(w)
# 11
# >>> t = h [2][2]
# >>> print(t)
# 13
# >>>
# >>> s = h [0][0]
# Traceback (most recent call last):
#   File "<pyshell#181>", line 1, in <module>
#     s = h [0][0]
# TypeError: 'int' object is not subscriptable
# >>> s = h [0]
# >>> print(s)
# 2
# >>> #Tuples are like lists, but size is fixed at time of creation.
# >>> #Can’t replace members (said to be "immutable")
# >>>
# >>>
# >>>
# >>> #Dictionaries (Associative Arrays)
# >>>
# >>> a = {}
# >>> #above is empty dictioanry
# >>> #dictionary
# >>>
# >>> b = {'x': 3, 'y': 4}
# >>> c = { 'uid': 105,
#       'login': 'Indra',
#       'name': 'Indramani Gupta'
#       }
# >>>
# >>> #Dictionary Access
# >>> u = c ['uid'] # get an element
# >>> print (u)
# 105
# >>> v = c ['login']
# >>> print (v)
# Indra
# >>> w = c['name']
# >>> print (w)
# Indramani Gupta
# >>> d = c.get("directory", None)
# >>> print(d)
# None
# >>>
# >>>
# >>> #Loops
# >>>
# >>> while a < b:
# 	a = a + 1
# 	print (a)
#
#
# Traceback (most recent call last):
#   File "<pyshell#217>", line 1, in <module>
#     while a < b:
# TypeError: '<' not supported between instances of 'dict' and 'dict'
# >>> m = 2
# >>> n = 5
# >>> while m < n:
# 	m = m +1
# 	print(m)
#
#
# 3
# 4
# 5
# >>>
# >>>
# >>> #Now for loops
# >>>
# >>>
# >>>  *-  #Now for loops
#
# SyntaxError: unexpected indent
# >>>
# >>> #Now for loops
# >>>
# >>> for i in [101, 305, 407]
# SyntaxError: invalid syntax
# >>> for i in [102, 306, 408]:
# 	ptint(i)
#
#
# Traceback (most recent call last):
#   File "<pyshell#236>", line 2, in <module>
#     ptint(i)
# NameError: name 'ptint' is not defined
# >>> for i in [102, 306, 408]:
# 	print(i)
#
#
# 102
# 306
# 408
# >>>
# >>>
# >>> for c in 'hello world':
# 	print(c)
#
#
# h
# e
# l
# l
# o
#
# w
# o
# r
# l
# d
# >>> for c in ('indramanai')
# SyntaxError: invalid syntax
# >>> for c in 'Indramani Gupta':
# 	print(c)
#
#
# I
# n
# d
# r
# a
# m
# a
# n
# i
#
# G
# u
# p
# t
# a
# >>> for c in "Hello":
# 	print(c)
#
#
# H
# e
# l
# l
# o
# >>> for c in "Hello", "Indra":
# 	print (c[1])
#
#
# e
# n
# >>> print (c[0])
# I
# >>> for c in 'India', 'is', 'my', 'great', 'country':
# 	print(c)
#
#
# India
# is
# my
# great
# country
# >>> names ['Indra', 'Rashmi', 'Rachit', 'India', 'is', 'my', 'great', 'country']
# Traceback (most recent call last):
#   File "<pyshell#259>", line 1, in <module>
#     names ['Indra', 'Rashmi', 'Rachit', 'India', 'is', 'my', 'great', 'country']
# TypeError: list indices must be integers or slices, not tuple
# >>> names = ['Indra', 'Rashmi', 'Rachit', 'India', 'is', 'my', 'great', 'country']
# >>> for c in names.len():
# 	print(names[c])
#
#
# Traceback (most recent call last):
#   File "<pyshell#263>", line 1, in <module>
#     for c in names.len():
# AttributeError: 'list' object has no attribute 'len'
# >>> for c in names.length():
# 	print(names[c])
#
#
# Traceback (most recent call last):
#   File "<pyshell#266>", line 1, in <module>
#     for c in names.length():
# AttributeError: 'list' object has no attribute 'length'
# >>> for c in names.len():
# 	print(name[c])
#
#
# Traceback (most recent call last):
#   File "<pyshell#269>", line 1, in <module>
#     for c in names.len():
# AttributeError: 'list' object has no attribute 'len'
# >>> for c in names
# SyntaxError: invalid syntax
# >>> for c in names:
# 	print(names[c])
#
#
# Traceback (most recent call last):
#   File "<pyshell#273>", line 2, in <module>
#     print(names[c])
# TypeError: list indices must be integers or slices, not str
# >>> print c
# SyntaxError: Missing parentheses in call to 'print'
# >>> print(c)
# Indra
# >>> for c in names:
# 	print(c)
#
#
# Indra
# Rashmi
# Rachit
# India
# is
# my
# great
# country
# >>> for i in range(0,100):
# 	print(i)
#
#
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# 21
# 22
# 23
# 24
# 25
# 26
# 27
# 28
# 29
# 30
# 31
# 32
# 33
# 34
# 35
# 36
# 37
# 38
# 39
# 40
# 41
# 42
# 43
# 44
# 45
# 46
# 47
# 48
# 49
# 50
# 51
# 52
# 53
# 54
# 55
# 56
# 57
# 58
# 59
# 60
# 61
# 62
# 63
# 64
# 65
# 66
# 67
# 68
# 69
# 70
# 71
# 72
# 73
# 74
# 75
# 76
# 77
# 78
# 79
# 80
# 81
# 82
# 83
# 84
# 85
# 86
# 87
# 88
# 89
# 90
# 91
# 92
# 93
# 94
# 95
# 96
# 97
# 98
# 99
# >>> for i in range(0,10):
# 	print(i+2)
#
#
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# >>>
# >>>
# >>>
# >>> #Functions
# >>>
# >>> #The def statement
# >>> # Return the reminder of a/b
# >>>
# >>> def remainder(a, b):
# 	q = a/b
# 	r = a - q*b
# 	return r
# #Now use it
# a = remainder(42, 5)
# SyntaxError: invalid syntax
# >>> a = remainder(42, 5)
# Traceback (most recent call last):
#   File "<pyshell#298>", line 1, in <module>
#     a = remainder(42, 5)
# NameError: name 'remainder' is not defined
# >>> def remainder(a, b):
# 	q = a/b
# 	r = a - q*b
# 	return r
#
# >>> #Now use it
# >>> a = remainder(42, 5)
# >>> print (a)
# 0.0
# >>> def remainder(a, b):
# 	q = a/b
# 	r = a - q*b
# 	return r
# a = remainder(42, 5)
# SyntaxError: invalid syntax
# >>> def remainder(a, b):
# 	q = a/b
# 	r = a - q*b
# 	return r
# print(r)
# SyntaxError: invalid syntax
# >>> def remainder(a, b):
# 	q = a/b
# 	r = a - q*b
# 	return r
#
# >>> print(remainder(42,5))
# 0.0
# >>> print(remainder(53,5))
# 0.0
# >>> def divide(a,b):
# 	q = a/b
# 	r = a - q*b
# 	return r
#
# >>> print (x,y = divide(42,5))
# Traceback (most recent call last):
#   File "<pyshell#318>", line 1, in <module>
#     print (x,y = divide(42,5))
# TypeError: 'y' is an invalid keyword argument for this function
# >>> def divide(a,b):
# 	q = a/b
# 	r = a - q*b
# 	return q, r
#
# >>> print (x,y = divide(42,5))
# Traceback (most recent call last):
#   File "<pyshell#321>", line 1, in <module>
#     print (x,y = divide(42,5))
# TypeError: 'y' is an invalid keyword argument for this function
# >>> x,y = divide(42,5)
# >>> print (x,y)
# 8.4 0.0
# >>> prit(x)
# Traceback (most recent call last):
#   File "<pyshell#324>", line 1, in <module>
#     prit(x)
# NameError: name 'prit' is not defined
# >>> print(x)
# 8.4
# >>> print(y)
# 0.0
# >>>
