#!/usr/bin/python

import Adafruit_DHT

sensor = Adafruit_DHT.DHT22

kitchenPin = 22
loungePin = 24
supplyAirPin = 23
outsideAirPin = 10
ExhaustAirPin = 18
MBedroomPin = 17


khumidity, ktemp = Adafruit_DHT.read_retry(sensor, kitchenPin)
if khumidity is not None and ktemp is not None:
    print 'Kitchen Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(ktemp, khumidity)
else:
    print 'Failed to get Kitchen reading. Try again!'



lhumidity, ltemp = Adafruit_DHT.read_retry(sensor, loungePin)
if lhumidity is not None and ltemp is not None:
    print 'Lounge Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(ltemp, lhumidity)
else:
    print 'Failed to get Lounge reading. Try again!'



sahumidity, satemp = Adafruit_DHT.read_retry(sensor, supplyAirPin)
if sahumidity is not None and satemp is not None:
    print 'Supply Air Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(satemp, sahumidity)
else:
    print 'Failed to get Supply Air reading. Try again!'



oahumidity, oatemp = Adafruit_DHT.read_retry(sensor, outsideAirPin)
if oahumidity is not None and oatemp is not None:
    print 'Outside Air Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(oatemp, oahumidity)
else:
    print 'Failed to get Outside Air reading. Try again!'



Eahumidity, Eatemp = Adafruit_DHT.read_retry(sensor, ExhaustAirPin)
if Eahumidity is not None and Eatemp is not None:
    print 'Exhaust Air Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(Eatemp, Eahumidity)
else:
    print 'Failed to get Exhaust Air reading. Try again!'




MBrhumidity, MBrtemp = Adafruit_DHT.read_retry(sensor, MBedroomPin)

if MBrhumidity is not None and MBrtemp is not None:
    print 'Master Bedroom Air Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(MBrtemp, MBrhumidity)
else:
    print 'Failed to get Master Bedroom reading. Try again!'
