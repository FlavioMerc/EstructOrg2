longitud =  int(input('Digite el tamaño del triangulo: '))

for i in range (1, longitud + 1):
    for j in range(1, i + 1):
        if j % 1 == 0:
            print(" *" * i,end= " ")
        else:
            print(" ",end= " ")
    print("")