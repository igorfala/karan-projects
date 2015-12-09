#!/usr/bin/env python
"""
Project: Calculate n'th Fibonacci number: fib_rec(n), fib_loop(n)
         Calculate the highest number up to n: fib_to(n)
         Generate the sequence to the n'th Fibonacci number: fib(n)
         Generate the sequence up to n'th Fibonacci number: fib_to_seq(n) 

@author: Igor Fala

date: 12/08/2015
"""
def fib_rec(n):
    """Calculates the n'th Fibonacci number using recursion"""
    if n < 0:
        n = int(raw_input("Please provide a nonnegative number > "))
        return fib_rec(n)
    elif n < 2:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_loop(n):
    """Calculates the n'th Fibonacci number using a for loop"""
    if n < 0:
        n = int(raw_input("Please provide a nonnegative number > "))
    if n < 2:
        return n
    else:
        fib1 = 0
        fib2 = 1
        total = 0
        for i in range(2,n+1):
            total = fib1 + fib2
            fib1 = fib2
            fib2 = total
        return total

def fib_to(n):
    if n < 0:
        n = int(raw_input("Please provide a nonnegative number > "))
    if n < 2:
        return n
    else:
        fib1 = 0
        fib2 = 1
        total = 0
        for i in range(2,n+1):
            total = fib1 + fib2
            fib1 = fib2
            fib2 = total
            if total >= n:
                break
        if total > n: #if total went over entered number
            return fib1 #the previous fibonacci number is returned
        return total #else total is returned

def fib(n):
    """Use helper function fib_rec(n) to generate a sequence"""
    return [fib_rec(i) for i in range(n+1)]
def fib_to_seq(n):
    """Use helper function fib_to(n) to generate a sequence"""
    seq = []
    for i in range(n+1):
        if fib_to(i) not in seq: seq.append(fib_to(i)) #making sure not to repeat numbers
    return seq
if __name__ == "__main__": print __doc__
