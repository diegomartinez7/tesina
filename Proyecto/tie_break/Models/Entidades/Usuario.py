class Usuario(object):
    def __init__(self, nombre: str, apellidos: str, usuario: str, rol: str, password: str):
        self.id = 0
        self.nombre: str = nombre
        self.apellidos: str = apellidos
        self.usuario: str = usuario
        self.rol: str = rol
        self.password: str = password

    def getNombreCompleto(self):
        return self.nombre + " " + self.apellidos

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def toString(self):
        print(f"Usuario: {self.getNombreCompleto()}")
        print(f"ID: {self.getId()}")
