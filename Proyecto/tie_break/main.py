#from tkinter import *
import flet
from flet import *
# from tkinter import font as tkfont
# from tkinter import ttk
# import helpers
# import splashscreen

from Controllers.LoginControl import LoginControlador
from Controllers.MenuEquipoControl import MenuEquipoControlador
from Controllers.RegistrarEquipoControl import RegistrarEquipoControlador
from Controllers.RegistrarPartidoControl import RegistrarPartidoControlador
from Models.Entidades.Equipo import Equipo

def configuracionInicial(page: Page):
    page.fonts = {
        "Nunito": "/fonts/Nunito-Regular.ttf",
        "Nunito Bold": "/fonts/Nunito-Bold.ttf"
    }

    page.theme = theme.Theme(font_family="Nunito")
    page.theme_mode = "light"
    page.title = "SSE Voley"
    page.bgcolor = "#D9D9D9"
    page.padding = 0
    page.update()

    page.window_center()
    page.on_close = page.close()


def main(page: Page):
    configuracionInicial(page)
    llamarLogin(page)

    # equipo = Equipo.getEquipos()[0]
    # page.session.set("equipo", equipo)
    # equipoContrario = Equipo.getEquipos()[1]
    # page.session.set("equipoContrario", equipoContrario)
    #
    # menuEquipo = MenuEquipoControlador(page)
    # menuEquipo.iniciarVista()

    #registrarPartido = RegistrarPartidoControlador(page)
    #registrarPartido.iniciarVista()



def llamarLogin(page):
    login = LoginControlador(page)
    login.iniciarVista()


flet.app(target=main, assets_dir="resources")
