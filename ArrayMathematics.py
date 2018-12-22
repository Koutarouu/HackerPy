import numpy

"""n, m = map(int, input().split())
a, b = (np.array([input().split() for _ in range(n)], dtype=int) for _ in range(2))
print(a+b, a-b, a*b, a//b, a%b, a**b, sep='\n')"""

rm=input().split()
n=int(rm[0])
m=int(rm[1])
arrayA=[input().split() for _ in range(n)]
arrayB=[input().split() for _ in range(n)]
a=numpy.array(arrayA, int)
b=numpy.array(arrayB, int)
arr=[a+b,a-b,a*b,a//b,a%b,a**b]
for i in range(6):
  print(arr[i])
#print(a,b)
