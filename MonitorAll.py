#!/usr/bin/python
import os

import HumidityAndTemp,TempOneWire, time

#########################
# Functions
#########################

def writeTemp(values):

    file = open("All.csv",'a')

    s = str(values)
    file.write(s)
    file.write("\n")

    file.close()

def addSpacing():
	file = open("All.csv",'a')
	file.write("\n")
	print ("\n")
	file.close()


#########################
# Main
#########################

while(True):

    bothVals = HumidityAndTemp.getHumAndTemp()
    justTempVals = TempOneWire.getReadings()
    allValues = bothVals + justTempVals

    file_name = "results.csv"
    tempHumidityIndexes = {0: "Date", 1: "ID", 2: "Pin Number", 3: "Temperature", 4: "Humidity"}
    tempWireIndexes = {0: "Date", 1: "ID", 2: "Temperature_wire"}
    temp_humidity = "Temp,Hum"
    temp = "Temp"
    both_count = 0
    wire_count = 0

    id_date = 0
    id_key = 1
    id_pin = 2
    id_both_temp = 3
    id_both_hum = 4
    id_wire_temp = 2
    for key, value in tempHumidityIndexes.iteritems():
        if value == "ID":
            id_key = key
        elif value == "Date":
            id_date = key
        elif value == "Pin Number":
            id_ping = key
        elif value == "Temperature":
            id_both_temp = key
        elif value == "Humidity":
            id_both_hum = key

    for key, value in tempWireIndexes.iteritems():
        if value == "Temperature_wire":
            id_wire_temp = key
    line = ""
    if not os.path.isfile(file_name):
        line += "Date"
        for res in allValues:
            line += ","+res[id_key]
            if len(res) == 5:
                line += ","
                both_count += 1
            elif len(res) == 3:
                wire_count += 1

        line += "\n"
        for i in xrange(both_count):
            line += ","+temp_humidity

        for i in xrange(wire_count):
            line += ","+temp

        line += "\n"

    line += allValues[0][0]
    for res in allValues:
        data = ""
        if len(res) == 5:
            data += ","+res[3]+","+res[4]
        elif len(res) == 3:
            data += ","+res[2]

        line += data

    line += "\n"

    print line

    file = open(file_name,'a')

    s = str(line)
    file.write(s)

    file.close()
    time.sleep(600)
