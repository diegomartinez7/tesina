from flet import Page

from Views.LoginView import LoginVista


class LoginControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.vista = LoginVista(self.page)

    def iniciarVista(self):
        self.page.vertical_alignment = "center"
        self.page.add(self.vista)

    def iniciarSesion(self):
        self.page.controls.pop()
        self.page.update()
        from Controllers.MenuSeleccionOCreacionControl import MenuSeleccionOCreacionControlador
        menuSeleccion = MenuSeleccionOCreacionControlador(self.page)
        menuSeleccion.iniciarVista()

    def registrarse(self):
        self.page.controls.pop()
        self.page.update()
        from Controllers.RegistroControl import RegistroControlador
        registro = RegistroControlador(self.page)
        registro.iniciarVista()
