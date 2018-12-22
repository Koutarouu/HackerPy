import calendar
import datetime

m,d,y=map(int,input().split())
Days=["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY","SUNDAY"]
a=calendar.weekday(y,m,d)
print("".join(list(calendar.day_name[a])).upper())
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())
print("".join(Days[a]).upper())
print(datetime.datetime(y, m, d).strftime("%A").upper())
"""if a==0:
  print("MONDAY")
elif a==1:
  print("TUESDAY")
elif a==2:
  print("WEDNESDAY")
elif a==3:
  print("THURSDAY")
elif a==4:
  print("FRIDAY")
elif a==5:
  print("SATURDAY")
elif a==6:
  print("SUNDAY")

#output format = MM DD YYYY
"""

