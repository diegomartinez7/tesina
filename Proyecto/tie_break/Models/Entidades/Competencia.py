from Models.Entidades.Partido import Partido


class Competencia:
    def __init__(self, idTipo, nombre, inicio, fin, activa):
        self.id: int = 0
        self.idTipo: int = idTipo
        self.nombre: str = nombre
        self.inicio: str = inicio
        self.fin: str = fin
        self.activa: bool = activa

        self.partidos: [Partido] = []

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setInicio(self, inicio):
        self.inicio = inicio

    def getInicio(self):
        return self.inicio

    def setFin(self, fin):
        self.fin = fin

    def getFin(self):
        return self.fin

    def setActiva(self, activa):
        self.activa = activa

    def isActiva(self):
        return self.activa

    def setTipo(self, tipo):
        self.idTipo = tipo

    def getTipo(self):
        return self.idTipo

    def insertarPartido(self, partido: Partido):
        self.partidos.append(partido)

    def getPartidoId(self, id):
        for partido in self.partidos:
            if partido.getId() == id:
                return partido

    def obtenerUltimoIdPartdo(self):
        id = len(self.partidos) + 1
        return id