from math import sqrt,acos,degrees,atan,asin,atan2

ab=int(input())
bc=int(input())
m=sqrt((ab**2)+(bc**2))
#M=m/2
print("{}°".format(round(degrees(atan2(ab,bc)))))
