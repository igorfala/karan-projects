#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Project: Pig Latin

author: Igor Fala

date: 06/17/2015

"""

def piglatin(s):

    consonants = 'qwrtpsdfghjklzxcvbnm'
    new_s = ''
    new_s += s[1:] + s[0]
    if s[0] in consonants:
        new_s += 'ay'
    else:
        new_s += 'way'
    return new_s