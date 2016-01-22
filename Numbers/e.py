#!/usr/bin/env python
"""
Project: Calculate e up to n'th digit . 
To use it:import the module e and call e.calc_e(n)

author: Igor Fala

Date: 12/08/2015

"""
def factorial_to_20():
    """A helper function that calculates all the factorials up to 20"""
    total = []
    for i in range(1,21):
        p = 1
        for j in xrange(1,i+1):
            p *= j
        total.append(p)
    return total
    
def calc_e(n):
    """Returns e up to n'th digit"""
    list = factorial_to_20()
    total = 0
    for i in range(0,len(list)):
        total += (i+1)/float(list[i])
        
    return round(total, n)
if __name__ == "__main__": print __doc__