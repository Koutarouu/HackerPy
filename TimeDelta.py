from datetime import datetime as dt

def time_delta(t1,t2):
  fmt="%a %d %b %Y %H:%M:%S %z"
  a = dt.strptime(t1,fmt)
  b = dt.strptime(t2,fmt)
  print(a-b)
  return str(int(abs((a-b).total_seconds())))

n=int(input())
for i in range(n):
  t1 = input()
  t2 = input()
  print(time_delta(t1, t2))

"""
Sample Input 0

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sample Output 0

25200
88200

datetime.strptime(date_string, format)¶
Return a datetime corresponding to date_string, parsed according to format.
This is equivalent to datetime(*(time.strptime(date_string, format)[0:6])). 
ValueError is raised if the date_string and format can’t be parsed by time.strptime()
or if it returns a value which isn’t a time tuple.
For a complete list of formatting directives, see strftime() and strptime() Behavior.
timedelta.total_seconds()
Return the total number of seconds contained in the duration. Equivalent to td
/ timedelta(seconds=1).
Note that for very large time intervals (greater than 270 years on most platforms)
this method will lose microsecond accuracy.
"""