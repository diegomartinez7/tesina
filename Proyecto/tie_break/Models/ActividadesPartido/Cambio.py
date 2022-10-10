from Models.ActividadesPartido.ActividadPartido import ActividadPartido


class Cambio(ActividadPartido):
    def __init__(self, id, idSet, marcadorPropio, marcadorContrario, idJugadorEntrante, idJugadorSaliente):
        super().__init__(id, idSet, marcadorPropio, marcadorContrario)
        self.idJugadorEntrante = idJugadorEntrante
        self.idJugadorSaliente = idJugadorSaliente