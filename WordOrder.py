from collections import Counter,OrderedDict
#W=Counter()
"""lista=[]
for _ in range(int(input())):
  lista.append(input())
print(len(set(lista)))
print(" ".join(map(str,Counter(lista).values())))"""
d=OrderedDict()#{}
for _ in range(int(input())):
  a=input()
  if a not in d:
    d[a]=1
  else:
    d[a]+=1
print(len(d))
print(*d.values())
# for v in sorted(d.values()):
#   print(v,end=" ")

"""
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())
"""