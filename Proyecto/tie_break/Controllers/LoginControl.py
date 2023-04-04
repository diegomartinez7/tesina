from flet import Page

from Models.LoginModel import LoginModel
from Views.LoginView import LoginVista


class LoginControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.vista = LoginVista(self.page)
        self.modelo = LoginModel()

    def iniciarVista(self):
        self.page.vertical_alignment = "center"
        self.page.add(self.vista)

    def iniciarSesion(self):
        self.limpiarVista()
        from Controllers.MenuSeleccionOCreacionControl import MenuSeleccionOCreacionControlador
        menuSeleccion = MenuSeleccionOCreacionControlador(self.page)
        menuSeleccion.iniciarVista()

    def registrarse(self):
        self.page.controls.pop()
        self.page.update()
        from Controllers.RegistroControl import RegistroControlador
        registro = RegistroControlador(self.page)
        registro.iniciarVista()

    def revisarCredenciales(self, usr, pswd):
        respuesta = self.modelo.revisarCredenciales(usr, pswd)
        if respuesta is not None:
            self.page.session.set("usuario", respuesta)
            return True
        else:
            return False

    def limpiarVista(self):
        self.page.controls.pop()
        self.page.update()
