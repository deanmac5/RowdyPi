#!/usr/bin/python


import HumidityAndTemp,TempOneWire, time

#########################
# Functions
#########################

def writeTemp(values):

    file = open("All.txt",'a')

    s = str(values)
    file.write(s)
    file.write("\n")

    file.close()

def addSpacing():
	file = open("test.txt",'a')
	file.write("\n\n\n\n\n\n")
	print ("\n\n\n\n\n\n")
	file.close()


#########################
# Main
#########################

while(True):
    bothVals = HumidityAndTemp.getHumAndTemp()
    justTempVals = TempOneWire.getReadings()
    allValues = bothVals.append(justTempVals)
    print allValues
    writeTemp(allValues)
    #time.sleep(600)
