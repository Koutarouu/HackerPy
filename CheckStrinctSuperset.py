A=set(map(int,input().split()));cont=0;n=int(input())
for _ in range(n):
	otherSet=set(map(int,input().split()))
	cont+=1 if len(A-otherSet)>=1 and otherSet-A==set() else 0
print(True if cont==n else False)