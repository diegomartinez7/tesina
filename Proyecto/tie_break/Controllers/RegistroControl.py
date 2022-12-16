from flet import Page

from Models.RegistroModel import RegistroModel
from Views.RegistroView import RegistroVista


class RegistroControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.vista = RegistroVista(self.page)
        self.modelo = RegistroModel()

    def iniciarVista(self):
        self.page.vertical_alignment = "center"
        self.page.add(self.vista)

    def validarUsuarioVacio(self, usr: {}):
        if(usr.get("nombre") == "" or usr.get("apellido") == "" or usr.get("usuario") == ""
                or usr.get("password") == "" or usr.get("rol") == ""):
            return True
        else:
            return False

    def validarPasswords(self, password: str, confirmacionPassword: str):
        return password == confirmacionPassword

    def registrarUsuario(self, usr: {}):
        self.modelo.registrarUsuario(usr)

    def registrarse(self):
        self.page.controls.pop()
        self.page.update()
        from Controllers.LoginControl import LoginControlador
        login = LoginControlador(self.page)
        login.iniciarVista()

    def regresar(self):
        self.page.controls.pop()
        self.page.update()
        from Controllers.LoginControl import LoginControlador
        login = LoginControlador(self.page)
        login.iniciarVista()



