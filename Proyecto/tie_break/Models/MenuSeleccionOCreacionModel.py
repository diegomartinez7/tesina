from Models.Entidades.Usuario import Usuario


class MenuSeleccionOCreacionModel(object):
    def __init__(self, usuario: Usuario):
        self.usuario = usuario

    def getNombreUsuario(self):
        return self.usuario.getNombreCompleto()

    def getIdUsuario(self):
        return self.usuario.getId()
