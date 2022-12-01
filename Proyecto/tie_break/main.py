#from tkinter import *
import flet
from flet import *
# from tkinter import font as tkfont
# from tkinter import ttk
# import helpers
# import splashscreen

from Controllers.LoginControl import LoginControlador
from Controllers.MenuEquipoControl import MenuEquipoControlador
#from Views.MenuEquipoView import MenuEquipoVista
from Models.Entidades.Equipo import Equipo


# ----------------------------------------------------------------------------------------------------#
#                                            APLICACIÓN                                               #
# ----------------------------------------------------------------------------------------------------#

# def start():
#     # ----------------------------------------------------------------------------------------------------#
#     #                                        DEFINICIÓN DE ROOT                                           #
#     # ----------------------------------------------------------------------------------------------------#
#
#     # Configuracion de la raíz
#     # rootWidth = 800
#     # rootHeight = 650
#     root = Tk()
#     # root.geometry(helpers.getGeometry(root,root.winfo_screenwidth(),root.winfo_screenheight()))
#     root.state("zoom")
#     root.title("Tie-Break")
#     root.minsize(height=460, width=620)
#     # root.iconbitmap(helpers.getImgPath('.ico'))
#     # root['background'] = theme["color1"]
#     root['background'] = '#1f1137'
#
#
#     root.mainloop()


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
    page.on_close=page.close()


def main(page: Page):
    configuracionInicial(page)
    llamarLogin(page)

    equipo = Equipo.getEquipos()[0]
    page.session.set("equipo", equipo)

    #equipoView = MenuEquipoVista(page)
    #equipoView.setEquipoSeleccionado("Gallos UAA")
    #page.add(equipoView)

    #menuEquipo = MenuEquipoControlador(page)
    #menuEquipo.iniciarVista()


def llamarLogin(page):
    login = LoginControlador(page)
    login.iniciarVista()


flet.app(target=main, assets_dir="resources")
