from itertools import permutations
s,k = input().split()
a=sorted(list(permutations(s,int(k))))
#for i in range(len(a)):
  #print(''.join(a[i]))
#print(*[''.join(i) for i in a],sep='\n')
[print(*p,sep="") for p in a]
