#!/usr/bin/env python
"""
Coin flip simulations

author: Igor Fala

date: 12/10/2015
"""
import random

def coin_flip(n):
    heads = 0
    for i in range(n):
        sim = random.choice([0,1])
        if sim == 1:
            heads += 1
    print "With %d coin simulations, we got: " % n
    print "%d heads" % heads
    print " Probability for heads is: %r" % (heads/float(n))
    print "%d tails" % (n-heads)
    print "Probability for tails is : %s" % ((n-heads)/float(n))

if __name__ == "__main__":
    n = int(raw_input('How many simulations would you like to perform? '))
    coin_flip(n)
            
