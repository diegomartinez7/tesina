from Models.AccionesPartido.AccionPartido import AccionPartido


class Acomodo(AccionPartido):
    def __init__(self, idPunto, idJugador, efectividad, zonaInicio, zonaFinalizacion, idTipoAcomodo):
        super().__init__(idPunto, idJugador, efectividad, zonaInicio, zonaFinalizacion)
        self.idTipoAcomodo = idTipoAcomodo