from flet import *
from flet import padding, icons
from flet.buttons import RoundedRectangleBorder

nombreEntrenador = "Alejandro González"

class MenuSeleccionOCreacionVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page

    def build(self):
        self.expand = True
        return self.inicializarComponentes()

    def inicializarComponentes(self):
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
            ),
            on_click=self.clickSeleccionarEquipo
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
            on_click=self.cerrarSesion
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

        containerMenuSeleccionOCreacionVista = Container(
            content= Column(
                [
                    columnTitulos,
                    rowBotonesMenu,
                    rowBotonesControl
                ],
                horizontal_alignment="center",
                alignment="spaceBetween"
            ),
            padding=50
        )

        return containerMenuSeleccionOCreacionVista

    def clickSeleccionarEquipo(self, e):
        from Controllers.MenuSeleccionOCreacionControl import MenuSeleccionOCreacionControlador
        controlador = MenuSeleccionOCreacionControlador(self.pagina)
        controlador.seleccionarEquipo()
    def cerrarSesion(self, e):
        from Controllers.MenuSeleccionOCreacionControl import MenuSeleccionOCreacionControlador
        controlador = MenuSeleccionOCreacionControlador(self.pagina)
        controlador.cerrarSesion()

