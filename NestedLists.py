"""#from operator import itemgetter

if __name__ == '__main__':
  arr=[]
  new=[]
  for i in range(int(input())):
    name = input()
    score = float(input())
    arr.append([name,score])
  a=sorted(arr,key=lambda scoree: scoree[1])
  for j in range(len(a)):
    for k in range(2):
      if a[j][k]==a[1][1]:
        new.append(a[j])

  new=sorted(new,key=lambda name: name[0])
  for a in range(len(new)):
    print(new[a][0])

  #print(sorted(new,key=itemgetter(0)))
"""

n = int(input())
marksheet = [[input(), float(input())] for _ in range(n)]

second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
"""
count=0
  for j in range(len(a)):
    for k in range(2):
      if a[j][k]==a[0][1]:
        count+=1
      elif a[j][k]==a[1][1] and count<2:
        new.append(a[j])
      elif a[j][k]==a[2][1]:
        new.append(a[j])
"""