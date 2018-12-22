N=int(input())
s_paises=set()
for _ in range(N):
  s_paises.add(input().strip())
print(s_paises,len(s_paises))

"""N=int(input())
s_paises=[]
for _ in range(N):
    a=input()
    if a not in s_paises:
        s_paises.append(a)
print(len(s_paises))"""
print(len(set([input().strip() for i in range(int(input()))])))