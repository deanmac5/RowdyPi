testResult = [['06/01/2016 11:20:45', 'Master Bedroom', '17', '24.1 , 58.9%'], ['06/01/2016 11:20:48', 'Supply Air', '23', '23.6 , 57.1%'], ['06/01/2016 11:20:51', 'Outside Air', '10', '24.1 , 55.8%'], ['06/01/2016 11:20:51', 'Lounge', '24', '23.9 , 45.1%'], ['06/01/2016 11:20:52', 'Exhaust Air', '18', '24.0 , 53.8%'], ['06/01/2016 11:20:52', 'Kitchen', '22', '23.7 , 58.5%'], ['06/01/2016 11:20:52', '28-000006deb43c', 23.812], ['06/01/2016 11:20:53', '28-000006ded395', 23.812], ['06/01/2016 11:20:54', '28-000006ded896', 24.187], ['06/01/2016 11:20:55', '28-000006dee264', 23.875], ['06/01/2016 11:20:56', '28-000006def465', 23.562]]

for res in testResult:
    print res
    # print len(res)
    print ','.join(res)