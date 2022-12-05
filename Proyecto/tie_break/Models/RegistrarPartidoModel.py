from Models.Entidades.Equipo import Equipo


class RegistrarPartidoModel(object):
    def __init__(self, equipo: Equipo, equipoContrario: Equipo):
        self.equipoPropio = equipo
        self.equipoContrario = equipoContrario

    def getNombreEquipoPropio(self):
        return self.equipoPropio.getNombre()

    def getJugadoresPropios(self):
        return self.equipoPropio.getJugadores()

    def getNombreEquipoContrario(self):
        return self.equipoContrario.getNombre()

    def getJugadoresContrarios(self):
        return self.equipoContrario.getJugadores()
