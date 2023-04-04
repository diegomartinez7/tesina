from Models.Entidades.Punto import Punto


class Set:
    def __init__(self, noSet, idPartido, puntosObjetivo):
        self.id = 0
        self.noSet = noSet
        self.idPartido = idPartido
        self.marcadorPropio = 0
        self.marcadorContrario = 0
        self.puntosObjetivo = puntosObjetivo
        self.resultado = False

        self.puntos: [Punto] = []

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getNoSet(self):
        return self.noSet

    def setMarcadorPropio(self, marcador):
        self.marcadorPropio = marcador

    def getMarcadorPropio(self):
        return self.marcadorPropio

    def setMarcadorContrario(self, marcador):
        self.marcadorContrario = marcador

    def getMarcadorContrario(self):
        return self.marcadorContrario

    def setResultado(self, resultado):
        self.resultado = resultado

    def getResultado(self):
        return self.resultado

    def agregarPunto(self, punto: Punto):
        self.puntos.append(punto)
