import datetime
from datetime import datetime

# weekdays as a set

WeekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
RunDuration=[0.0,0.0,0.0,0.0,0.0,0.0,0.0]
TotalDuration=0
today=datetime.date(datetime.now())
print(f'Today date is ', today)
todayindex=today.weekday()
todaystring=WeekDays[todayindex]
print(f'Today is ', todaystring)
#print(datetime.date(datetime.now()))
x=todayindex
while x>=0:
    print(f'enter run duration for ', WeekDays[x])
    RunDuration[x] = input()
    x-=1
x=6
while x>todayindex:
    print(f'enter run duration for ', WeekDays[x])
    RunDuration[x] = input()
    x-=1

for y in range(0, 6):
    print( WeekDays[y], f'run duration is ',RunDuration[y] )
    TotalDuration += float(RunDuration[y])

print( f'Average run duration is ',TotalDuration/7 )