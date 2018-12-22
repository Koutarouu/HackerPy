def merge_the_tools(string, k):
  # your code goes here
  new=[]
  longtemp=0
  temp=[]
  for i in string:
    longtemp+=1
    if i not in temp:
      temp.append(i)
    if longtemp==k:
      new.append(''.join(temp)) #lo podia imprimir desde aca
      temp=[]
      longtemp=0
  return "\n".join(map(str, new))

  #return string,k

string, k = input(), int(input())
print(merge_the_tools(string, k))
#=================================================
print("========================================================================")
S, N = input(), int(input()) 
print(zip(*[iter(S)] * N))
for part in zip(*[iter(S)] * N):
  d = dict()
  print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
"""
for i in range(0,len(string)+1,substrings):
    new.append(string[(i-substrings):i])"""

"""
Sample input
AABCAAADA
3
Output
AB
CA
AD
"""