#!/usr/bin/env python
"""
Project: Display the list of all prime factors of a number: prime(n)
         Find the sequence of all prime numbers up to number n: eratosthenes(n)
         Display the next prime number starting with number n: next_prime(n) 

author: Igor Fala

date: 12/07/2015
"""
from sys import exit

def prod_list(list):
    #Helper function that calculates the product of elements of a list
    total = 1
    if list:
        for el in list:
            total *= el
    return total


def prime(n):
    """The function returns a list of all the prime factors of number n"""
    if n == 1:
        return [n,]
    list = []
    initial_n = n
    while prod_list(list) < initial_n:
        for number in xrange(2,(n+1)):
            if (n % number) == 0:
                list.append(number)
                n = n / number
                break
            # On the last iteration we break out when number is greater than n/2
            # If there are no divisors up to that point, than the number is a prime
            if number > (n+1)/2:
                list.append(n)
                break
    return list
    
def eratosthenes(n):
    """ 
    Using the Sieve of Eratosthenes, this function finds all the prime numbers 
    up to the number is passed in the function as parameter: n
    """
    if n < 0:
        print " Will calculate for nonnegative n"
        eratosthenes(-n)
    if n <= 3:
        return range(3)
    list_n = range(2,n+1)
    p = 2
    while p != list_n[-1]:
        for i in list_n:
            if (i % p == 0) and i > p:
                list_n.pop(list_n.index(i)) #popping out all the dividends
        #print p
        if p != list_n[-1]:
            p = list_n[(list_n.index(p)+1)]
    return list_n

def next_prime(n):
    #The function provides the next prime number 
    action = raw_input('Please press ENTER to continue or SPACE to exit >>>  ')
    prime = False
    while action != ' ':
        if n < 0:
            print "Will calculate for nonnegative n"
            next_prime(-n)
        if n < 3:
            print "The next prime number is: %d" % (n+1)
            prime = True
        else:
            while not prime:
                n += 1
                for i in xrange(2,n):
                    if n % i == 0:
                        break
                    if i > (n+2)/2:
                        prime = True
                        break
            print "The next prime number is: %d" % n
        print
        action = raw_input('Please press ENTER to continue or SPACE to exit >>>  ')
        n += 1
        prime = False
    exit(0)

if __name__ == "__main__": print __doc__