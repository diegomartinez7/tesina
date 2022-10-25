from flet import Page

from Views.RegistroView import RegistroVista


class RegistroControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.vista = RegistroVista(self.page)

    def iniciarVista(self):
        self.page.vertical_alignment = "center"
        self.page.add(self.vista)

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



