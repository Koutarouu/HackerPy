for _ in range(int(input())):
	num=int(input())
	original=num
	cont=0
	while num>0:
		if (num%10)!=0 and original%(num%10)==0:
			cont+=1
		num//=10
	print(cont)

for _ in range(int(input())):
	num=list(input())
	cont=0
	for i in num:	
		cont+=(1 if int(i)!=0 and (int("".join(num))%int(i))==0 else 0)
	print(cont)

for _ in range(int(input())):
	num=int(input())
	print(len([i for i in map(int,list(str(num))) if i!=0 and num%i==0]))