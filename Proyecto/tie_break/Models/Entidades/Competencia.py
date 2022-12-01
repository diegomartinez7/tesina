class Competencia:
    def __init__(self, id, tipo, nombre, inicio, fin, activa):
        self.id: int = id
        self.tipo: str = tipo
        self.nombre: str = nombre
        self.inicio: str = inicio
        self.fin: str = fin
        self.activa: bool = activa

        self.partidos = []

    def getNombre(self):
        return self.nombre

    def getInicio(self):
        return self.inicio

    def getFin(self):
        return self.fin

    def isActiva(self):
        return self.activa

    def getTipo(self):
        return self.tipo