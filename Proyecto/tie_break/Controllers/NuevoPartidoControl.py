from flet import *

from Models.NuevoPartidoModel import NuevoPartidoModel


class NuevoPartidoContolador(object):
    def __init__(self, page: Page):
        self.page = page
        self. vista = None
        self.modelo = NuevoPartidoModel()

    def iniciarVista(self):
        self.page.clean()

