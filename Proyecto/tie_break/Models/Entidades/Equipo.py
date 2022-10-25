class Equipo:
    def __init__(self, id, nombreEquipo, categoria, rama, tipoEquipo, nombreEntidad, contrario):
        self.id = id
        self.nombreEquipo = nombreEquipo
        self.categoria = categoria
        self.rama = rama
        self.tipoEquipo = tipoEquipo
        self.nombreEntidad = nombreEntidad
        self.contrario = contrario

    @classmethod
    def getJugadores(cls, equipo: str):
        from Models.Entidades.Jugadores.Jugador import Jugador

        jugadores = []

        if equipo == "Gallos UAA":
            jugadores = [
                Jugador(1, "Iván Alejandro Luna Hermosillo", "M", "Libero", 1, False, equipo),
                Jugador(2, "Sergio Ruvalcaba Lozano", "M", "Acomodador", 4, True, equipo),
                Jugador(3, "Brayan Alexis Aguilera de la Cruz", "M", "Opuesto", 5, False, equipo),
                Jugador(4, "Eduardo Velazco Ramírez", "M", "Banda", 6, False, equipo),
                Jugador(5, "José Raúl Ortega Rodríguez", "M", "Banda", 9, False, equipo),
                Jugador(6, "Víctor Román López", "M", "Central", 11, False, equipo),
                Jugador(7, "César Andrés Ramírez González", "M", "Central", 13, False, equipo),
                Jugador(8, "César Hazael Moreno Rodríguez", "M", "Libero", 14, False, equipo),
                Jugador(9, "Carlos Ruiz", "M", "Banda", 15, False, equipo),
                Jugador(10, "Iojan Leo Escobedo Velázquez", "M", "Banda", 17, False, equipo),
                Jugador(11, "Alan Manuel Márquez Álvarez", "M", "Central", 18, False, equipo)
            ]
        elif equipo == "Águilas Reales UPA":
            jugadores = [
                Jugador(1, "Benjamín Esqueda Medrano", "M", "Central", 10, True, equipo),
                Jugador(2, "Jesús Ruvalcaba Lozano", "M", "Banda", 2, False, equipo),
                Jugador(3, "Daichi Guerrero", "M", "Acomodador", 5, False, equipo),
                Jugador(4, "José Moreno Prieto", "M", "Banda", 6, False, equipo),
                Jugador(5, "Ernesto Armando Pérez Pandas", "M", "Banda", 9, False, equipo)
            ]
        else:
            jugadores = [
                Jugador(1, "Dummy", "M", "Central", 1, False, equipo),
                Jugador(2, "Dummy", "M", "Banda", 2, False, equipo),
                Jugador(3, "Dummy", "M", "Acomodador", 3, False, equipo),
                Jugador(4, "Dummy", "M", "Banda", 4, True, equipo),
                Jugador(5, "Dummy", "M", "Banda", 5, False, equipo),
                Jugador(6, "Dummy", "M", "Banda", 6, False, equipo)
            ]

        return jugadores

    @classmethod
    def getEquipos(cls):
        return [
            "Gallos UAA",
            "Águilas Reales UPA",
            "Águilas ITA",
            "Lobos UTA",
            "Linces UTR",
            "Pumas UNAM",
            "Tigres UNAM"
        ]
