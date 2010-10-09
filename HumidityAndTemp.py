
import Adafruit_DHT
import time, datetime



def readDHT(room,sensor,pin):
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)
    return printOutput(room, hum, temp, pin)


def printOutput(room, hum,temp, pin):
    if hum is not None and temp is not None:
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%d/%m/%Y %H:%M:%S')
        #ftem = '0.1f%'.format(temp)
	ftem = '%2.1f'% temp
        fhum = '%2.1f'% hum
        values = [st, room, str(pin), ftem,fhum]
	return values

    else:
        print 'Failed to get reading from pin %d' % pin

def getHumAndTemp():
    sensor = Adafruit_DHT.DHT22
    #pins = {'Kitchen': 22, 'Lounge': 24, 'Supply Air': 23, 'Outside Air': 10, 'Exhaust Air': 18, 'Master Bedroom': 17}
    pins = {'Kitchen': 22, 'Lounge': 24, 'Supply Air': 23, 'Outside Air': 10, 'Exhaust Air': 18, 'Master Bedroom': 17}
    valList = []
    for room,pin in pins.items():
        valList.append(readDHT(room, sensor, pin))

    return valList
