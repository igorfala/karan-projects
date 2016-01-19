#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Verify if a string is palindrome. 
Import the module and call one of the functions:
palindrome(s), or palindrome_recur(s)

author: Igor Fala

date: 01/17/2015

"""

def palindrome(s):
    if len(s) <= 1:
        return True
    begin = s[:(len(s)/2)]
    if len(s) % 2 == 0:
        end = s[(len(s)/2):]
    else:
        end = s[(len(s)/2+1):]
    return begin == end[::-1]

        
def palindrome_recur(s):
    if len(s) <=1:
        return True
    else:
        if s[0] != s[-1]:
            return False
        return palindrome_recur(s[1:-1])
