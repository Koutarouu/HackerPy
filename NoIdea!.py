n,m=map(int,input().split())
array=input().split()
A=list(set(input().split()))
B=list(set(input().split()))
print([(i in A)-(i in B) for i in array])
print(sum([(i in A)-(i in B) for i in array]))
happiness=0
for i in array:
  if i in A:
    happiness+=1
  elif i in B:
    happiness-=1
print(happiness)

"""
array=list(array)
for i in range(0,m):    
  happiness += array.count(A[i])
  happiness -= array.count(B[i])
  print(array.count(A[i]),array.count(B[i]))
print(happiness)"""