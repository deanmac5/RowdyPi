#!/usr/bin/python

import Adafruit_DHT

sensor = Adafruit_DHT.DHT22

kitchenPin = 22
loungePin = 24



khumidity, ktemp = Adafruit_DHT.read_retry(sensor, kitchenPin)
lhumidity, ltemp = Adafruit_DHT.read_retry(sensor, loungePin)

if khumidity is not None and ktemp is not None:
    print 'Kitchen Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(ktemp, khumidity)
else:
    print 'Failed to get Kitchen reading. Try again!'

if lhumidity is not None and ltemp is not None:
    print 'Lounge Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(ltemp, lhumidity)
else:
    print 'Failed to get Lounge reading. Try again!'
