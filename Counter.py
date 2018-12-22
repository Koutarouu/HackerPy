from collections import Counter

x=int(input())
shoes=Counter(map(int, input().split()))
t=int(input())
total=0
for a0 in range(t):
  #size and price talla y precio
  a,b=map(int,input().split())
  if shoes[a]:
    total+=b
    shoes[a]-=1
print(total)

"""
Sample Input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55 #se agotaron
4 40
18 60
10 50 #nunca existio
Output
200
"""