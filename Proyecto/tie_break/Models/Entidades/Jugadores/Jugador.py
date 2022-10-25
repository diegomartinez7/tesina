class Jugador:
    def __init__(self, id, nombre, genero, posicion, noJugador, capitan):
        self.id: int = id
        self.nombre: str = nombre
        self.genero: str = genero
        self.posicion: str = posicion
        self.noJugador: int = noJugador
        self.capitan: bool = capitan