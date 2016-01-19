"""
Collatz Conjecture. The program calculates the steps
it takes to reach 1, starting with the number given as input 
to function collatz(n)
"""
def collatz(n):
    """Takes in a number n and returns a tuple of:
    (num, list) where num is the number of steps to reach 1,
    and list is a list of those steps.
    """
    total = 0
    list = []
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        list.append(n)
        total += 1
    return total, list

if __name__ == "__main__":
    n =int(raw_input("Enter a number to start the Conjecture:\t"))
    num, list = collatz(n)
    print "Numbers the program steps through,",
    print "in order to reach number 1:"
    print ", ".join(["%i" % number for number in list])
    print 
    print "The number of steps it takes: %s" % num