from flet import *
from flet import colors, icons, margin, padding
from flet.buttons import RoundedRectangleBorder

from Views import EntrenadorMenuEquipos
from Views import Registro


def login(page: Page):
    prepararPagina(page)
    inicializarComponentes(page)


def prepararPagina(page: Page):
    page.clean()
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"
    page.padding = padding.all(50)


def inicializarComponentes(page: Page):
    def iniciarSesion(e):
        EntrenadorMenuEquipos.menuEquipos(page)

    def registrarse(e):
        Registro.registro(page)

    tituloSistema = Text(
        value="SSE Voley",
        color="#001f60",
        size=96,
        font_family="Nunito"
    )
    labelUsuario = Text(
        value="Usuario",
        color="#001f60",
        size=30,
        font_family="Nunito"
    )
    labelPassword = Text(
        value="Contraseña",
        color="#001f60",
        size=30,
        font_family="Nunito"
    )

    inputUsuario = TextField(
        color="#001f60",
        text_size=16,
        border_radius=12.5,
        width=400,
        border_color=colors.WHITE,
        focused_border_color="#001f60"
    )
    inputPassword = TextField(
        password=True,
        can_reveal_password=True,
        color="#001f60",
        text_size=16,
        border_radius=12.5,
        width=400,
        border_color=colors.WHITE,
        focused_border_color="#001f60"
    )

    buttonIniciarSesion = ElevatedButton(
        content=Text(
            value="Iniciar Sesión",
            size=24
        ),
        bgcolor="#001f60",
        color="#D9D9D9",
        on_click=iniciarSesion,
        style=ButtonStyle(
            shape=RoundedRectangleBorder(radius=12.5)
        )
    )
    buttonRegistrarse = TextButton(
        content=Text(
            value="Registrarse",
            size=18,
            color="#001f60"
        ),
        on_click=registrarse
    )
    buttonInfo = IconButton(
        icon=icons.INFO_OUTLINED,
        icon_color="#001f60",
        icon_size=36
    )

    containerLabelUsuario = Container(
        content=labelUsuario,
        margin=margin.only(0, 10, 0, 0),
    )

    containerInputUsuario = Container(
        content=inputUsuario,
        bgcolor=colors.WHITE,
        border_radius=12.5
    )

    containerLabelPassword = Container(
        content=labelPassword,
        margin=margin.only(0, 10, 0, 0)
    )

    containerinputPassword = Container(
        content=inputPassword,
        bgcolor=colors.WHITE,
        border_radius=12.5
    )

    containerButtonIniciarSesion = Container(
        content=buttonIniciarSesion,
        margin=margin.only(0, 20, 0, 0)
    )

    contanerButtonInfo = Container(
        content=buttonInfo,
        alignment=alignment.bottom_right,
    )

    columnElementosPrincipales = Column([
        containerLabelUsuario,
        containerInputUsuario,
        containerLabelPassword,
        containerinputPassword,
        containerButtonIniciarSesion,
        buttonRegistrarse
    ], horizontal_alignment="center")

    page.add(tituloSistema, columnElementosPrincipales, contanerButtonInfo)
