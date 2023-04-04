from flet import Page

from Models.MenuSeleccionOCreacionModel import MenuSeleccionOCreacionModel
from Views.MenuSeleccionOCreacionView import MenuSeleccionOCreacionVista


class MenuSeleccionOCreacionControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.vista = MenuSeleccionOCreacionVista(self.page)
        self.modelo = MenuSeleccionOCreacionModel(self.page.session.get("usuario"))

    def iniciarVista(self):
        self.page.vertical_alignment = "center"
        self.page.add(self.vista)

    def obtenerNombreEntrenador(self):
        return self.modelo.getNombreUsuario()

    def seleccionarEquipo(self):
        self.limpiarVista()
        from Controllers.SeleccionarEquipoControl import SeleccionarEquipoControlador
        seleccionar = SeleccionarEquipoControlador(self.page)
        seleccionar.iniciarVista()

    def crearEquipo(self):
        self.limpiarVista()
        from Controllers.RegistrarEquipoControl import RegistrarEquipoControlador
        registrar = RegistrarEquipoControlador(self.page)
        registrar.iniciarVista()

    def cerrarSesion(self):
        self.limpiarVista()
        self.page.session.remove("usuario")
        from Controllers.LoginControl import LoginControlador
        login = LoginControlador(self.page)
        login.iniciarVista()

    def limpiarVista(self):
        self.page.controls.pop()
        self.page.update()
