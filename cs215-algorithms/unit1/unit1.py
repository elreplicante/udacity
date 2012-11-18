'''
Created on 26/06/2012

@author: repli
'''

import math

#def time(n):
#    return 3 + 2 * math.ceil(n/5)

def countdown(x):
    y = 0
    while x > 0:
        x = x - 5
        y = y + 1
    print y

print countdown(50)

def russian(a, b):
    x = a; y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y 
        y = y << 1
        x = x >> 1
    return z

def rec_russian(a, b):
    if a == 0:
        return 0
    if a % 2 == 0:
        return 2 * rec_russian(a/2, b)
    return b + 2 * rec_russian(a - 1 / 2, b)
    

print russian(1000, 123098)

def naive(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        z = z + y
        x = x - 1
    return z

def rec_naive(a, b):
    if a == 0:
        return 0
    return b + rec_naive(a -1, b)

def time(a):
    # The number of steps it takes to execute naive(a, b)
    # as a function of a
    steps = 3 + 2*a
    # your code here
    return steps

rec_naive(17, 6)