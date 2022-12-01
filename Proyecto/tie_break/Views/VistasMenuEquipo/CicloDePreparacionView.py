from flet import *
from flet import border, colors, padding, icons, margin
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder


class CicloDePreparacionVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.listaPruebasFisicas = []
        self.columnPruebas = None

    def build(self):
        self.expand = True
        self.obtenerContenedoresPruebasFisicas()
        self.columnPruebas = Column(
            controls=self.listaPruebasFisicas,
            scroll="auto",
            expand=True
        )
        return self.inicializarComponentes()

    def inicializarComponentes(self):
        encabezadoEtapa1 = Text(
            value="Inicial",
            color="#001f60",
            size=16,
            font_family="Nunito",
            text_align="center"
        )
        encabezadoEtapa2 = Text(
            value="Precompetitiva",
            color="#001f60",
            size=16,
            font_family="Nunito",
            text_align="center"
        )
        encabezadoEtapa3 = Text(
            value="Competitiva",
            color="#001f60",
            size=16,
            font_family="Nunito",
            text_align="center"
        )
        encabezadoEtapa4 = Text(
            value="Transitorio",
            color="#001f60",
            size=16,
            font_family="Nunito",
            text_align="center"
        )
        encabezadoNombrePrueba = Text(
            value="Nombre",
            color="#001f60",
            size=16,
            font_family="Nunito",
            text_align="start",
            expand=2
        )
        encabezadoFechaPrueba = Text(
            value="Fecha",
            color="#001f60",
            size=16,
            font_family="Nunito",
            text_align="start",
            expand=1
        )
        encabezadoCicloEntrenamiento = Text(
            value="Etapa",
            color="#001f60",
            size=16,
            font_family="Nunito",
            text_align="start",
            expand=1
        )
        encabezadoAplicada = Text(
            value="Aplicada",
            color="#001f60",
            size=16,
            font_family="Nunito",
            text_align="start",
            expand=1
        )

        buttonNuevaPrueba = ElevatedButton(
            content=Text(
                value="Nueva Prueba",
                size=16,
                color="#ffa400"
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            # on_click=self.abrirDialogNuevoJugador
        )

        containerEtapa1 = Container(
            content=encabezadoEtapa1,
            expand=1,
            border=border.all(1, color="#001f60"),
            height=35,
            alignment=alignment.center,
            bgcolor="#52CE48"
        )
        containerEtapa2 = Container(
            content=encabezadoEtapa2,
            expand=1,
            border=border.all(1, color="#001f60"),
            height=35,
            alignment=alignment.center,
            bgcolor="#52CE48"
        )
        containerEtapa3 = Container(
            content=encabezadoEtapa3,
            expand=1,
            border=border.all(1, color="#001f60"),
            height=35,
            alignment=alignment.center
        )
        containerEtapa4 = Container(
            content=encabezadoEtapa4,
            expand=1,
            border=border.all(1, color="#001f60"),
            height=35,
            alignment=alignment.center
        )

        rowEtapasDePreparacion = Row(
            controls=[
                containerEtapa1,
                containerEtapa2,
                containerEtapa3,
                containerEtapa4
            ],
            spacing=0
        )
        rowEncabezadoTablaPruebas = Row(
            controls=[
                encabezadoNombrePrueba,
                encabezadoFechaPrueba,
                encabezadoCicloEntrenamiento,
                encabezadoAplicada,
                Container(
                    expand=1
                )
            ]
        )

        containerEtapasDePreparacion = Container(
            content=rowEtapasDePreparacion,

        )
        containerEncabezadoTablaEquiposRivales = Container(
            content=rowEncabezadoTablaPruebas,
            border=border.only(None, None, None, BorderSide(1, color="#001f60")),
            padding=padding.symmetric(5, 70),
            bgcolor=colors.WHITE
        )

        containerListaPruebas = Container(
            content=self.columnPruebas,
            margin=margin.symmetric(0, 50),
            bgcolor=colors.WHITE,
            expand=True
        )

        containerButtonNuevaPrueba = Container(
            content=buttonNuevaPrueba,
            alignment=alignment.center_right,
            padding=10,
            bgcolor=colors.WHITE,
            margin=margin.symmetric(0, 50),
        )

        columnTablaPruebasFisicas = Column(
            controls=[
                containerEtapasDePreparacion,
                containerEncabezadoTablaEquiposRivales,
                containerListaPruebas,
                containerButtonNuevaPrueba
            ],
            spacing=0,
            expand=True
        )

        containerCicloEntrenamiento = Container(
            content=columnTablaPruebasFisicas
        )

        return containerCicloEntrenamiento

    def obtenerContenedoresPruebasFisicas(self):
        self.listaPruebasFisicas.clear()
        for prueba in self.obtenerPruebasFisicas():
            self.listaPruebasFisicas.append(
                Container(
                    content=Row(
                        controls=[
                            Text(
                                value=prueba.getNombre(),
                                size=14,
                                color="#001f60",
                                expand=2,
                                text_align="start"
                            ),
                            Text(
                                value=prueba.getFecha(),
                                size=14,
                                color="#001f60",
                                expand=1,
                                text_align="start"
                            ),
                            Text(
                                value=prueba.getCiclo(),
                                size=14,
                                color="#001f60",
                                expand=1,
                                text_align="start"
                            ),
                            Container(
                                content=Icon(
                                    name=icons.DONE if prueba.isAplicada() else icons.CLOSE,
                                    size=14,
                                    color="#00BC06" if prueba.isAplicada() else "#d50037",
                                ),
                                alignment=alignment.center_left,
                                expand=1
                            ),
                            Row(
                                controls=[
                                    IconButton(
                                        icon=icons.REMOVE_RED_EYE,
                                        icon_color="#001f60",
                                        tooltip="Ver Pruebas",
                                    ),
                                    IconButton(
                                        icon=icons.EDIT_NOTE,
                                        icon_color="#ffa400",
                                        tooltip="Editar Pruebas",
                                    ),
                                    IconButton(
                                        icon=icons.DELETE,
                                        icon_color="#d50037",
                                        tooltip="Borrar Pruebas"
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

    def obtenerPruebasFisicas(self):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerPruebas()
