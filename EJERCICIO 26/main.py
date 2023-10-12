
pila = [1,2,3,4,5,6,7,8,9]

print("Funciones de Pila: ")
#Apilar
print('Apilar: ')
pila.append(10)
print(pila)
#Desapilar
print('Desapilar: ')
print(pila.pop())
#Tamaño
print('Tamaño: ')
tamaño = len(pila)
print(tamaño)
#Isvacia
print('Isvacia: ')
if tamaño <= 0:
    print("La pila está vacía")
else:
    print("La pila no está vacía")
#Vaciar 
print('Vaciar: ')
pila.clear()
print(pila)