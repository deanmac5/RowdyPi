#!/usr/bin/python


import HumidityAndTemp
import TempOneWire

while(True):
    HumidityAndTemp.getHumAndTemp()
    TempOneWire.getReadings()
