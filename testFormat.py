import os

testResult = [['06/01/2016 14:15:51', 'Master Bedroom', '17', '24.0', '58.5'], ['06/01/2016 14:15:52', 'Supply Air', '23', '23.5', '57.0'], ['06/01/2016 14:15:52', 'Outside Air', '10', '23.9', '55.4'], ['06/01/2016 14:15:53', 'Lounge', '24', '23.7', '46.5'], ['06/01/2016 14:15:53', 'Exhaust Air', '18', '23.8', '53.6'], ['06/01/2016 14:15:54', 'Kitchen', '22', '23.6', '58.3'],
              ['06/01/2016 14:15:54', '28-000006deb43c', '23.75'], ['06/01/2016 14:15:55', '28-000006ded395', '23.75'], ['06/01/2016 14:15:56', '28-000006ded896', '24.125'], ['06/01/2016 14:15:56', '28-000006dee264', '23.812'], ['06/01/2016 14:15:57', '28-000006def465', '23.562']]

file_name = "Paul-Test.csv"
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
    for res in testResult:
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

line += testResult[0][0]
for res in testResult:
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
