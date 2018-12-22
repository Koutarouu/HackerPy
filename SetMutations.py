_,A=input(),set(map(int,input().split()))
for _ in range(int(input())):
  eval('A.%s(%s)'%((input().split()[0]),set(map(int,input().split()))))
print(sum(A),A)