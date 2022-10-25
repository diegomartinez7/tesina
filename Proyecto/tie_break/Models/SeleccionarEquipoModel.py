from Models.Entidades.Jugadores.JugadorPropio import JugadorPropio

class SeleccionarEquipoModel(object):
    def __init__(self):
        self.jugadores: [JugadorPropio] = []

    def getJugadores(self):
        self.jugadores = None