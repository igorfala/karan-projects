#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ipLookUp: A simple script that determines info about the ip given.

@author: Igor Fala

date: 01/17/2015

"""

import json
from urllib import urlopen

def ipLookUp(ipAddress):
    '''ipAddress should be a string of the format: "111.111.111.111".'''
    URL = 'http://ipinfo.io/%s/json' % ipAddress
    fsock = urlopen(URL)
    if fsock.getcode() != 200:
        print '\nInvalid ip address.\n'
        return
    data = fsock.read()
    data = json.loads(data)
    fsock.close()
    print "\nDetailed information extracted from ipinfo.io:\n"
    for key, value in data.items():
        print key, ':', value
if __name__ == "__main__":
    import sys
    try:
        ipAddress = sys.argv[1]
    except:
        ipAddress = raw_input('Enter the ip address:\t')
    ipLookUp(ipAddress)