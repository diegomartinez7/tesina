from Models.Entidades.AccionesPartido.AccionPartido import AccionPartido


class Punto:
    def __init__(self, idSet, marcadorPropio, marcadorContrario):
        self.id = 0
        self.idSet = idSet
        self.resultado = False
        self.marcadorPropio = marcadorPropio
        self.marcadorContrario = marcadorContrario

        self.accionesPartido: [AccionPartido] = []

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setResultado(self, resultado):
        self.resultado = resultado

    def agregarAccion(self, accion: AccionPartido):
        self.accionesPartido.append(accion)