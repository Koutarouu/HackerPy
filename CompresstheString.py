from itertools import groupby

print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

groups = []
uniquekeys = []
data = input()
for k, g in groupby(data):
  groups.append(list(g))      # Store group iterator as a list
  uniquekeys.append(k)

for k in range(len(uniquekeys)):
  print((len(groups[k]),int(uniquekeys[k])),end=' ')
