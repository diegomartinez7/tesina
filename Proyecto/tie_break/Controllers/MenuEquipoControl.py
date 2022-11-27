from flet import Page

from Views.MenuEquipoView import MenuEquipoVista
from Models.MenuEquipoModel import MenuEquipoModel


class MenuEquipoControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.modelo = MenuEquipoModel

    def iniciarVista(self):
        self.page.clean()
        self.vista = MenuEquipoVista(self.page)
        self.page.vertical_alignment = "start"
        self.page.add(self.vista)

    def obtenerJugadores(self, equipo):
        return self.modelo.getJugadores(equipo)
