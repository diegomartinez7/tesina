from flet import *
from flet import border, padding, colors, margin, icons
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder


class EquiposRivalesVista(UserControl):
    def __init__(self, page):
        super().__init__()
        self.pagina = page
        self.listaRivales = []
        self.columnListaRivales = None

    def build(self):
        self.expand = True
        self.obtenerContenedoresRivales()
        self.columnListaRivales = Column(
            controls=self.listaRivales,
            scroll="auto",
            expand=True
        )
        return self.inicializarComponentes()

    def inicializarComponentes(self):
        encabezadoEquipo = Text(
            value="Equipo",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=2,
            text_align="start"
        )
        encabezadoCategoria = Text(
            value="Categoría",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=1,
            text_align="start"
        )
        encabezadoRama = Text(
            value="Rama",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=1,
            text_align="start"
        )
        encabezadoTipo = Text(
            value="Tipo",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=1,
            text_align="start"
        )
        encabezadoEntidadRepresentada = Text(
            value="Entidad Representada",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=2,
            text_align="start"
        )

        buttonNuevoRival = ElevatedButton(
            content=Text(
                value="Nuevo Rival",
                size=16,
                color="#ffa400"
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            # on_click=self.abrirDialogNuevoJugador
        )

        rowEncabezadoTablaEquiposRivales = Row(
            controls=[
                encabezadoEquipo,
                encabezadoCategoria,
                encabezadoRama,
                encabezadoTipo,
                encabezadoEntidadRepresentada,
                Container(
                    expand=1
                )
            ]
        )

        containerEncabezadoTablaEquiposRivales = Container(
            content=rowEncabezadoTablaEquiposRivales,
            border=border.only(None, None, None, BorderSide(1, color="#001f60")),
            padding=padding.symmetric(5, 70),
            #bgcolor=colors.WHITE
            bgcolor="#ffa400"
        )

        containerListaRivales = Container(
            content=self.columnListaRivales,
            margin=margin.symmetric(0, 50),
            bgcolor=colors.WHITE,
            expand=True
        )

        containerButtonNuevoRival = Container(
            content=buttonNuevoRival,
            alignment=alignment.center_right,
            padding=10,
            bgcolor=colors.WHITE,
            margin=margin.symmetric(0, 50),
        )

        columnTablaEquiposRivales = Column(
            controls=[
                containerEncabezadoTablaEquiposRivales,
                containerListaRivales,
                containerButtonNuevoRival
            ],
            spacing=0,
            expand=True
        )

        containerEquiposRivalesVista = Container(
            content=columnTablaEquiposRivales
        )

        return containerEquiposRivalesVista

    def obtenerContenedoresRivales(self):
        self.listaRivales.clear()
        for rival in self.obtenerRivales():
            self.listaRivales.append(
                    Container(
                        content=Row(
                            controls=[
                                Text(
                                    value=rival.getNombre(),
                                    size=14,
                                    color="#001f60",
                                    expand=2,
                                    text_align="start"
                                ),
                                Text(
                                    value=rival.getCategoria(),
                                    size=14,
                                    color="#001f60",
                                    expand=1,
                                    text_align="start"
                                ),
                                Text(
                                    value=rival.getRama(),
                                    size=14,
                                    color="#001f60",
                                    expand=1,
                                    text_align="start"
                                ),
                                Text(
                                    value=rival.getTipoEquipo(),
                                    size=14,
                                    color="#001f60",
                                    expand=1,
                                    text_align="start"
                                ),
                                Text(
                                    value=rival.getEntidadRepresentada(),
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
                                            tooltip="Ver Jugadores",
                                        ),
                                        IconButton(
                                            icon=icons.EDIT_NOTE,
                                            icon_color="#ffa400",
                                            tooltip="Editar Equipo",
                                        ),
                                        IconButton(
                                            icon=icons.DELETE,
                                            icon_color="#d50037",
                                            tooltip="Borrar Equipo"
                                        )
                                    ],
                                    expand=1
                                ),

                            ],
                            expand=True
                        ),
                        margin=margin.symmetric(2.5, 20),
                        border=border.only(bottom=BorderSide(1, "#001f60")),
                        padding=padding.symmetric(5, 0)
                    )
            )

    def obtenerRivales(self):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerRivales()
