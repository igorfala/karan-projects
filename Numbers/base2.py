#!/usr/bin/env python
"""
Project: A program that converts from base 2 to base 10 and viceversa 

author: Igor Fala

date: 12/07/2015
"""
def bin_to_dec(string):
    """
    Converts binary to decimal. Input should be string
    
    """
    # first we reverse the string
    string = string[::-1]
    total = 0
    for i in range(len(string)):
        total += (2**i) * int(string[i])
    return total
    
def dec_to_bin(n):
    """
    Converts decimal to binary. Input should be a positive integer
    
    """
    total = ''
    while n > 0:
        total += str(n % 2)
        n /=2
    # it returns a reverse copy of the string created in the loop
    return int(total[::-1])
