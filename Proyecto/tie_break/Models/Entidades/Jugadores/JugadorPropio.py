from Models.Entidades.Jugadores.Jugador import Jugador


class JugadorPropio(Jugador):
    def __init__(self, nombre, genero, posicion, noJugador, capitan):
        super().__init__(nombre, genero, posicion, noJugador, capitan)
        self.lesiones = False
        self.titular = False

    def setLesion(self, lesion):
        self.lesiones = lesion

    def setTitular(self, titularidad):
        self.titular = titularidad

    def getLesiones(self):
        return self.lesiones

    def getTitular(self):
        return self.titular