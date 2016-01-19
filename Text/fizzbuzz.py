#!/usr/bin/env python
"""
Project: FizzBuzz

author: Igor Fala

date: 12/07/2015
"""

def fizzBuzz(n,m=0):
    #if m is assigned, then n and m are changing values
    if m !=0:
        n, m =m, n
    # The range is from m to n. m is 0 if it is not assigned and they dont exchange values
    for i in range(m,n+1):
        if i%3 == 0:
            if i%5 == 0:
                print 'FizzBuzz'
            else:
                 print 'Fizz'
        elif i%5 == 0:
            print 'Buzz'
        else:
            print i

def fizzBuzz1(n):
    """An alternative way of solving this"""
    for i in range(n+1):
        if not (i % 15): print 'FizzBuzz'
        elif not (i%3): print 'Fizz'
        elif not (i%5): print 'Buzz'
        else: print i 