from Models.Entidades.ActividadesPartido.ActividadPartido import ActividadPartido


class Tiempo(ActividadPartido):
    def __init__(self, id, idSet, marcadorPropio, marcadorContrario, noTiempo):
        super().__init__(id, idSet, marcadorPropio, marcadorContrario)
        self.noTiempo = noTiempo