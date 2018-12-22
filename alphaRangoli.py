import string as st
alpha = st.ascii_lowercase

n = int(input());L = []
for i in range(n):
  s = "-".join(alpha[i:n])
  #print(s,s[::-1],s[1:])
  #le concatena al abecedario alrevez el normal apartir de la segunda la letra por ejemplo de la a sigue la b
  L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
#La imprime primero alrevez y ya la segunda mitad solo la imprime normal con el salto de linea
print('\n'.join(L[:0:-1]+L))
print(L)