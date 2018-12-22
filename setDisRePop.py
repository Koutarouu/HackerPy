"""N=int(input())
S=set(map(int,input().rstrip().split()))
NC=int(input())
for _ in range(NC):
  s = input().split()
  cmd = s[0]
  args = s[1:]
  cmd += "("+ ",".join(args) +")"
  eval("S."+cmd)
  #print(cmd,args,S)

print(sum(S))

n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):#El asterisco hace referencia a los argumentos que se van a 
  eval('s.{0}({1})'.format(*input().split()+[''])) #Se le agrega la lista vacia por elemento como pop que no lleva argumentos

print(sum(s))"""
N=int(input())
S=set(map(int,input().rstrip().split()))
for _ in range(int(input())):
  method, *args = input().split()
  getattr(S, method)(*map(int,args))

"""
getattr(object, name[, default])
Return the value of the named attribute of object. name must be a string. If the string is the name of one of the object’s attributes, the result is the value of that attribute.
For example, getattr(x, 'foobar') is equivalent to x.foobar. If the named attribute does not exist, default is returned if provided, otherwise AttributeError is raised.
methods = {
  'pop' : S.pop,
  'remove' : S.remove,
  'discard' : S.discard
}
for _ in range(int(input())):
  method, *args = input().split()
  methods[method](*map(int,args))

Asterisk expands list or tuple to positional arguments. If we have a=[1,2,3]
then function(*a) is equal to function(1,2,3)
Thanks! I get that. Also, why is the need for adding an empty list?
El formato espera al menos 2 parámetros posicionales (función y argumento), pero puede que no haya parámetros como en la función pop.
Sample Input

"""