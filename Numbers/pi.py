#!/usr/bin/env python
"""
Project: Calculate pi up to n'th digit 

author: Igor Fala

Implementation of "Nilakantha series" to calculate Pi up to n'th digit: pi(n)
Implementation by importing the math module and calling it's methods: pi2(n)
 
"""
from decimal import getcontext, Decimal
import math

def pi(n):
    """Calculates Pi up to the n'th digit"""
    iter = 2.0 #iteration step
    p = 3 #starting point
    if n <= 50:
        for i in range(0,3000):
            p += 4.0 / (iter * (iter+1) * (iter+2))
            iter +=2
            p -= 4.0 / (iter * (iter+1) * (iter+2))
            iter +=2
        getcontext().prec = n+1 #changing default precision 
        #print getcontext().prec
        p = Decimal(p)
        print "Pi = ",
        print p*1 #for Decimal object to get the \
                  #right prec it needs to be multiplied by 1
    else:
        print "The number you provided is too large!"
        print "Here is a representation of Pi up to 50 digits:"
        return (pi(50))

def pi2(n):
    while n > 50:
        n = int(raw_input("Number too large. Please enter a number up to 50> "))
    
    else:
        print ' %.*f' % (n, math.pi)
if __name__ == "__main__": print __doc__