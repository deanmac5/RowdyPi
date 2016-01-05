#!/usr/bin/python


import HumidityAndTemp
import TempOneWire
import time

while(True):
    HumidityAndTemp.getHumAndTemp()
    TempOneWire.getReadings()
    print 'Date/Time | Location | Identifier | Temperature | Humidity'
    
