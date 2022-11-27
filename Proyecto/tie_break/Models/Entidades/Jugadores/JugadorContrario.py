from Models.Entidades.Jugadores.Jugador import Jugador


class JugadorContrario(Jugador):
    def __init__(self, id, nombre, genero, posicion, noJugador, capitan):
        super().__init__(id, nombre, genero, posicion, noJugador, capitan)
