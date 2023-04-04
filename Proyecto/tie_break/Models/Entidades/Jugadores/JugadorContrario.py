from Models.Entidades.Jugadores.Jugador import Jugador


class JugadorContrario(Jugador):
    def __init__(self, nombre, genero, posicion, noJugador, capitan):
        super().__init__(nombre, genero, posicion, noJugador, capitan)
