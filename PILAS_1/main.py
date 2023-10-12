class Nodo:

    def __init__(self,dato):
        self.dato = dato
        self.apuntador = None

class Pila:

    def __init__(self):
        self.superior = None
    
    def apilar(self,dato):
        print(f"Agregando {dato} en la cima de la pila")
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.apuntador = self.superior
        self.superior = nuevo_nodo

    def listar(self):
        if self.superior == None:
            print("La pila esta vacia")
            return
        print("Imprimiendo pila. ")
        nodo_aux = self.superior
        while nodo_aux != None:
            print(f"{nodo_aux.dato}", end =", ")
            nodo_aux = nodo_aux.apuntador
        print("")
    
    def desapilar(self):
        print(f"Desapilando {self.superior.dato}")
        self.superior = self.superior.apuntador

pila = Pila ()

pila.apilar("Flavio")
pila.apilar("Alan")
pila.apilar("Brenda")

pila.listar()

pila.desapilar()