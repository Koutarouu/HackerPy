from itertools import combinations_with_replacement
S,k=input().split()
for i in combinations_with_replacement(sorted(S),int(k)):
  print("".join(i)) #Join es mucho mas rapido
  #print(*i, sep='')
#print(*[''.join(p) for p in combinations_with_replacement(sorted(S), int(k))], sep='\n')
#Esta de abajo es la que gasta mas memoria por que tiene que transformar a lista
"""Sample Input

HACK 2
"""