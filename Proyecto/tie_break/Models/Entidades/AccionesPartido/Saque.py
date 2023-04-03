from Models.Entidades.AccionesPartido.AccionPartido import AccionPartido


class Saque(AccionPartido):
    def __init__(self, idPunto, idJugador, efectividad, zonaInicio, zonaFinalizacion, contrario):
        super().__init__(idPunto, idJugador, efectividad, zonaInicio, zonaFinalizacion, contrario)
        self.tipo = "None"
