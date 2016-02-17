#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple alarm clock and timer script that works cross-system

Call: timer(t) for timer
and: alarm(t) for alarm

author: Igor Fala
date:01/21/2016

"""   

import time, datetime
import os
import subprocess, signal

def process(sound = 'alarm.wav'):
    '''Determines what system is running on and uses the appropriate command
       to start a process to play a sound: 'alarm.wav' by default'''
    import sys
    systems = {'linux': 'aplay %s' % sound,
              'linux2': 'aplay %s' % sound,
              'win32': ['start', sound],
              'cygwin': ['start', sound],
              'darwin': 'afplay %s' % sound,
              'os2': 'afplay %s' % sound,
              'os2emx': 'afplay %s' % sound,
              }
    for key in systems:
        if key == sys.platform:
            return subprocess.Popen(systems[key], shell=True)

def timer(t):
    '''Timer function'''
    t = t.strip()
    # Any of the following formats can be used
    timeFormats = ('%H:%M:%S', '%M:%S', '%S', '%H hr %M min %S sec',\
                   '%M min %S sec', '%S sec', '%H hr %M min', '%H hr',\
                   '%M min %S sec', '%M min', '%S sec', '%H hr %S sec',)
    for format in timeFormats:
        try:
            tParsed = time.strptime(t, format)
        except ValueError:
            pass

    tDelta = datetime.timedelta(hours=tParsed.tm_hour, minutes=tParsed.tm_min, seconds=tParsed.tm_sec)
    print "Time remaining:"
    while True:
        tDelta -= datetime.timedelta(seconds = 1) # Decrease one second at a time
        print tDelta

        if not tDelta:            # When reaching '0'
            action = process()    # Action is started
            input = raw_input('Press any buttons to stop the alarm. Then press ENTER\n\n')
            if input != None:                               # If Enter is pressed
                os.kill(int(action.pid), signal.SIGTERM)    # process is killed
                break                                       # Breaking out of loop
        time.sleep(1)                    # Delay each step a second

def alarm(t):
    '''Alarm function'''
    timeFormats = ('%H:%M', '%H hr %M min', '%H hr', '%I %p', '%I:%M %p')
    for format in timeFormats:
        try:
            tParsed = time.strptime(t, format)
        except ValueError:
            pass
    # create a datetime.time instance: setTime from USER input
    setTime = datetime.time(hour=tParsed.tm_hour, minute=tParsed.tm_min)
    print 'Alarm set for %s' % setTime.strftime('%I:%M %p')

    while True:
        now = datetime.datetime.now().time()
        now = now.replace( microsecond = 0)
        if now ==setTime:
            action = process()
            input = raw_input('Press any buttons to stop the alarm. Then press ENTER\n\n')
            if input != None:
                os.kill(int(action.pid), signal.SIGTERM)
                break
        time.sleep(1)

if __name__ == "__main__":
    print __doc__
