from cmath import phase,polar
n=input()
z=phase(complex(n))
r=abs(complex(n))
print(r)
print(z)
#  1+2j
print(*polar(complex(n)), sep='\n')
