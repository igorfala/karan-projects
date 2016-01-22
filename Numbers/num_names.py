#!/usr/bin/env python
"""
Project: Numbers to words. To use it, import num_names from num_names
         and call num_names(n). n can be float up to 999,999,999,999.99

author: Igor Fala

date: 12/08/2015
"""

def spell(n):
    """Spells numbers up to one 999"""
    names ={1 : "one", 2 : "two", 3 : 'three', 4 : 'four', 5 : 'five',
        6 : 'six', 7 : 'seven', 8 : ' eight', 9 :'nine', 10 : 'ten',
        11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
        15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18: 'eighteen',
        19 : 'nineteen', 0 :''
        }
    teens = { 2 :'twenty', 3 : 'thirty', 4 : 'forty', 5 : 'fifty',
        6 : 'sixty', 7 : 'seventy', 8 : 'eighty', 9 : 'ninety' 
        }
    if n == 0:
        print "zero",
    else:
        if n > 99:
            if n < 199:
                print "one hundreed",
            else:
                print " %s hundreed" % names[n//100],
            n = n % 100
        if n >= 20:
            print teens[n//10], names[int(n % 10)],
        elif n != 0:
            print names[n],

def num_names(n):
    """ 
    The function spells numbers up to 99 billion.
    """
    if n < 0:
        n = abs(n)
        print "minus",
        
    def dec(n):
        """Spells the decimals"""
        try:
            dec = str(n).split('.')[1][:2]
            if (n % 1) > 0:
                print 'point',
                if dec[0] == '0':
                    print 'zero',
                spell(int(dec))
        except IndexError: #if n is not float, pass
            pass
    #the number is divided to the order it belongs and each time 
    #the function spell is applied to it
    if n< 10**12 and n >= 10**9:
        spell(n//1000000000),
        if n < 2*10**9:
            print "billion",
        else:
            print "bilions",
        string = str(n)
        #slice the string as many characters as needed
        if n<10**10:
            n = float(string[1:])
        elif n<10**11:
            n = float(string[2:])
        else:
            n = float(string[3:])
    
    if n< 1000000000 and n >= 1000000:
        string = str(n)
        spell(n//1000000),
        if n < 2000000:
            print "million",
        else:
            print "millions",
        if n < 10**7:
            n = float(string[1:])
        elif n < 10**8:
            n = float(string[2:])
        else:
            #slice the string 3 characters
            n = float(string[3:])


    if n< 1000000 and n >= 1000:
        spell(n//1000),
        if n < 2000:
            print "thousand",
        else:
            print "thousands",
        string = str(n)
        
        #slice the string as many characters as needed
        if n<10000:
            n = float(string[1:])
        elif n<100000:
            n = float(string[2:])
        else:
            n = float(string[3:])
        
    if n < 1000:
        if n >= 1:
            spell(int(n))
        dec(n) 
