class TipoCompetencia(object):
    def __init__(self, nombre):
        self.id = 0
        self.nombre = nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id
