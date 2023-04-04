from Models.Entidades.Sets.Set import Set

class Partido:
    def __init__(self, idEquipo, idContrario, idCompetencia, ubicacion, fecha):
        self.id = 0
        self.idEquipo = idEquipo
        self.idContrario = idContrario
        self.idCompetencia = idCompetencia
        self.ubicacion = ubicacion
        self.fecha = fecha
        self.resultado = False

        self.sets = []

    def getUbicacion(self):
        return self.ubicacion

    def getFecha(self):
        return self.fecha

    def setResultado(self, resultado):
        self.resultado = resultado

    def getResultado(self):
        return self.resultado

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getIdCompetencia(self):
        return self.idCompetencia

    def agregarSet(self, set: Set):
        self.sets.append(set)