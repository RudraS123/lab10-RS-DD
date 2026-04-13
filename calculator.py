# https://github.com/RudraS123/lab10-RS-DD
# Partner 1: William Albright
# Partner 2: Adrian Moreno

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
# First example
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

    
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        return "Error: Inputs must be numbers."

def add(a, b): 
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a == 0:
        raise ZeroDivisionError
    else:
        return b / a
import math
# First example
def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
def log(a,b):
    if b == 0 or a == 0:
        raise ValueError
    else:
        return math.log(b,a)
def exp(a,b):
    return a**b
def logarithm(a, b):
    if a == 0 or b == 0:
        raise ValueError
    else:
        return math.log(b, a)
def exponent(a, b):
    return a**b 


