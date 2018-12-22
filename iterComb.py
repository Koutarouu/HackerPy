from itertools import combinations
S,k=input().split()
k=int(k)
#print("\n".join([(''.join(p)) for i in range(1,int(k)+1) for p in combinations(sorted(S), i)]))
for i in range(1, k+1):
  for j in combinations(sorted(S), i):
    print(''.join(j))
"""
Sample Input

HACK 2
Sample Output

A
C
H
K
AC
AH
AK
CH
CK
HK
"""