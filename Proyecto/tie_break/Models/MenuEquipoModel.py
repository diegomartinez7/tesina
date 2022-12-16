from Models.Entidades.Equipo import Equipo
from Models.Entidades.Jugadores.Jugador import Jugador
from Models.Entidades.Competencia import Competencia


class MenuEquipoModel(object):
    def __init__(self, equipo: Equipo):
        self.equipo: Equipo = equipo
        self.jugadores = self.equipo.getJugadores()

    def getJugadores(self):
        return self.jugadores

    def insertarJugador(self, jugador: {}):
        id = self.equipo.obtenerUltimoIdJugador()
        nombre = jugador.get("nombre")
        genero = self.equipo.obtenerGeneroEquipo()
        posicion = jugador.get("posicion")
        numero = int(jugador.get("numero"))
        capitan = jugador.get("capitan")
        nuevoJugador = Jugador(nombre, genero, posicion, numero, capitan)
        if self.equipo.checarJugadorRepetido(nuevoJugador):
            return False
        else:
            self.equipo.insertarJugador(nuevoJugador)
            return True

    def editarJugador(self, jugador):
        self.equipo.editarJugador(jugador)

    def borrarJugador(self, jugador):
        self.equipo.borrarJugador(jugador.getId())

    def insertarRival(self, rival: {}):
        nombre = rival.get("nombre_equipo")
        entidad = rival.get("nombre_entidad")
        categoria = rival.get("categoria")
        rama = rival.get("rama")
        tipo = rival.get("tipo_equipo")
        nuevoEquipo = Equipo(nombre, categoria, rama, tipo, entidad, True)
        if self.equipo.checarRivalRepetido(nuevoEquipo):
            return False
        else:
            self.equipo.insertarRival(nuevoEquipo)
            return True

    def editarRival(self, rival):
        self.equipo.editarRival(rival)

    def borrarRival(self, rival):
        self.equipo.borrarRival(rival)

    def insertarCompetencia(self, competencia: {}):
        nombre = competencia.get("nombre")
        inicio = competencia.get("fecha_inicio")
        fin = competencia.get("fecha_fin")
        activa = competencia.get("activa")
        tipo = competencia.get("id_tipo")
        nuevaCompetencia = Competencia(tipo, nombre, inicio, fin, activa)
        if self.equipo.checarCompetenciaRepetida(nuevaCompetencia):
            return False
        else:
            self.equipo.insertarCompetencia(nuevaCompetencia)
            return True

    def editarCompetencia(self, competencia):
        self.equipo.editarCompetencia(competencia)

    def borrarCompetencia(self, competencia):
        self.equipo.borrarCompetencia(competencia)

    def getCompetencias(self):
        return self.equipo.getCompetencias()

    def getPruebas(self):
        return self.equipo.getPruebasFisicas()

    def getRivales(self):
        return self.equipo.getRivales()

    def getJugadoresContrarios(self, equipoBuscado: Equipo):
        for equipo in self.equipo.getRivales():
            if equipo.getNombre() == equipoBuscado.getNombre():
                return equipo.getJugadores()

    @classmethod
    def getJugadoresEquipo(cls, equipo):
        return Equipo.getJugadores(equipo)
