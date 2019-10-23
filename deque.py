from collections import deque

d = deque()
for _ in range(int(input())):
	put = input().split()
	getattr(d, put[0])(*put[1] if len(put)>1 else []) #*[] es igual que nada estos argumentos son * parseados ya
print(*d)