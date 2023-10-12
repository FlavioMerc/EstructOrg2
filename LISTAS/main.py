#LISTAS
#Metodos

#Crear una lista estatica
lista = [1,2,10.5,4,5,'Carlos','C']
listados = [23,56]

#Agregar un nuevo elemento a la lista (append)
lista.append('Brenda')

#Vacia todos los items de una lista (clear)
lista.clear()

#Une una lista una con otra (extend)
lista.extend(listados)

#Cuenta el numero de veces que aparece un item (count)
[1,2,10.5,4,5,'Carlos','C'].count(1)

#Devuelve el indice en el que aparece un item(index)
[1,2,10.5,4,5,'Carlos','C'].index(1)

#Agrega un item en una posicion especifica(insert)
#Primera Posicion
listados.insert(0,0)
#Penultima Posicion
listados.insert(-1,20)
#Ultima Posicion con  len
n = (len(listados))
listados.insert(n,30)
#Posicion fuera del rango
listados.insert(999, 35)

#Extraer un item de la lista y lo borra(pop)
print(listados.pop())
#Sacar el primer elemento
print(listados.pop(0))

#Borra el primer item cuyo valor concuerde con el que se indique(remove)
listados.remove(23)

#Le da la vuelta a la lista(Reverse)
listados.reverse()
#Cadenas no tienen metodo .reverse
lista = list("Hola Mundo")
lista.reverse()
cadena = "".join(lista)
print(cadena)

#Ordenar de menor a mayor(sort)
listados.sort()
#Ordenar de mayor a menor
listados.sort(reverse=True)

#Retorna el numero de items de una lista(len)
resultado = len(listados)

#Imprimir la lista
print(lista)