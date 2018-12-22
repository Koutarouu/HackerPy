def minion_game(string):
  # your code goes here
  vowel=['A','E','I','O','U']
  S=0
  K=0
  for i in range(len(string)):
    if string[i] in vowel:
      K+= len(string)-i
    else:
      S+=len(string)-i
  print(K,S)
  if S>K:
    print("Stuart"+" "+ "%d" % S)
  elif K>S:
    print("Kevin"+" "+'%d' % K)
  else:
    print("Draw")
    
minion_game("BANANA")

def minion_game2(string):
  vowels="AEIOU"
  s,k=0,0
  for i in range(len(string)):
    if string[i] in vowels:
      k+=len(string)-i #son todas las subcadenas de diferente longitud que empiecen con vocal
      print(s)
    else:
      s+=len(string)-i
      print(k)
  print(k,s)
  if s>k:
    print("Stuart"+" "+ "%i" % s)
  elif k>s:
    print("Kevin"+" "+'%i' % k)
  else:
    print("Draw")

minion_game2("BANANA")

"""Esto es Python. La lógica es simple: tomar todas las subcadenas posibles,
dividirlas en dos conjuntos de acuerdo con la letra inicial, luego sumar elementos en conjuntos. 
Todas las subcadenas posibles son cadenas de longitud 1, 
luego las cadenas de longitud 2, etc., 
iarriba son un iterador para esa longitud. 
Y luego viene una pequeña optimización: si conoce la letra de inicio,
puede agregar todas las subcadenas de diferente longitud que comiencen con esta letra. Serálen(s) - i
"""