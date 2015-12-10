#!/usr/bin/env python
"""
Project: A program that calculates the cost of buying tiles to cover the area needed

@author: Igor Fala

date: 12/07/2015
"""
def tile(cost, width, height):
    area = width * height
    # Integer representation of area in square feet
    area_ft = int(area / 144) #assuming price is in square feet
    if area % 144 > 0:        #buying by square feet, if the area is not integer
        area_ft += 1          #an extra foot is needed
    #print area_ft
    return cost * area_ft