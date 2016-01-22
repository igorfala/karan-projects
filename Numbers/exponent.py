#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project: Exponentiation with different methods
        Call any of the methods: pow(x, n)
                                 pow_recur(x, n)
                                 pow_fast(x, n)
                                 pow_fast_recur(x, n)
        The last 2 methods perform the operation
        with the speed O(lg(n)).

author: Igor Fala
date: 07/07/2015

"""
def pow(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    if n < 0:
        return pow(1/float(x), -n)
    total = 1
    for i in range(n):
        total *= x
    return total

# It does the same thing with recursion
def pow_recur(x, n):
    if x == 0:
        return 0
    elif n == 0:
        return 1
    elif n < 0:
        return pow_recur(1/float(x), -n)
    else:
        return x * pow_recur(x, n-1)
        
# The next 2 functions calculate x to the n power with the speed O(lg(n))

def pow_fast(x, n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return x
    if n < 0:
        return pow_fast(1/float(x), -n)
    total = 1
    
    while n > 1:
        #print total, x, n
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n-1) / 2
            total *= x
        x = x**2
        if n == 1:
            total *= x
    return total

def pow_fast_recur(x, n):
    if x == 0:
        return 0
    elif n == 0:
        return 1
    elif n < 0:
        return pow_fast_recur(1/float(x), -n)
    elif n % 2 == 0:
        return pow_fast_recur(x**2, n/2)
    else:
        return x * pow_fast_recur(x**2, (n-1)/2)