from Models.Entidades.Jugadores.Jugador import Jugador
from Models.Entidades.Competencia import Competencia

from Models.Entidades.Pruebas.PruebaEquipo import PruebaEquipo


class Equipo:
    def __init__(self, nombreEquipo, categoria, rama, tipoEquipo, nombreEntidad, contrario):
        # Información del Equipo
        self.id: int = 0
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
            self.pruebasFisicas: [PruebaEquipo] = []
            self.setCompetenciasIniciales()
            self.setRivalesIniciales()
            self.setPruebasFisicasIniciales()

        self.setJugadoresIniciales()

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setNombre(self, nombre):
        self.nombreEquipo = nombre

    def getNombre(self):
        return self.nombreEquipo

    def setCategoria(self, categoria):
        self.categoria = categoria

    def getCategoria(self):
        return self.categoria

    def setRama(self, rama):
        self.rama = rama

    def getRama(self):
        return self.rama

    def setTipoEquipo(self, tipo):
        self.tipoEquipo = tipo

    def getTipoEquipo(self):
        return self.tipoEquipo

    def setEntidadRepresentada(self, entidad):
        self.nombreEntidad = entidad

    def getEntidadRepresentada(self):
        return self.nombreEntidad

    def getJugadores(self):
        return self.jugadores

    def setJugadores(self, jugadores: []):
        self.jugadores = jugadores
        self.ordenarJugadores()

    def getCompetencias(self):
        return self.competencias

    def setCompetencias(self, competencias: []):
        self.competencias = competencias

    def getPruebasFisicas(self):
        return self.pruebasFisicas

    def setPruebasFisicas(self, pruebas: []):
        self.pruebasFisicas = pruebas

    def getRivales(self):
        return self.equiposRivales

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

    def insertarRival(self, nuevoRival):
        self.equiposRivales.append(nuevoRival)
        print("Rival Insertado")

    def editarRival(self, rivalEditado):
        for i, rival in enumerate(self.equiposRivales):
            if(rival.getNombre() == rivalEditado.getNombre() and rival.getCategoria() == rivalEditado.getCategoria()
                    and rival.getRama() == rivalEditado.getRama()
                    and rival.getTipoEquipo() == rivalEditado.getTipoEquipo()
                    and rival.getEntidadRepresentada() == rivalEditado.getEntidadRepresentada()):
                self.equiposRivales[i] = rivalEditado
                print("Rival editado")

    def borrarRival(self, rivalBorrado):
        for rival in self.equiposRivales:
            if (rival.getNombre() == rivalBorrado.getNombre() and rival.getCategoria() == rivalBorrado.getCategoria()
                    and rival.getRama() == rivalBorrado.getRama()
                    and rival.getTipoEquipo() == rivalBorrado.getTipoEquipo()
                    and rival.getEntidadRepresentada() == rivalBorrado.getEntidadRepresentada()):
                self.equiposRivales.remove(rival)
                print("Rival eliminado")

    def checarRivalRepetido(self, nuevoRival):
        for rival in self.equiposRivales:
            if(rival.getNombre() == nuevoRival.getNombre() and rival.getCategoria() == nuevoRival.getCategoria()
                    and rival.getRama() == nuevoRival.getRama() and rival.getTipoEquipo() == nuevoRival.getTipoEquipo()
                    and rival.getEntidadRepresentada() == nuevoRival.getEntidadRepresentada()):
                return True
        return False

    def insertarCompetencia(self, competencia):
        self.competencias.append(competencia)
        print("Competencia insertada")

    def editarCompetencia(self, competenciaEditada):
        for i, competencia in enumerate(self.competencias):
            if (competencia.getNombre() == competenciaEditada.getNombre()
                    and competencia.getInicio() == competenciaEditada.getInicio()
                    and competencia.getFin() == competenciaEditada.getFin()
                    and competencia.getTipo() == competenciaEditada.getTipo()):
                self.competencias[i] = competenciaEditada
                print("Competencia editada")

    def borrarCompetencia(self, competenciaBorrada):
        for competencia in self.competencias:
            if (competencia.getNombre() == competenciaBorrada.getNombre()
                    and competencia.getInicio() == competenciaBorrada.getInicio()
                    and competencia.getFin() == competenciaBorrada.getFin()
                    and competencia.getTipo() == competenciaBorrada.getTipo()):
                self.competencias.remove(competencia)
                print("Competencia eliminada")

    def checarCompetenciaRepetida(self, nuevaCompetencia):
        for competencia in self.competencias:
            if(competencia.getNombre() == nuevaCompetencia.getNombre()
                    and competencia.getInicio() == nuevaCompetencia.getInicio()
                    and competencia.getFin() == nuevaCompetencia.getFin()
                    and competencia.getTipo() == nuevaCompetencia.getTipo()):
                return True
        return False

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

    def setJugadoresIniciales(self):
        if not self.contrario:
            self.jugadores = [
                Jugador("Iván Alejandro Luna Hermosillo", "M", "Libero", 1, False),
                Jugador("Sergio Ruvalcaba Lozano", "M", "Acomodador", 4, True),
                Jugador("Brayan Alexis Aguilera de la Cruz", "M", "Opuesto", 5, False),
                Jugador("Eduardo Velazco Ramírez", "M", "Banda", 6, False),
                Jugador("José Raúl Ortega Rodríguez", "M", "Banda", 9, False),
                Jugador("Víctor Román López", "M", "Central", 11, False),
                Jugador("César Andrés Ramírez González", "M", "Central", 13, False),
                Jugador("César Hazael Moreno Rodríguez", "M", "Libero", 14, False),
                Jugador("Carlos Ruiz", "M", "Banda", 15, False),
                Jugador("Iojan Leo Escobedo Velázquez", "M", "Banda", 17, False),
                Jugador("Alan Manuel Márquez Álvarez", "M", "Central", 18, False)
            ]
        else:
            self.jugadores = [
                Jugador("Iván Alejandro Luna Hermosillo", "M", "Libero", 1, False),
                Jugador("Sergio Ruvalcaba Lozano", "M", "Acomodador", 4, True),
                Jugador("Brayan Alexis Aguilera de la Cruz", "M", "Opuesto", 5, False),
                Jugador("Eduardo Velazco Ramírez", "M", "Banda", 6, False),
                Jugador("César Hazael Moreno Rodríguez", "M", "Libero", 14, False),
                Jugador("Carlos Ruiz", "M", "Banda", 15, False),
                Jugador("Iojan Leo Escobedo Velázquez", "M", "Banda", 17, False),
                Jugador("Alan Manuel Márquez Álvarez", "M", "Central", 18, False)
            ]

    def setRivalesIniciales(self):
        self.equiposRivales = [
            Equipo("Celtas", "Libre", "Varonil", "Club",
                   "Club Celtas Voleibol", True),
            Equipo("Toros", "Libre", "Varonil", "Club",
                   "Club Toros Voleibol", True),
            Equipo("TESM Querétaro", "Universitaria", "Varonil", "Institucional",
                   "TESM Campus Querétaro", True),
            Equipo("Anahuac Querétaro", "Universitaria", "Varonil", "Institucional",
                   "Universidad Anáhuac Querétaro", True)
        ]

    def setCompetenciasIniciales(self):
        self.competencias = [
            Competencia(1, "Torneo del pavo 2019", "10-Oct-2019", "20-Dic-2019", False),
            Competencia(3, "Partidos Amistosos 2022", "01-Ene-2022", "-", True),
            Competencia(2, "Liga Regional CONDE 2022", "13-Ago-2022", "12-Nov-2022", False)
        ]

    def setPruebasFisicasIniciales(self):
        self.pruebasFisicas = [
            PruebaEquipo(1, self.id, "Pruebas Finales Enero 2022", "23-Ene-2022", "Competitiva", True),
            PruebaEquipo(2, self.id, "Pruebas Pre Vacaciones Diciembre 2022", "13-Dic-2022", "Precompetitiva", False),
            PruebaEquipo(3, self.id, "Pruebas Post Vacaciones Enero 2022", "03-Ene-2022", "Competitiva", False),
        ]

    @classmethod
    def getJugadoresEquipo(cls, equipo: str):
        from Models.Entidades.Jugadores.Jugador import Jugador

        jugadores = []

        if equipo == "Gallos UAA":
            jugadores = [
                Jugador("Iván Alejandro Luna Hermosillo", "M", "Libero", 1, False),
                Jugador("Sergio Ruvalcaba Lozano", "M", "Acomodador", 4, True),
                Jugador("Brayan Alexis Aguilera de la Cruz", "M", "Opuesto", 5, False),
                Jugador("Eduardo Velazco Ramírez", "M", "Banda", 6, False),
                Jugador("José Raúl Ortega Rodríguez", "M", "Banda", 9, False),
                Jugador("Víctor Román López", "M", "Central", 11, False),
                Jugador("César Andrés Ramírez González", "M", "Central", 13, False),
                Jugador("César Hazael Moreno Rodríguez", "M", "Libero", 14, False),
                Jugador("Carlos Ruiz", "M", "Banda", 15, False),
                Jugador("Iojan Leo Escobedo Velázquez", "M", "Banda", 17, False),
                Juga("Alan Manuel Márquez Álvarez", "M", "Central", 18, False)
            ]
        elif equipo == "Águilas Reales UPA":
            jugadores = [
                Jugador("Benjamín Esqueda Medrano", "M", "Central", 10, True),
                Jugador("Jesús Ruvalcaba Lozano", "M", "Banda", 2, False),
                Jugador("Daichi Guerrero", "M", "Acomodador", 5, False),
                Jugador("José Moreno Prieto", "M", "Banda", 6, False),
                Jugador("Ernesto Armando Pérez Pandas", "M", "Banda", 9, False)
            ]
        else:
            jugadores = [
                Jugador("Dummy", "M", "Central", 1, False),
                Jugador("Dummy", "M", "Banda", 2, False),
                Jugador("Dummy", "M", "Acomodador", 3, False),
                Jugador("Dummy", "M", "Banda", 4, True),
                Jugador("Dummy", "M", "Banda", 5, False),
                Jugador("Dummy", "M", "Banda", 6, False)
            ]

        return jugadores

    @classmethod
    def getEquipos(cls):
        equipos = [
            Equipo("Gallos UAA", "Universitaria", "Varonil", "Institucional",
                   "Universidad Autónoma de Aguascalientes", False),
            Equipo("Gallas UAA", "Universitaria", "Femenil", "Institucional",
                   "Universidad Autónoma de Aguascalientes", False),
            Equipo("Lobas ENA", "Bachillerato", "Femenil", "Institucional",
                   "Escuela Normal de Aguascalientes", False),
            Equipo("AGS Juvenil Mayor", "Juvenil Mayor", "Varonil", "Selectivo",
                   "Estado de Aguascalientes", False)
        ]

        return equipos
