# Complete the solve function below.
def solve(s):
  new=s.split()
  new2=[]
  for i in range(len(new)):
    new2.append(new[i][0].upper()+new[i][1:])
  return new2

def solve2(s):
  newName=""
  ward=0
  for i in s:
    if i==s[0]:
      i=i.upper()
    elif i==" ":
      ward=len(newName)+1
    elif ward==len(newName):
      i=i.upper()
    newName+=i
  return newName

print(" ".join(solve("diego francisco")))
print(solve2("chris alan"))