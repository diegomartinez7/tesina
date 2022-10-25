from flet import Page

from Views.SeleccionarEquipoView import SeleccionarEquipoVista


class SeleccionarEquipoControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.vista = SeleccionarEquipoVista(self.page)

    def iniciarVista(self):
        self.page.vertical_alignment = "center"
        self.page.add(self.vista)