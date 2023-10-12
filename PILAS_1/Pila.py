import Nodo

class Pila:

    def __init__(self):
        self.superior = None
    
    def apilar(self,dato):
        print(f"Agregando {dato} en la cima de la pila")
        if self.superior == None:
            self.superior = Nodo(dato)
            return nuevo_nodo