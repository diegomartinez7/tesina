from Models.Entidades.AccionesPartido.AccionPartido import AccionPartido


class Remate(AccionPartido):
    def __init__(self, idPunto, idJugador, efectividad, zonaInicio, zonaFinalizacion, limpio):
        super().__init__(idPunto, idJugador, efectividad, zonaInicio, zonaFinalizacion)
        self.limpio = limpio