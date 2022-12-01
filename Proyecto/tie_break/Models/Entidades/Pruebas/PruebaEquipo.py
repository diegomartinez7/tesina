from Models.Entidades.Pruebas import PruebaJugador


class PruebaEquipo:
    def __init__(self, id: int, idEquipo: int, nombre: str, fecha: str, ciclo: str, aplicada: bool):
        self.id: int = id
        self.idEquipo: int = idEquipo
        self.nombrePrueba: str = nombre
        self.fecha: str = fecha
        self.ciclo: str = ciclo
        self.aplicada: bool = aplicada

        self.pruebas: [PruebaJugador] = []

    def getNombre(self):
        return self.nombrePrueba

    def getFecha(self):
        return self.fecha

    def getCiclo(self):
        return self.ciclo

    def isAplicada(self):
        return self.aplicada

    def getPruebas(self):
        return self.pruebas
