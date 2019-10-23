string = input()
odds, evens, lowercase, uppercase, =[],[],[],[]

for i in string:
	if i>='0' and i<='9':
		if int(i)%2==0: evens.append(i)
		else: odds.append(i)
	else:
		if i>='a' and i<='z': lowercase.append(i)
		else: uppercase.append(i)
odds.sort(); evens.sort(); lowercase.sort(); uppercase.sort()
print(*lowercase, *uppercase, *odds, *evens , sep='') 


# We know this:
"""
All sorted lowercase letters are ahead of uppercase letters. 
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits."""