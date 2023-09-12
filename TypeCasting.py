"""
There are two types of type casting in python:
1. Implicit type casting
2. Explicit type casting

Implicit type casting - Done by the python interpreter itself
Explicit type casting - Done explicity by the programmer
"""
c = "45"
d = "34.87"
res = int(c) + float(d)
print(type(int(c)))
print(type(float(d)))
print(res)
print(type(res))