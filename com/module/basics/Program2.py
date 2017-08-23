# Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 18:41:36) [MSC v.1900 64 bit (AMD64)] on win32
# Type "copyright", "credits" or "license()" for more information.
# >>>
# myVariable = 30
# >>> myVariable
# 30
# >>> myVariable **3
# 27000
# >>> value = input("Enter the value:
# 	      ")
#
# SyntaxError: EOL while scanning string literal
# >>> value = input("Enter the value:")
# Enter the value:50
# >>> value
# '50'
# >>> value + 20
# Traceback (most recent call last):
#   File "<pyshell#6>", line 1, in <module>
#     value + 20
# TypeError: must be str, not int
# >>> value =int (input("Enter the value:"))
# Enter the value:50
# >>> value
# 50
# >>> value + 20
# 70
# >>>
# value + 50+60
# 160
# >>>
# >>> value = float(input("Enter the value"))
# Enter the value50.6
# >>> value
# 50.6
# >>>
# >>>
# >>>
# 2 **3
# 8
# >>>
# >>> pow(2, 3)
# 8
# >>> dir(__builtins__)
# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
# >>> abs(18.55555)
# 18.55555
# >>> len("hello")
# 5
# >>> min(10)
# Traceback (most recent call last):
#   File "<pyshell#22>", line 1, in <module>
#     min(10)
# TypeError: 'int' object is not iterable
# >>> help(ascii)
# Help on built-in function ascii in module builtins:
#
# ascii(obj, /)
#     Return an ASCII-only representation of an object.
#
#     As repr(), return a string containing a printable representation of an
#     object, but escape the non-ASCII characters in the string returned by
#     repr() using \\x, \\u or \\U escapes. This generates a string similar
#     to that returned by repr() in Python 2.
#
# >>> help(max)
# Help on built-in function max in module builtins:
#
# max(...)
#     max(iterable, *[, default=obj, key=func]) -> value
#     max(arg1, arg2, *args, *[, key=func]) -> value
#
#     With a single iterable argument, return its biggest item. The
#     default keyword-only argument specifies an object to return if
#     the provided iterable is empty.
#     With two or more arguments, return the largest argument.
#
# >>> max(19, 56,89)
# 89
# >>>
# >>> import math
# >>> math.factorial
# <built-in function factorial>
# >>> math.factorial(5)
# 120
# >>> math.sqrt(5)
# 2.23606797749979
# >>> math.sqrt(16)
# 4.0
# >>> math.sqrt(9)
# 3.0
# >>> math.trunc(19:199)
# SyntaxError: invalid syntax
# >>> help(trunc)
# Traceback (most recent call last):
#   File "<pyshell#34>", line 1, in <module>
#     help(trunc)
# NameError: name 'trunc' is not defined
# >>> help(trunc)
# Traceback (most recent call last):
#   File "<pyshell#35>", line 1, in <module>
#     help(trunc)
# NameError: name 'trunc' is not defined
# >>> squareRoot = math.sqrt
# >>> squareRoot(9)
# 3.0
# >>> help(trunc)
# Traceback (most recent call last):
#   File "<pyshell#38>", line 1, in <module>
#     help(trunc)
# NameError: name 'trunc' is not defined
# >>> help(trunc())
# Traceback (most recent call last):
#   File "<pyshell#39>", line 1, in <module>
#     help(trunc())
# NameError: name 'trunc' is not defined
# >>>
# >>>
# >>>
# >>>
# >>>
