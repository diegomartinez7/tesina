from Models.Entidades.Equipo import Equipo
from Models.Entidades.Partido import Partido


class RegistrarPartidoModel(object):
    def __init__(self, equipo: Equipo, equipoContrario: Equipo):
        self.equipoPropio = equipo
        self.equipoContrario = equipoContrario
        self.partido: Partido = None

    def getNombreEquipoPropio(self):
        return self.equipoPropio.getNombre()

    def getJugadoresPropios(self):
        return self.equipoPropio.getJugadores()

    def getNombreEquipoContrario(self):
        return self.equipoContrario.getNombre()

    def getJugadoresContrarios(self):
        return self.equipoContrario.getJugadores()

    def setPartido(self, partido: Partido):
        self.partido = partido

    def getPartido(self):
        return self.partido

    def agregarSet(self, set):
        self.partido.agregarSet(set)
