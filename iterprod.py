#FOR CALCULATE THE CARTESIAN PRODUCT
from itertools import product
a=list(map(int, input().rstrip().split()))
b=list(map(int, input().rstrip().split()))
x=list(product(a,b))
print(' '.join(str(i) for i in x))
print(' '.join(map(str, x)))