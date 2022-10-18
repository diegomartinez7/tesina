from flet import *
from flet import padding, icons
from flet.buttons import RoundedRectangleBorder

from Views import LoginVista

nombreEntrenador = "Alejandro González"


def menuEquipos(page: Page):
    prepararPagina(page)
    inicializarComponentes(page)


def prepararPagina(page: Page):
    page.clean()
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"
    page.padding = padding.all(50)


def inicializarComponentes(page: Page):
    def cerrarSesion(e):
        LoginVista.login(page)

    tituloSistema = Text(
        value="SSE Voley",
        color="#001f60",
        size=96,
        font_family="Nunito"
    )
    mensajeBienvenidaEntrenador = Text(
        value=f"Bienvenido {nombreEntrenador}",
        color="#001f60",
        size=32,
        font_family="Nunito"
    )

    buttonSeleccionarEquipo = ElevatedButton(
        content=Text(
            value="Seleccionar Equipo",
            size=32
        ),
        bgcolor="#001f60",
        color="#D9D9D9",
        width=400,
        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=12.5),
            padding=padding.symmetric(10, 0)
        )
    )
    buttonRegistrarEquipo = ElevatedButton(
        content=Text(
            value="Registrar Equipo",
            size=32
        ),
        bgcolor="#001f60",
        color="#D9D9D9",
        width=400,
        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=12.5),
            padding=padding.symmetric(10, 0)
        )
    )
    buttonCerrarSesion = IconButton(
        icon=icons.LOGOUT,
        icon_color="#001f60",
        icon_size=36,
        on_click=cerrarSesion
    )
    buttonConfiguracion = IconButton(
        icon=icons.SETTINGS,
        icon_color="#001f60",
        icon_size=36
    )

    columnTitulos = Column(
        [
            tituloSistema,
            mensajeBienvenidaEntrenador
        ],
        horizontal_alignment="center"
    )

    rowBotonesMenu = Row(
        [
            buttonSeleccionarEquipo,
            buttonRegistrarEquipo
        ],
        alignment="spaceEvenly"
    )
    rowBotonesControl = Row(
        [
            buttonCerrarSesion,
            buttonConfiguracion
        ],
        alignment="spaceBetween",
        vertical_alignment="end"
    )

    page.add(columnTitulos, rowBotonesMenu, rowBotonesControl)
