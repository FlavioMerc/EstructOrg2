class Nodo:
    def __init__(self, edad):
        self.edad = edad
        self.siguiente = None

class Clinica:
    def __init__(self):
        self.inicio = None
        self.final = None

    def agregarPaciente(self, edad):
        print(f"Agregando paciente de {edad} años a la cola de la clínica")
        nuevo_nodo = Nodo(edad)
        if self.final is None:
            self.inicio = self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def eliminarPaciente(self):
        if self.inicio is None:
            print("La clínica está vacía")
            return
        print(f"Eliminando al paciente de {self.inicio.edad} años")
        self.inicio = self.inicio.siguiente
        if self.inicio is None:
            self.final = None

    def listarPacientes(self):
        if self.inicio is None:
            print("La clínica está vacía")
            return
        print("Edades de los pacientes en la clínica:")
        nodo_aux = self.inicio
        while nodo_aux:
            print(nodo_aux.edad, end=", ")
            nodo_aux = nodo_aux.siguiente
        print()

    def buscarPacientesMayoresDe70(self, eliminar=False):
        if self.inicio is None:
            print("La clínica está vacía")
            return

        pacientes_mayores_de_70 = []
        nodo_actual = self.inicio
        paciente_anterior = None

        while nodo_actual:
            if nodo_actual.edad  >= 70:
                pacientes_mayores_de_70.append(nodo_actual.edad)
                if eliminar:
                    if paciente_anterior:
                        paciente_anterior.siguiente = nodo_actual.siguiente
                        if nodo_actual == self.final:
                            self.final = paciente_anterior
                    else:
                        self.inicio = nodo_actual.siguiente
                else:
                    paciente_anterior = nodo_actual

            if not eliminar:
                paciente_anterior = nodo_actual

            nodo_actual = nodo_actual.siguiente

        if (pacientes_mayores_de_70):
            clinica.eliminarPaciente()

clinica = Clinica()

clinica.agregarPaciente(70)
clinica.agregarPaciente(30)
clinica.agregarPaciente(60)

clinica.listarPacientes()

clinica.agregarPaciente(75)
clinica.agregarPaciente(78)

clinica.listarPacientes()

clinica.buscarPacientesMayoresDe70()

clinica.listarPacientes()