#!/usr/bin/python
import time;

localtime = time.localtime(time.time())
print "Local current time :", localtime

formattedcurrenttime = 
( time.localtime(time.time()))
print "Local current time :", formattedcurrenttime

print "what is your name?"
name = raw_input()
print "Hello %s!" % name


#ask what hour is it?
print "What is the hour?"
hour = raw_input()


#ask what minutes is it?
print "how many minutes?"
mins = raw_input()

#ask is it am or pm?
print "AM or PM"
ampm = raw_input()


#print them all out
print "%s %s %s" % (hour,mins,ampm)

# Now set the time using a python time function


#print out the nicely formatted time like do on line 4
