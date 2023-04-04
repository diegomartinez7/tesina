import requests

from Models.Entidades.Usuario import Usuario


class RegistroModel(object):
    def __init__(self):
        self.nuevoUsuario: Usuario = None
        # self.urlBack = "http://localhost:8080/usuario"
        self.urlBack = "http://localhost:3000/api/usuarios"

    def registrarUsuario(self, usr: {}):
        nombre = usr.get("nombre")
        apellido = usr.get("apellido")
        usuario = usr.get("usuario")
        rol = usr.get("rol")
        password = usr.get("password")
        self.nuevoUsuario = Usuario(nombre, apellido, usuario, rol, password)

        jsonUsr = {
          "apellidos": apellido,
          "nombre": nombre,
          "password": password,
          "rol": rol,
          "username": usuario
        }

        resultado = requests.post(self.urlBack, jsonUsr)

        print(resultado)
