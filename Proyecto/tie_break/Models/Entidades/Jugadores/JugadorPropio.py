from Models.Entidades.Jugadores.Jugador import Jugador


class JugadorPropio(Jugador):
    def __init__(self, id, nombre, genero, posicion, noJugador, lesiones, titular):
        super().__init__(id, nombre, genero, posicion, noJugador)
        