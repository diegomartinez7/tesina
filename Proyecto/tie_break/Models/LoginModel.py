import requests

from Models.Entidades.Usuario import Usuario


class LoginModel(object):
    def __init__(self):
        # self.url = "http://localhost:8080/usuario/login"  # Url para backend en Spring
        self.url = "http://localhost:3000/api/usuarios/login"   # Url para backend en Nodejs

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
        id = respuesta[0].get("id")
        nombre = respuesta[0].get("nombre")
        apellido = respuesta[0].get("apellidos")
        username = respuesta[0].get("username")
        password = respuesta[0].get("password")
        rol = respuesta[0].get("rol")
        usuario = Usuario(nombre, apellido, username, rol, password)
        usuario.setId(id)
        return usuario
