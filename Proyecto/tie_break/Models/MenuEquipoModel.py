from Models.Entidades.Equipo import Equipo


class MenuEquipoModel(object):
    def __init__(self):
        self.equipo: Equipo = None
        self.jugadores = []

    @classmethod
    def getJugadores(cls, equipo):
        return Equipo.getJugadores(equipo)
