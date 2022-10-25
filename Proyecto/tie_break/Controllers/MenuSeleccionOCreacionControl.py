from flet import Page

from Views.MenuSeleccionOCreacionView import MenuSeleccionOCreacionVista


class MenuSeleccionOCreacionControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.vista = MenuSeleccionOCreacionVista(self.page)

    def iniciarVista(self):
        self.page.vertical_alignment = "center"
        self.page.add(self.vista)

    def seleccionarEquipo(self):
        self.page.controls.pop()
        self.page.update()
        from Controllers.SeleccionarEquipoControl import SeleccionarEquipoControlador
        seleccionar = SeleccionarEquipoControlador(self.page)
        seleccionar.iniciarVista()

    def cerrarSesion(self):
        self.page.controls.pop()
        self.page.update()
        from Controllers.LoginControl import LoginControlador
        login = LoginControlador(self.page)
        login.iniciarVista()