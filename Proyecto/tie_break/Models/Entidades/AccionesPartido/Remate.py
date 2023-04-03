from Models.Entidades.AccionesPartido.AccionPartido import AccionPartido


class Remate(AccionPartido):
    def __init__(self, idPunto, idJugador, efectividad, zonaInicio, zonaFinalizacion, contrario):
        super().__init__(idPunto, idJugador, efectividad, zonaInicio, zonaFinalizacion, contrario)
        self.limpio = None