from flet import Page

from Views.SeleccionarEquipoView import SeleccionarEquipoVista
from Models.SeleccionarEquipoModel import SeleccionarEquipoModel


class SeleccionarEquipoControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.vista = None
        self.modelo = SeleccionarEquipoModel

    def iniciarVista(self):
        self.vista = SeleccionarEquipoVista(self.page)
        self.page.vertical_alignment = "center"
        self.page.add(self.vista)

    def obtenerEquipos(self):
        return self.modelo.getEquipos()

    def obtenerJugadores(self, equipo):
        return self.modelo.getJugadores(equipo)

    def regresar(self):
        self.page.controls.pop()
        self.page.update()
        from Controllers.MenuSeleccionOCreacionControl import MenuSeleccionOCreacionControlador
        menuSeleccion = MenuSeleccionOCreacionControlador(self.page)
        menuSeleccion.iniciarVista()
