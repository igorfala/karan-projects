#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Factorial Finder:
    call: fact_loop(n) 
    or  : fact_recurs(n)

@author: Igor Fala
date: 11/07/2015
"""

def fact_loop(n):
    if n < 0:
        print "Negative number. Calculating for abs(n)"
        n = abs(n)
    total = 1
    if n == 0:
        return 1
    for i in range(1,n+1):
        total *= i
    return total

def fact_recurs(n):
    if n < 0:
        print "Negative number. Calculating for abs(n)"
        n = abs(n)
    if n == 0:
        return 1
    else:
        return n * fact_recurs(n-1)

if __name__ == '__main__':
    print __doc__