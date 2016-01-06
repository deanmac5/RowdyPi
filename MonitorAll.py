#!/usr/bin/python


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
    

    for res in allValues:
        cleanResult =  ','.join(res)
        print cleanResult
        writeTemp(cleanResult)
        

    # writeTemp(allValues)
    # addSpacing()
    # time.sleep(600)
