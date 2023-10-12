class Pila:

    def __init__(self):
        self.elementos = []

    def apilar(self, dato):
        self.elementos.append(dato)
        return dato

    def deapilar(self):
        return self.elementos.pop()
    
    def checarPila(self):
        return len(self.elementos) == 0

    def checarUltimo(self):
        return self.elementos[-1]


if __name__ == '__main__':
    pila = Pila()

print(pila.checarPila())

pila.apilar(1)
pila.apilar('Flavio')
pila.apilar(5.9)
pila.apilar('Cibeles')

print(pila.checarPila())

print(pila.checarUltimo())