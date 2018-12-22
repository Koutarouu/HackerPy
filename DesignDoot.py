n,m=map(int, input().split())
#m=n*3
l=".|."
p="-"

#Parte de arriba
for i in range(1,n):
  if i==n-1:
    print("WELCOME".center(m,p))
  elif i%2!=0:
    print((l*(i)).center(m,p))
  
#Parte de abajo
for j in range(n,0,-1):
  if j%2!=0 and j!=n:
    print((l*(j)).center(m,p))

#sample input 9 27