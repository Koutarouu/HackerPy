from functools import reduce

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
  #print(reduce(lambda x,y: x*10+y, [i]*i))
  #print(sum(map(lambda x: i * 10**x, range(i))))
  print((10**i//9) * i)
  #print([0,1,22,333,4444,55555,666666,7777777,88888888,999999999][i]) #o i-1
  #print(*[i for j in range(i)],sep='')
  #print(str(i)*i)

"""
product = 1
list = [1, 2, 3, 4]
for num in list:
    product *= num

# product = 24

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# Output: 24

"""