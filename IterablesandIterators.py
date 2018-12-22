from itertools import combinations

_,letters=input(),list(combinations(input().split(),int(input())))
cont=0
for i in letters:
	cont+=(1 if 'a' in i else 0)
print("%.4f"%(cont/len(letters)))

#cont2=0
#cont2+=1
#F = filter(lambda c: 'a' in c, letters)
#print("{0:.3}".format(len(list(F))/len()))