lista = []
longitud = int(input('Digite el numero de elementos: '))

for i in range(1,longitud+1):
    dato = input('Escriba el dato: ')
    lista.append(dato)

for i in lista:
    print(i,end=' ')
#   print(i)