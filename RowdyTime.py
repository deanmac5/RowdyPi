import os
from datetime import datetime


#print "Enter the year"
#year = raw_input()

#print "Enter the month"
#month = raw_input()

#print "Enter the day"
#day = raw_input()

#date_str = year+month+day
#print date_str
date2 = "20081004"
time = "18:00:00"
date3 = "20091004 16:00"
#dt = datetime.strptime("2000-10-04 01:10:11", '%Y-%m-%d %T')
date4 = "2015-04-24T20:09:00.052-0500"
date5 = "1971-01-22 10:11Z"

os.system('date  -s %s' % date4)
