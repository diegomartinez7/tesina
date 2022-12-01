from flet import *
from flet import UserControl, border, padding, colors, icons, margin
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder


class CompetenciasYPartidosVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.listaCompetencias = []
        self.columnListaCompetencias = None

    def build(self):
        self.expand = True
        self.obtenerContenedoresCompetencias()
        self.columnListaCompetencias = Column(
            controls=self.listaCompetencias,
            scroll="auto",
            expand=True
        )
        return self.inicializarComponentes()

    def inicializarComponentes(self):
        encabezadoCompetencia = Text(
            value="Competencia",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=2,
            text_align="start"
        )
        encabezadoFechaInicio = Text(
            value="Fecha de Inicio",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=1,
            text_align="start"
        )
        encabezadoFechaFin = Text(
            value="Fecha de Término",
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
        encabezadoActiva = Text(
            value="Activa",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=1,
            text_align="start"
        )

        buttonNuevaCompetencia = ElevatedButton(
            content=Text(
                value="Nueva Competencia",
                size=16,
                color="#ffa400"
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            #on_click=self.abrirDialogNuevoJugador
        )

        rowEncabezadoTablaCompetencias = Row(
            controls=[
                encabezadoCompetencia,
                encabezadoFechaInicio,
                encabezadoFechaFin,
                encabezadoTipo,
                encabezadoActiva,
                Container(
                    expand=1
                )
            ]
        )

        containerEncabezadoTablaCompetencias = Container(
            content=rowEncabezadoTablaCompetencias,
            border=border.only(None, None, None, BorderSide(1, color="#001f60")),
            padding=padding.symmetric(5, 70),
            bgcolor=colors.WHITE
        )

        containerListaCompetencias = Container(
            content=self.columnListaCompetencias,
            margin=margin.symmetric(0, 50),
            bgcolor=colors.WHITE,
            expand=True
        )

        containerButtonNuevaCompetencia = Container(
            content=buttonNuevaCompetencia,
            alignment=alignment.center_right,
            padding=10,
            bgcolor=colors.WHITE,
            margin=margin.symmetric(0, 50),
        )

        columnTablaCompetencias = Column(
            controls=[
                containerEncabezadoTablaCompetencias,
                containerListaCompetencias,
                containerButtonNuevaCompetencia
            ],
            spacing=0,
            expand=True
        )

        containerCompetenciasYPartidosVista = Container(
            content=columnTablaCompetencias
        )

        return containerCompetenciasYPartidosVista

    def obtenerContenedoresCompetencias(self):
        self.listaCompetencias.clear()
        for competencia in self.obtenerCompetencias():
            self.listaCompetencias.append(
                Container(
                    content=Row(
                        controls=[
                            Text(
                                value=competencia.getNombre(),
                                size=14,
                                color="#001f60",
                                expand=2,
                                text_align="start"
                            ),
                            Text(
                                value=competencia.getInicio(),
                                size=14,
                                color="#001f60",
                                expand=1,
                                text_align="start"
                            ),
                            Text(
                                value=competencia.getFin(),
                                size=14,
                                color="#001f60",
                                expand=1,
                                text_align="start"
                            ),
                            Text(
                                value=competencia.getTipo(),
                                size=14,
                                color="#001f60",
                                expand=1,
                                text_align="start"
                            ),
                            Container(
                                content=Icon(
                                    name=icons.DONE if competencia.isActiva() else icons.CLOSE,
                                    size=14,
                                    color="#00BC06" if competencia.isActiva() else "#d50037",
                                ),
                                alignment=alignment.center_left,
                                expand=1
                            ),
                            Row(
                                controls=[
                                    IconButton(
                                        icon=icons.REMOVE_RED_EYE,
                                        icon_color="#001f60",
                                        tooltip="Ver Partidos",
                                    ),
                                    IconButton(
                                        icon=icons.EDIT_NOTE,
                                        icon_color="#ffa400",
                                        tooltip="Editar Competencia",
                                    ),
                                    IconButton(
                                        icon=icons.DELETE,
                                        icon_color="#d50037",
                                        tooltip="Borrar Competencia"
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

    def obtenerCompetencias(self):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerCompetencias()
