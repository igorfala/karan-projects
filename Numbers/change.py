#!/usr/bin/env python
"""
Project: A program that returns the exact change 

author: Igor Fala

date: 12/05/2015
"""
def changeReturn(cost, amount):
    """
    Buying a product that costs 'cost' money and having 'amount' of 
    money, the function will return the most effective way to give 
    exact change . To utilize it, import it from the module
    and call it: changeReturn(cost, amount)
    """
    if amount < cost:
        print "Not enough resources!"
        return
    changes = []
    names = ["hundreds", "fifties", "twenties", \
                 "tens", "fives", "ones", \
                 "quarters", "dimes", "nickels", "pennies"]
    numbers = [100, 50, 20, 10, 5, 1, 25, 10, 5, 1]
    change = amount - cost
    # drilling the amount all the way down to pennies,
    for number, name in zip(numbers, names):
        if name == "quarters": change = round(change * 100)           
            
        count = int(change)/number
        change -= count * number
        changes.append(count)  # each time appending the number to the change_list
    print "The most effective change from %s dollars for %s dollars cost is: " \
          % (amount, cost)
    print "\n".join(["%i\t%s" %(count, name) for count, name\
                      in zip(changes, names) if count])

if __name__ == "__main__":
    print changeReturn.__doc__


