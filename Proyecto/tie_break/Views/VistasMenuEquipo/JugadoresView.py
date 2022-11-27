from flet import *
from flet import UserControl, padding, border, icons, margin, colors
from flet.border import BorderSide


class JugadoresVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.filasJugadores = []
        self.columnListaJugadores = None

    def build(self):
        self.expand = True
        self.obtenerContenedoresJugadores()
        self.columnListaJugadores = Column(
            controls=self.filasJugadores,
            scroll="auto",
            expand=True
        )
        return self.inicializarComponentes()

    def inicializarComponentes(self):
        encabezadoNumero = Text(
            value="No.",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=1,
            text_align="start"
        )
        encabezadoJugador = Text(
            value="Jugador",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=3,
            text_align="start"
        )
        encabezadoPosicion = Text(
            value="Posición",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=2,
            text_align="start"
        )

        rowEncabezadoTablaJugadores = Row(
            controls=[
                encabezadoNumero,
                encabezadoJugador,
                encabezadoPosicion,
                Container(
                    expand=1
                )
            ]
        )

        containerEncabezado = Container(
            content=rowEncabezadoTablaJugadores,
            border=border.only(None, None, None, BorderSide(1, color="#001f60")),
            padding=padding.symmetric(5, 70),
            bgcolor=colors.WHITE
        )

        containerListaJugadores = Container(
            content=self.columnListaJugadores,
            margin=margin.symmetric(0, 50),
            bgcolor=colors.WHITE,
            expand=True
        )

        columnTablaJugadores = Column(
            controls=[
                containerEncabezado,
                containerListaJugadores,
                containerEncabezado
            ],
            spacing=0,
            expand=True
        )

        containerJugadoresVista = Container(
            content=columnTablaJugadores
        )

        return containerJugadoresVista

    def obtenerContenedoresJugadores(self):
        for jugador in self.obtenerJugadores("Gallos UAA"):
            self.filasJugadores.append(
                Container(
                    content=Row(
                        controls=[
                            Text(
                                value=jugador.getNumero(),
                                size=14,
                                color="#001f60",
                                expand=1,
                                text_align="start"
                            ),
                            Row(
                                controls=[
                                    Text(
                                        value=f"{jugador.getNombre()}",
                                        size=14,
                                        color="#001f60",
                                        text_align="start"
                                    ),
                                    Text(
                                        value=" C",
                                        size=14,
                                        color="#d50037",
                                        text_align="start",
                                        font_family="Nunito Bold",
                                        tooltip="Capitán del Equipo"
                                    ) if jugador.isCapitan() else Container(margin=0, padding=0, width=0)
                                ],
                                expand=3,
                                vertical_alignment="center"
                            ),
                            Text(
                                value=jugador.getPosicion(),
                                size=14,
                                color="#001f60",
                                expand=2,
                                text_align="start"
                            ),
                            Row(
                                controls=[
                                    IconButton(
                                        icon=icons.REMOVE_RED_EYE,
                                        icon_color="#001f60",
                                        tooltip="Ver Jugador"
                                    ),
                                    IconButton(
                                        icon=icons.EDIT_NOTE,
                                        icon_color="#ffa400",
                                        tooltip="Editar Jugador"
                                    ),
                                    IconButton(
                                        icon=icons.DELETE,
                                        icon_color="#d50037",
                                        tooltip="Borrar Jugador"
                                    )
                                ],
                                expand=1
                            )
                        ],
                        expand=True
                    ),
                    margin=margin.symmetric(2.5, 20),
                    border=border.only(bottom=BorderSide(1, "#001f60")),
                    padding=padding.symmetric(5, 0)
                )
            )

    def obtenerJugadores(self, equipo):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerJugadores(equipo)
