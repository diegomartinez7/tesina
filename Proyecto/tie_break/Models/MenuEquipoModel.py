from Models.Entidades.Equipo import Equipo
from Models.Entidades.Jugadores.Jugador import Jugador


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
        nuevoJugador = Jugador(id, nombre, genero, posicion, numero, capitan)
        if self.equipo.checarJugadorRepetido(nuevoJugador):
            return False
        else:
            self.equipo.insertarJugador(nuevoJugador)
            return True

    def editarJugador(self, jugador):
        self.equipo.editarJugador(jugador)

    def borrarJugador(self, jugador):
        self.equipo.borrarJugador(jugador.getId())

    @classmethod
    def getJugadoresEquipo(cls, equipo):
        return Equipo.getJugadores(equipo)
