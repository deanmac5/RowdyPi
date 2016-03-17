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

os.system('date  -s %s' % date2)
