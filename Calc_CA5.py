# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 00:45:01 2018

@author: melan
"""

#1
def add(numbers):
    return reduce(lambda x, y: x+y, numbers)

#2          
def divide(numbers):
    return reduce(lambda x, y: x/y, numbers)
    if y == 0:
        return('Divide by 0 not allowed')
            
#3
def exponent(numbers):
    return reduce(lambda x: x**x, numbers)

#4
def multiply(numbers):
    return reduce(lambda x, y: x*y, numbers)

#5
def subtract(numbers):
    return reduce(lambda x, y: x-y, numbers)

#6
def squareRoot(numbers):
    return reduce(lambda x: x**.5, numbers)

#7
def square(numbers):
    return reduce(lambda x: x**2, numbers)

#8
def cube(numbers):
    return reduce(lambda x: x**3, numbers)

#9  
def percentage(numbers):
    return list(map(lambda x, y: x/100*y))
    if x == 0:
        return ('0 is not allowed')
    if y == 0:
        return ('0 is not allowed')

#10
def pythagorus(numbers):
    return list(map(lambda x, y: (x*x) + (y*y)))
    if x == 0:
        return ('0 is not allowed')
    if y == 0:
        return ('0 is not allowed')

