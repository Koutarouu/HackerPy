_, arr=int(input()), input().split()
#print(all([int(i)>=0 for i in arr]) and any([i[::-1]==i for i in arr]))
#list(map(int,...))muy importante ponerlo como lst por que el map solo lo modificas una vez y ya no lo puedes volver a utilizar por que me ayudo al primero pero para ar2 ya no
ar1=[int(i)>=0 for i in arr] #es como fijar el espacio en memoria del array
ar2=[i[::-1]==i for i in arr] #como esta tecnica no funciona muy bien con numeros negativos en el print especificamos
print(all(ar1)==any(ar2) if all(ar1) else False) #si hay negativos ya no importa nada
print(all(ar1) and all(ar2))
