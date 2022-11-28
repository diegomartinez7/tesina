from Models.Entidades.Jugadores.Jugador import Jugador
from Models.Entidades.Competencia import Competencia

from operator import attrgetter

class Equipo:
    def __init__(self, id, nombreEquipo, categoria, rama, tipoEquipo, nombreEntidad, contrario):
        # Información del Equipo
        self.id: int = id
        self.nombreEquipo: str = nombreEquipo
        self.categoria: str = categoria
        self.rama: str = rama
        self.tipoEquipo: str = tipoEquipo
        self.nombreEntidad: str = nombreEntidad
        self.contrario: bool = contrario

        # Conjuntos de datos pertenecientes al equipo
        self.jugadores: [Jugador] = []

        # Opcional en el caso de que el equipo sea propio
        if not self.contrario:
            self.competencias: [Competencia] = []
            self.equiposRivales: [Equipo] = []
            self.ciclosEntrenamiento = []

        self.setJugadores()

    def getNombre(self):
        return self.nombreEquipo

    def getJugadores(self):
        return self.jugadores

    def setJugadores(self):
        self.jugadores = [
            Jugador(1, "Iván Alejandro Luna Hermosillo", "M", "Libero", 1, False),
            Jugador(2, "Sergio Ruvalcaba Lozano", "M", "Acomodador", 4, True),
            Jugador(3, "Brayan Alexis Aguilera de la Cruz", "M", "Opuesto", 5, False),
            Jugador(4, "Eduardo Velazco Ramírez", "M", "Banda", 6, False),
            Jugador(5, "José Raúl Ortega Rodríguez", "M", "Banda", 9, False),
            Jugador(6, "Víctor Román López", "M", "Central", 11, False),
            Jugador(7, "César Andrés Ramírez González", "M", "Central", 13, False),
            Jugador(8, "César Hazael Moreno Rodríguez", "M", "Libero", 14, False),
            Jugador(9, "Carlos Ruiz", "M", "Banda", 15, False),
            Jugador(10, "Iojan Leo Escobedo Velázquez", "M", "Banda", 17, False),
            Jugador(11, "Alan Manuel Márquez Álvarez", "M", "Central", 18, False)
        ]

    def insertarJugador(self, jugadorNuevo: Jugador):
        self.jugadores.append(jugadorNuevo)
        self.ordenarJugadores()
        print("Jugador insertado")

    def borrarJugador(self, id):
        for jugador in self.jugadores:
            if jugador.id == id:
                self.jugadores.remove(jugador)
                print("Jugador eliminado")
        self.ordenarJugadores()

    def editarJugador(self, jugadorEditado: Jugador):
        for i, jugador in enumerate(self.jugadores):
            if jugador.id == jugadorEditado.id:
                self.jugadores[i] = jugadorEditado
                print("Jugador editado")
        self.ordenarJugadores()

    def obtenerUltimoIdJugador(self):
        id = len(self.jugadores) + 1
        return id

    def obtenerGeneroEquipo(self):
        if self.rama == "Varonil":
            return "M"
        else:
            return "F"

    def ordenarJugadores(self):
        self.jugadores.sort(key=lambda x: x.noJugador)

    def checarJugadorRepetido(self, jugadorNuevo: Jugador):
        for jugador in self.jugadores:
            if jugador.getNumero() == jugadorNuevo.getNumero() or jugador.getNombre() == jugadorNuevo.getNombre():
                return True
        return False

    @classmethod
    def getJugadoresEquipo(cls, equipo: str):
        from Models.Entidades.Jugadores.Jugador import Jugador

        jugadores = []

        if equipo == "Gallos UAA":
            jugadores = [
                Jugador(1, "Iván Alejandro Luna Hermosillo", "M", "Libero", 1, False),
                Jugador(2, "Sergio Ruvalcaba Lozano", "M", "Acomodador", 4, True),
                Jugador(3, "Brayan Alexis Aguilera de la Cruz", "M", "Opuesto", 5, False),
                Jugador(4, "Eduardo Velazco Ramírez", "M", "Banda", 6, False),
                Jugador(5, "José Raúl Ortega Rodríguez", "M", "Banda", 9, False),
                Jugador(6, "Víctor Román López", "M", "Central", 11, False),
                Jugador(7, "César Andrés Ramírez González", "M", "Central", 13, False),
                Jugador(8, "César Hazael Moreno Rodríguez", "M", "Libero", 14, False),
                Jugador(9, "Carlos Ruiz", "M", "Banda", 15, False),
                Jugador(10, "Iojan Leo Escobedo Velázquez", "M", "Banda", 17, False),
                Jugador(11, "Alan Manuel Márquez Álvarez", "M", "Central", 18, False)
            ]
        elif equipo == "Águilas Reales UPA":
            jugadores = [
                Jugador(1, "Benjamín Esqueda Medrano", "M", "Central", 10, True),
                Jugador(2, "Jesús Ruvalcaba Lozano", "M", "Banda", 2, False),
                Jugador(3, "Daichi Guerrero", "M", "Acomodador", 5, False),
                Jugador(4, "José Moreno Prieto", "M", "Banda", 6, False),
                Jugador(5, "Ernesto Armando Pérez Pandas", "M", "Banda", 9, False)
            ]
        else:
            jugadores = [
                Jugador(1, "Dummy", "M", "Central", 1, False),
                Jugador(2, "Dummy", "M", "Banda", 2, False),
                Jugador(3, "Dummy", "M", "Acomodador", 3, False),
                Jugador(4, "Dummy", "M", "Banda", 4, True),
                Jugador(5, "Dummy", "M", "Banda", 5, False),
                Jugador(6, "Dummy", "M", "Banda", 6, False)
            ]

        return jugadores

    @classmethod
    def getEquipos(cls):
        equipos = [
            Equipo(1, "Gallos UAA", "Universitaria", "Varonil", "Institucional",
                   "Universidad Autónoma de Aguascalientes", False),
            Equipo(2, "Gallas UAA", "Universitaria", "Femenil", "Institucional",
                   "Universidad Autónoma de Aguascalientes", False),
            Equipo(3, "Lobas ENA", "Bachillerato", "Femenil", "Institucional",
                   "Escuela Normal de Aguascalientes", False),
            Equipo(4, "AGS Juvenil Mayor", "Juvenil Mayor", "Varonil", "Selectivo",
                   "Estado de Aguascalientes", False)
        ]

        return equipos
