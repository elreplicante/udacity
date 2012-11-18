'''
Created on 02/09/2012

@author: repli
'''


# CORRECT SPECIFICATION:
#
# isPrime checks if a positive integer is prime.
#
# A positive integer is prime if it is greater than 
# 1, and its only divisors are 1 and itself.
#
# TASKS:
#
# 1) Add an assertion to test() that shows
#    isPrime(number) to be incorrect for 
#    some input.
#
# 2) Write isPrime2(number) to correctly 
#    check if a positive integer is prime.

import math

def isPrime(number):
    if number == 2:
        return True
    if number<=1 or (number%2)==0:
        return False
    for check in range(3,int(math.sqrt(number)) + 1):  
        if (number%check) == 0:  
            return False
    return True

def isPrime2(number):  
    ###Your isPrime2 code here.

    pass

def test_prime():
    assert isPrime(1) == False
    assert isPrime(2) == True
    assert isPrime(3) == True
    assert isPrime(4) == False
    assert isPrime(5) == True
    assert isPrime(20) == False
    assert isPrime(21) == False
    assert isPrime(22) == False
    assert isPrime(23) == True
    assert isPrime(24) == False
    ###Your test code here.

    pass

# SPECIFICATION:
#
# The stats function computes some basic statistics functions
# when given a list of numbers as input.
#
# TASK:
#
# Achieve full statement coverage on the stats function. 
# All you should have to do is modify the test function 
# to call stats with different lists of values.

def stats(lst):
    min = None
    max = None
    freq = {}
    for i in lst:
        if min is None or i < min:
            min = i
        if max is None or i > max:
            max = i
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    lst_sorted = sorted(lst)
    if len(lst_sorted)%2 == 0:
        middle = len(lst_sorted)/2
        median = (lst_sorted[middle] + lst_sorted[middle-1]) / 2
    else:
        median = lst_sorted[len(lst_sorted)/2]
    mode_times = None
    for i in freq.values():
        if mode_times is None or i > mode_times:
            mode_times = i
    mode = []
    for (num, count) in freq.items():
        if count == mode_times:
            mode.append (num)
    print "list = " + str(lst)
    print "min = " + str(min)
    print "max = " + str(max)
    print "median = " + str(median)
    print "mode(s) = " + str(mode)

def test():
    ###Your code here.
    # Change l to something that manages full coverage. You may 
    # need to call stats twice with different input in order 
    # to achieve full coverage.
    l = [31, 32, 33, 33, 34]
    stats(l)
    l = [31, 32, 33, 33]

test()
