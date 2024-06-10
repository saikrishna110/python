"""
WAP to assign 75 and 3.14 values to the variable and constant.
Check the values and type of those after the assignment.
"""
import sys
x=75
Y=3.14
print(type(x))
print(type(Y))

'''
WAP to define one complex number with lower case 'j' and
another one with the upper case 'J'.
Check the values and type of the variables after the assignment.
'''

x=1+6j
y=2+4J
print(x,',',type(x))
print(y,',',type(y))

'''
WAP to assign 99 digits integer number to a variable.
Check the value, size and type of the variable after the assignment.
'''
n=123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789123456789
print(type(n),n)
print(sys.getsizeof(n))