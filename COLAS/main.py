class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:

    def __init__(self):
        self.frente = None
        self.final = None

    def encolar(self, dato):
        print(f"Agregando {dato} al final de la cola")
        nuevo_nodo = Nodo(dato)
        if self.final is None:
            self.frente = self.final = nuevo_nodo
            return
        self.final.siguiente = nuevo_nodo
        self.final = nuevo_nodo

    def desencolar(self):
        print(f"Desencolando {self.frente.dato}")
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None

    def listar(self):
        if self.frente is None:
            print("La cola está vacía")
            return
        print("Imprimiendo cola:")
        nodo_aux = self.frente
        while nodo_aux:
            print(f"{nodo_aux.dato}", end=", ")
            nodo_aux = nodo_aux.siguiente
        print("")

cola = Cola()

cola.encolar('Flavio')
cola.encolar('Maria')
cola.encolar('Jose')

cola.listar()

cola.encolar("Hugo")

cola.desencolar()
cola.listar()