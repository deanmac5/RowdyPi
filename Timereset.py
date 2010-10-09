#!/usr/bin/python
import os
import sys

#to reset time to local time after power faillure
#sudo date -s "Wed March 9 02:29:00 UTC 2016"Wed Mar  9 13:29:00 AEDT 2016
#Australian Easten Standard Time is UTC+10 
#Australian Easten Daylight Time is UTC+11


#########################
# Functions
#########################

def writeTime(values):
    file = open("All.csv", 'a')

    s = str(values)
    file.write(s)
    file.write("\n")

    file.close()


def addSpacing():
    file = open("All.csv", 'a')
    file.write("\n")
    print ("\n")
    file.close()


