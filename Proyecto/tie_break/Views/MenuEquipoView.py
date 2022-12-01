from flet import *
from flet import UserControl, Page, icons, border, colors, padding, margin
from flet.border import BorderSide

from Views.VistasMenuEquipo.CicloDePreparacionView import CicloDePreparacionVista
from Views.VistasMenuEquipo.CompetenciasYPartidosView import CompetenciasYPartidosVista
from Views.VistasMenuEquipo.EquiposRivalesView import EquiposRivalesVista
from Views.VistasMenuEquipo.JugadoresView import JugadoresVista


class MenuEquipoVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.opcionSeleccionada = None
        self.equipoSeleccionado = self.pagina.session.get("equipo").getNombre()
        self.tituloEquipo = None
        self.tiuloOpcionSeleccionada = None
        self.containerContenidoSeleccionado = None

    def build(self):
        self.expand = True
        return self.inicializarComponentes()

    def inicializarComponentes(self):
        self.tituloEquipo = Text(
            value=f"{self.equipoSeleccionado}",
            color="#ffa400",
            size=14,
            font_family="Nunito"
        )
        self.tiuloOpcionSeleccionada = Text(
            value=f"{' - ' + self.opcionSeleccionada if self.opcionSeleccionada else ''}",
            color="#b3b3cc",
            size=14,
            font_family="Nunito"
        )
        rowTitulosMenuEquipo = Row(
            controls=[
                self.tituloEquipo,
                self.tiuloOpcionSeleccionada
            ],
            alignment="center",
            spacing=0
        )
        containerTituloEquipo = Container(
            content=rowTitulosMenuEquipo,
            expand=True
        )

        buttonRegresar = IconButton(
            icon=icons.KEYBOARD_RETURN_ROUNDED,
            icon_color="#b3b3cc",
            icon_size=16,
            on_click=self.regresar
        )
        buttonConfiguracion = IconButton(
            icon=icons.SETTINGS,
            icon_color="#b3b3cc",
            icon_size=16
        )
        rowEncabezadoMenuEquipo = Row(
            controls=[
                buttonRegresar,
                containerTituloEquipo,
                buttonConfiguracion
            ]
        )
        containerEncabezadoMenuEquipo = Container(
            content=rowEncabezadoMenuEquipo,
            bgcolor="#001f60"
        )

        dropdownGestionarEquipo = PopupMenuButton(
            content=Row(
                [
                    Text(
                        value="Gestionar Equipo",
                        size=18,
                        color="#001f60"
                    ),
                    Icon(
                        name=icons.ARROW_DROP_DOWN,
                        size=20,
                        color="#001f60"
                    )
                ]
            ),
            items=[
                PopupMenuItem(
                    content=Text(
                        value="Competencias y partidos",
                        size=16,
                        color="#001f60"
                    ),
                    on_click=self.gestionarEquipoOnClick
                ),
                PopupMenuItem(
                    content=Text(
                        value="Jugadores",
                        size=16,
                        color="#001f60"
                    ),
                    on_click=self.gestionarEquipoOnClick
                ),
                PopupMenuItem(
                    content=Text(
                        value="Ciclo de Preparación",
                        size=16,
                        color="#001f60"
                    ),
                    on_click=self.gestionarEquipoOnClick
                ),
                PopupMenuItem(
                    content=Text(
                        value="Equipos Rivales",
                        size=16,
                        color="#001f60"
                    ),
                    on_click=self.gestionarEquipoOnClick
                )
            ],
            tooltip="Ver opciones"
        )
        buttonRegistrarPartido = TextButton(
            content=Text(
                value="Registrar Partido",
                size=18,
                color="#001f60"
            ),
            style=ButtonStyle(
                overlay_color=colors.WHITE
            ),
            on_click=self.registrarPartidoOnClick
        )
        buttonRegistrarEntrenamiento = TextButton(
            content=Text(
                value="Registrar Entrenamiento",
                size=18,
                color="#001f60"
            ),
            style=ButtonStyle(
                overlay_color=colors.WHITE
            ),
            on_click=self.registrarEntrenamientoOnClick
        )
        buttonReportes = TextButton(
            content=Text(
                value="Reportes",
                size=18,
                color="#001f60"
            ),
            style=ButtonStyle(
                overlay_color=colors.WHITE
            ),
            on_click=self.reportesOnClick
        )
        rowOpcionesMenuEquipo = Row(
            controls=[
                dropdownGestionarEquipo,
                buttonRegistrarPartido,
                buttonRegistrarEntrenamiento,
                buttonReportes
            ],
            alignment="spaceEvenly"
        )
        containerOpcionesMenuEquipo = Container(
            content=rowOpcionesMenuEquipo,
            padding=padding.symmetric(0, 20),
            bgcolor=colors.WHITE
        )

        columnEncabezadoMenu = Column(
            controls=[
                containerEncabezadoMenuEquipo,
                containerOpcionesMenuEquipo
            ],
            spacing=0
        )
        containerEncabezadoMenu = Container(
            content=columnEncabezadoMenu,
            border=border.only(None, None, None, BorderSide(3, color="#001f60"))
        )

        self.containerContenidoSeleccionado = Container(
            #content=Text(value="Por favor seleccione una opción"),
            content=CicloDePreparacionVista(self.pagina),
            expand=True,
            alignment=alignment.center
        )

        containerMenuEquipoVista = Container(
            content=Column(
                [
                    containerEncabezadoMenu,
                    self.containerContenidoSeleccionado
                ],
                spacing=0
            )
        )

        return containerMenuEquipoVista

    def setEquipoSeleccionado(self, equipo):
        self.equipoSeleccionado = equipo
        self.pagina.update()

    def gestionarEquipoOnClick(self, e):
        opcionesDropdown = {
            "Competencias y partidos": self.opcionCompetenciasYPartidosSeleccionada,
            "Jugadores": self.opcionJugadoresSeleccionada,
            "Ciclo de Preparación": self.opcionCicloDePreparacionSeleccionada,
            "Equipos Rivales": self.opcionEquiposRivalesSeleccionada
        }
        opcionesDropdown.get(e.control.content.value)()
        self.setOpcionSeleccionada(e.control.content.value)

    def registrarPartidoOnClick(self, e):
        self.setOpcionSeleccionada(e.control.content.value)

    def registrarEntrenamientoOnClick(self, e):
        self.setOpcionSeleccionada(e.control.content.value)

    def reportesOnClick(self, e):
        self.setOpcionSeleccionada(e.control.content.value)

    def setOpcionSeleccionada(self, opcion):
        self.opcionSeleccionada = opcion
        self.tiuloOpcionSeleccionada.value = f"{' - ' + self.opcionSeleccionada if self.opcionSeleccionada else ''}"
        self.update()

    def opcionCompetenciasYPartidosSeleccionada(self):
        tablaCompetencias = CompetenciasYPartidosVista(self.pagina)
        self.containerContenidoSeleccionado.content = tablaCompetencias
        self.update()

    def opcionJugadoresSeleccionada(self):
        tablaJugadores = JugadoresVista(self.pagina)
        self.containerContenidoSeleccionado.content = tablaJugadores
        self.update()

    def opcionCicloDePreparacionSeleccionada(self):
        tablaPruebas = CicloDePreparacionVista(self.pagina)
        self.containerContenidoSeleccionado.content = tablaPruebas
        self.update()

    def opcionEquiposRivalesSeleccionada(self):
        tablaRivales = EquiposRivalesVista(self.pagina)
        self.containerContenidoSeleccionado.content = tablaRivales
        self.update()

    def regresar(self, e):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        controlador.regresar()
