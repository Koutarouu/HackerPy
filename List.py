n = int(input())
l = []
for _ in range(n):
    s = str(input()).split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)

N = int(input())

lista=[]
e=0
print(""" Escoja cualquiera de estas opciones: insert i e:
          Insert integer  at position .
          print: Print the list.
          remove e: Delete the first occurrence of integer .
          append e: Insert integer  at the end of the list.
          sort: Sort the list.
          pop: Pop the last element from the list.
          reverse: Reverse the list.""")
for _ in range(0,N):
  opc=str(input())
  if opc=="insert":
    i=int(input("ingrese la posicion: "))
    e=int(input("ingrese el entero: "))
    lista.insert(i, e)
  elif opc=="print":
    print(lista)
  elif opc=="remove":
    e=int(input("ingrese el entero que quiere eliminar: "))
    lista.remove(e)
  elif opc=="append":
    e=int(input("Ingrese el entero que quiere añadir al final: "))
    lista.append(e)
  elif opc=="sort":
    lista.sort()
  elif opc=="pop":
    lista.pop()
  elif opc=="reverse":
    lista.sort(reverse=True)

"""
i=int(input("ingrese la posicion: "))
e=int(input("ingrese el entero: "))
e=int(input("ingrese el entero que quiere eliminar: "))
e=int(input("Ingrese el entero que quiere añadir al final: "))
"""