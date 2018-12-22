"""xy=input().split()
x=int(xy[0])
y=int(xy[1])-1
suma=0
while y>=0:
	suma+=x**y
	y-=1
print(True if suma==int(xy[1]) else False)
"""
x,y=map(int,input().split())
print(y==eval(input()))