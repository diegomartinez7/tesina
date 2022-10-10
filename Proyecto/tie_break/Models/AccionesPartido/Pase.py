from Models.AccionesPartido.AccionPartido import AccionPartido


class Pase(AccionPartido):
    def __init__(self, idPunto, idJugador, efectividad, zonaInicio, zonaFinalizacion, tipo):
        super().__init__(idPunto, idJugador, efectividad, zonaInicio, zonaFinalizacion)
        self.tipo = tipo