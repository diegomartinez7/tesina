from Models.Entidades.Equipo import Equipo

class SeleccionarEquipoModel(object):
    def __init__(self):
        self.equipo: Equipo = None
        self.jugadores = []

    @classmethod
    def getJugadores(cls, equipo):
        return Equipo.getJugadoresEquipo(equipo)

    @classmethod
    def getEquipos(cls):
        return Equipo.getEquipos()
