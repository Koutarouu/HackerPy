from collections import deque
d=deque()
for _ in range(int(input())):
  method, *args = input().split()
  getattr(d, method)(*map(int,args))
# for i in range(int(input())):
#     eval('d.{0}({1})'.format(*input().split()+['']))
print(" ".join(map(str,d)))

"""
6
append 1
append 2
append 3
appendleft 4
pop
popleft
"""