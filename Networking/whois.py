"""
WHOIS: A simple script that determines whois from the ip given.

author: Igor Fala

date: 01/17/2015

"""


import subprocess, sys

try:
    ipAddress = sys.argv[1]
except:
    ipAddress = raw_input('Enter an ip address to search WHOIS:\t')

subprocess.call(['whois', ipAddress])