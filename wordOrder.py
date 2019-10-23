from collections import Counter

d=Counter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())

d={}
for _ in range(int(input())):
	w=input()
	if w in d:
		d[w]+=1
		continue
	d[w]=1
print(len(d))
print(*d.values())
