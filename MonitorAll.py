#!/usr/bin/python


import HumidityAndTemp
import TempOneWire

while(True):
    bothVals = HumidityAndTemp.getHumAndTemp()
    # justTempVals = TempOneWire.getReadings()
    print 'Date/Time | Location | Identifier | Temperature | Humidity'
    print bothVals
    # print justTempVals
