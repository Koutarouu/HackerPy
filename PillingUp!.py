from collections import deque

for _ in range(int(input())):
  input()
  lengths=deque(map(int,input().split()))
  print("No" if max(lengths) not in (lengths[0],lengths[-1]) else "Yes")
    

"""for _ in range(int(input())):
  input()
  lengths=list(map(int,input().split()))
  l=len(lengths)
  i=0
  while i < l - 1 and lengths[i] >= lengths[i+1]:
    i += 1
  while i < l - 1 and lengths[i] <= lengths[i+1]:
    i += 1
  print("Yes" if i == l - 1 else "No")
"""
"""for t in range(int(input())):
  input()
  lst = [int(i) for i in input().split()]
  min_list = lst.index(min(lst))
  left = lst[:min_list]
  right = lst[min_list+1:]
  if left == sorted(left,reverse=True) and right == sorted(right):
    print("Yes")
  else:
    print("No")"""
"""for i in range(len(lengths)//2):
    if lengths[i]>=lengths[(len(lengths)-1)-i]:
      new.append(lengths[i])

      if new:
    print("Yes")
  else:
    print("No")"""