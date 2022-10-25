class Jugador:
    def __init__(self, id, nombre, genero, posicion, noJugador, capitan, equipo):
        self.id: int = id
        self.nombre: str = nombre
        self.genero: str = genero
        self.posicion: str = posicion
        self.noJugador: int = noJugador
        self.capitan: bool = capitan
        self.equipo: str = equipo

    def getNombre(self):
        return self.nombre

    def getGenero(self):
        return self.genero

    def getPosicion(self):
        return self.posicion

    def getNumero(self):
        return self.noJugador

    def isCapitan(self):
        return self.capitan
