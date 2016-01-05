#!/usr/bin/python


import Adafruit_DHT




def readDHT(pin):
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    printOutput(hum,temp)


def printOutput(hum,temp):
    if hum is not None and temp is not None:
        print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temp, hum)
    else:
        print 'Failed to get reading. Boo hiss'

def getHumAndTemp():
    sensor = Adafruit_DHT.DHT22
    pins = {'Kitchen': 22, 'Lounge': 24, 'Supply Air': 23, 'Outside Air': 10, 'Exhaust Air': 18, 'Master Bedroom': 17}
    for room,pin in pins.items():
        print 'Room %s is pin %s' % (room,pin)
        readDHT(pin)
