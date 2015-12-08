#!/usr/bin/env python
"""
Project: A program that calculates the distance between 2 locations 

@author: Igor Fala

date: 12/07/2015
"""

import math, urllib, json, sys

def coordinates(address):
    """
    Takes in a string that represents a location name and returns
    a dictionary with coordinates. It uses google geocode api in order
    retrieve the latitude and longitude of the location 
    The returned dictionary is of form: {'lat': degrees, 'lng': degrees}
    """
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'
    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    uh = urllib.urlopen(url)
    data = uh.read()

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
    location = (js["results"][0]["geometry"]["location"])
    return location

def distanceCosine(locA, locB):
    """
    Returns the absolute distance between two locations
    Takes in 2 strings, that represent the locations as argument
    Ex:  distanceCosine(locA, locB)
    """
    locA, locB = map(coordinates, [locA, locB])
    #change the coordinates from degrees to radians on both cities
    for loc in locA, locB:
        for coord in loc: loc[coord] = math.radians(loc[coord])
    angle = math.radians(90)
    cosa = math.cos(angle-locA['lat'])* math.cos(angle-locB['lat'])\
         + math.sin(angle-locA['lat'])*math.sin(angle-locB['lat'])*\
         math.cos(abs(locA['lng']-locB['lng']))
    a = math.acos(cosa)
    a = math.degrees(a)
    distance = 40074 * a / 360
    return distance

if __name__ == "__main__":
    #print __doc__
    locA = raw_input("Enter the first location: ")
    locB = raw_input("Enter the second location: ")
    distance = distanceCosine(locA, locB)
    print "\nThe distance between %s and %s is:" \
          %(locA.capitalize(), locB.capitalize())
    print "Distance in km: %.2f" % distance
    print "Distance in miles: %.2f\n" % (distance *0.621371192)