import os
from datetime import datetime


print "Enter the year"
year = raw_input()

print "Enter the month"
month = raw_input()

print "Enter the day"
day = raw_input()

print "Enter the hour"
hour = raw_input()

print "Enter the minutes"
minutes = raw_input()


#Changed time zone to +1000
date_str = year+'-'+month+'-'+day+'T'+hour+':'+minutes+':00.52+1000'
print date_str


date4 = "2015-04-24T20:09:00.052-0500" #this is the format we need


os.system('date  -s %s' % date_str)
