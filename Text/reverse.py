#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project: Reverse a string
Call any of the functions:
reverse(s) or reverse_recur(s)

python's default reverse implementation is :
string[::-1]

author: Igor Fala

date: 06/17/2015

"""


def reverse(s):
    r = ''
    for i in range(len(s)):
        r += s[len(s)-i-1]
    return r
    

def reverse_recur(s):
    if len(s) == 0:
        return None
    if len(s) == 1:
        return s
    else:
        return s[-1:] + reverse_recur(s[:-1])
