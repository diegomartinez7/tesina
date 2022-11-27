from flet import Page

from Views.MenuSeleccionOCreacionView import MenuSeleccionOCreacionVista


class MenuSeleccionOCreacionControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.vista = MenuSeleccionOCreacionVista(self.page)

    def iniciarVista(self):
        self.page.vertical_alignment = "center"
        self.page.add(self.vista)
        print(self.page.session.get("usuario"))

    def seleccionarEquipo(self):
        self.limpiarVista()
        from Controllers.SeleccionarEquipoControl import SeleccionarEquipoControlador
        seleccionar = SeleccionarEquipoControlador(self.page)
        seleccionar.iniciarVista()

    def cerrarSesion(self):
        self.limpiarVista()
        self.page.session.remove("usuario")
        from Controllers.LoginControl import LoginControlador
        login = LoginControlador(self.page)
        login.iniciarVista()

    def limpiarVista(self):
        self.page.controls.pop()
        self.page.update()
