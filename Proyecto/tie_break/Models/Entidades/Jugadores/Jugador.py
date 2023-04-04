class Jugador:
    def __init__(self, nombre, genero, posicion, noJugador, capitan):
        self.id: int = 0
        self.nombre: str = nombre
        self.genero: str = genero
        self.posicion: str = posicion
        self.noJugador: int = noJugador
        self.capitan: bool = capitan

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def getGenero(self):
        return self.genero

    def setGenero(self, genero: str):
        self.genero = genero

    def getPosicion(self):
        return self.posicion

    def setPosicion(self, posicion: str):
        self.posicion = posicion

    def getNumero(self):
        return self.noJugador

    def setNumero(self, numero: int):
        self.noJugador = numero

    def isCapitan(self):
        return self.capitan

    def setCapitan(self, cap: bool):
        self.capitan = cap

    def toString(self):
        print("Id: " + str(self.id))
        print("Jugador: " + self.nombre)
        print("Numero: " + str(self.noJugador))
        print("Posicion: " + self.posicion)
        print("Genero: " + self.genero)
        print("Capitán: " + str(self.capitan))
