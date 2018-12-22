"""M_i=int(input())
M=set(map(int,input().split()))
N_i=int(input())
N=set(map(int,input().split()))
#intersection=M.intersection(N)
print("\n".join(list(map(str,sorted(M.union(N)-M.intersection(N))))))"""
#a,b = [set(input().split()) for _ in range(4)][1::2]
M,N = [set(input().split()) for _ in range(4)][1::2]
print("\n".join(sorted(M.union(N)-M.intersection(N),key=int)))
"""print('\n'.join(sorted(a^b, key=int)))
print(a^b)#simetric diff"""