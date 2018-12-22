import re

for _ in range(int(input())):
  res=True
  try:
    reg=re.compile(input())
  except re.error:
    res=False
  print(res)


"""
Sample Input

2
.*\+
.*+
Sample Output

True
False
"""