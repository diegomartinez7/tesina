from Models.Entidades.Sets.Set import Set


class SetDesempate(Set):
    def __init__(self, id, noSet, idPartido, marcadorPropio, marcadorContrario, puntosObjetivo, resultado,
                 marcadorPropioAlCambio, marcadorContrarioAlCambio):
        super().__init__(id, noSet, idPartido, marcadorPropio, marcadorContrario, puntosObjetivo, resultado)
        self.marcadorPropioAlCambio = marcadorPropioAlCambio
        self.marcadorContrarioAlCambio = marcadorContrarioAlCambio