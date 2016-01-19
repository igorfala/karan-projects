#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A credit card validator function that uses a checksum.
Luhn formula is used to verify whether the card is valid or not

@author: Igor Fala

date: 12/08/2015
"""

def validator(n):
    r = str(n)[::-1]     # Reverse the string
    total = 0
    new_r = ''
    for i in range(len(r)):
        if i % 2 != 0:
            new_r += str(int(r[i]) * 2)
        else: 
            new_r += r[i]
    for i in new_r:
        total += int(i)
    # verify the first two digits of the card (the last two reversed,
    # since we reversed the number)
    if (int(r[-1]+r[-2]) in [34, 37]) and len(r) == 15:
        print 'American Express' 
    if (int(r[-1]+r[-2]) in range(51, 56)) and len(r) ==16:
        print "Mastercard"
    if (int(r[-1]) == 4) and (len(r) == 13 or len(r) == 16):
        print "Visa"
    if ((int(r[-1]+r[-2]+r[-3]) in [601, 622, 644, 645, 646, 647, 648, 649] 
        or int(r[-1]+r[-2]) == 65) and len(r) == 16):
        print "Discover"
        
    return total % 10 == 0
if __name__ == "__main__": 
    print __doc__