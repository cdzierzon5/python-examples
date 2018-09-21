#Cody Dzierzon
#9/21/18
# Clock


def clock():
 import time
 import calendar

 x=calendar.timegm(time.gmtime())

 x=x*1000

 total_second = x//1000
 current_second = total_second%60

 total_minutes = total_second//60
 current_minute = total_minutes%60

 total_hours = total_minutes//60
 current_hour = total_hours%24
 mtt_hour = int(current_hour)-6
 print(mtt_hour,":",current_minute,":",current_second)



i=0
while i==0:

    clock()


