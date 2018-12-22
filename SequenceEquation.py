n=int(input())+1
prev=[0]*n
p=list(map(int,input().split()))
x=0
for i in p:
	prev[i] = x = x+1
print(*(prev[prev[i]] for i in range(1,n)), sep='\n')
