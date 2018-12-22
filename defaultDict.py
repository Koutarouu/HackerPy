from collections import defaultdict

d=defaultdict(list)
list1=[]
n,m=map(int,input().split())

for i in range(n):
  d[input()].append(i+1)

for i in range(m):
  list1+=[input()]
print(d,list1)
for i in list1:
  if i in d:
    print(" ".join(map(str,d[i])))
  else:
    print -1
"""
from collections import defaultdict
n,m=map(int,input().split())
A=defaultdict(list)

for i in range(n):
    A[input()].append(str(i+1))

for i in range(m):
    print(' '.join(A[input()]) or -1)
"""

from collections import defaultdict
d = defaultdict(list)

nm=list(map(int,input().split()))

for i in range(0,nm[0]):
    d[input()].append(str(i+1)) 

for i in range(0,nm[1]):
    t=input()
    if t in d.keys():
        print(' '.join(d[t]))
    else:
        print(-1)
