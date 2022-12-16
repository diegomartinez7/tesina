import requests

from Models.Entidades.Usuario import Usuario


class LoginModel(object):
    def __init__(self):
        self.url = "http://localhost:8080/usuario/login"

    def revisarCredenciales(self, usr: str, pswd: str):
        jsonCredenciales = {
            "username": usr,
            "password": pswd
        }

        respuesta = requests.post(self.url, jsonCredenciales)
        print(respuesta.text)
        if respuesta.text == "":
            print("respuesta vacía, credenciales inexistentes")
            return None
        else:
            print("credenciales válidas")
            return self.crearUsuarioRespuesta(respuesta.json())

    def crearUsuarioRespuesta(self, respuesta):
        id = respuesta.get("id")
        nombre = respuesta.get("nombre")
        apellido = respuesta.get("apellidos")
        username = respuesta.get("username")
        password = respuesta.get("password")
        rol = respuesta.get("rol")
        usuario = Usuario(nombre, apellido, username, rol, password)
        usuario.setId(id)
        return usuario
