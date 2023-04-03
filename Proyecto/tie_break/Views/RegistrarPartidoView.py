from flet import *
from flet import colors, margin, border, padding, icons
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder

from Models.Entidades.AccionesPartido.Acomodo import Acomodo
from Models.Entidades.AccionesPartido.Pase import Pase
from Models.Entidades.AccionesPartido.Remate import Remate
from Models.Entidades.AccionesPartido.Saque import Saque
from Models.Entidades.Sets.Set import Set
from Models.Entidades.Sets.SetDesempate import SetDesempate
from Models.Entidades.Punto import Punto
from Models.Entidades.AccionesPartido.AccionPartido import AccionPartido


class RegistrarPartidoVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page

        self.setsObjetivo = self.pagina.session.get("sets")
        self.puntosSet = self.pagina.session.get("puntos")
        self.setActual = None
        self.puntoActual = None
        self.accionActual = None
        self.jugador = None
        self.tipoAccion = None
        self.contrario = None
        self.partidoIniciado = False

        self.numeroSet = 1
        self.textNumeroSet = None
        self.textEquipoPropio = None
        self.textEquipoContrario = None
        self.listaJugadoresPropios = []
        self.listaJugadoresContrarios = []
        self.columnListaJugadoresPropios = None
        self.columnListaJugadoresContrarios = None

        self.marcadorPropio = 0
        self.marcadorContrario = 0
        self.textMarcadorPropio = None
        self.textMarcadorContrario = None

        self.inputComandos = None
        self.listaLogs = []
        self.listViewLogs = None

        self.accionesIniciadas: bool = False
        self.accionEnProceso: str = ""
        self.accionesEnPunto: str = ""
        self.jugadorSeleccionado = None
        self.zonasPorSeleccionar = False
        self.zonaInicial: str = ""
        self.zonaFinal: str = ""

        self.jugadoresPropiosEnCancha = []
        self.contenedoresJugadoresPropiosEnCancha = []
        self.jugadoresContrariosEnCancha = []
        self.contenedoresJugadoresContrariosEnCancha = []

        self.containerZonasCancha = None
        self.containerJugadoresEnCancha = None
        self.reescalado = False

        self.imagenCancha = None
        self.contenidoCancha = None
        self.stackCancha = None
        self.containerImagenCancha = None

    def build(self):
        idPartido = self.pagina.session.get("partidoRegistrado").getId()
        nuevoSet = Set(self.numeroSet, idPartido, self.puntosSet)
        nuevoSet.setId(1)
        self.setActual = nuevoSet
        self.puntoActual = Punto(self.setActual.getId(), 0, 0)
        self.puntoActual.setId(1)
        self.iniciarSet()
        self.expand = True
        self.textNumeroSet = Text(
            value=f"Set {self.numeroSet}",
            size=20,
            color="#D9D9D9",
        )
        self.textEquipoPropio = Text(
            value=self.obtenerNombreEquipoPropio(),
            size=20,
            color="#001F60"
        )
        self.textEquipoContrario = Text(
            value=self.obtenerNombreEquipoContrario(),
            size=20,
            color="#D50037"
        )

        self.obtenerContenedoresJugadores(False)
        self.columnListaJugadoresPropios = Column(
            controls=self.listaJugadoresPropios,
            spacing=0,
            expand=True
        )
        self.obtenerContenedoresJugadores(True)
        self.columnListaJugadoresContrarios = Column(
            controls=self.listaJugadoresContrarios,
            spacing=0,
            expand=True
        )

        self.textMarcadorPropio = Text(
            value=f"{self.marcadorPropio}",
            color=colors.WHITE,
            size=20
        )
        self.textMarcadorContrario = Text(
            value=f"{self.marcadorContrario}",
            color=colors.WHITE,
            size=20
        )

        self.inputComandos = TextField(
            text_size=14,
            border_radius=12.5,
            content_padding=10,
            border_width=0,
            color="#001f60"
        )

        self.jugadoresPropiosEnCancha = self.definirJugadoresEnCancha(False)
        self.construirContenedoresJugadoresEnCancha(False)
        self.jugadoresContrariosEnCancha = self.definirJugadoresEnCancha(True)
        self.construirContenedoresJugadoresEnCancha(True)

        self.contenidoCancha = self.iniciarContenedoresJugadoresCancha()

        self.pagina.on_resize = self.reescalarZonas

        self.imagenCancha = Image(
            src=f"/img/cancha_larga3.jpg",
            bottom=0,
            top=0,
            left=0,
            right=0
        )
        self.stackCancha = Stack(
            controls=[
                self.imagenCancha,
                self.contenidoCancha
            ]
        )
        self.containerImagenCancha = Container(
            content=self.stackCancha,
            margin=margin.symmetric(10, 50),
            expand=True
        )

        return self.inicializarComponentes()

    def inicializarComponentes(self):
        encabezadoComandos = Text(
            value="Comandos",
            size=16,
            color="#D9D9D9"
        )
        encabezadoLogs = Text(
            value="Logs",
            size=16,
            color="#D9D9D9"
        )

        self.listViewLogs = ListView(
            controls=self.listaLogs,
            expand=True,
            auto_scroll=True
        )

        buttonRegresar = IconButton(
            icon=icons.KEYBOARD_RETURN_ROUNDED,
            icon_color="#b3b3cc",
            icon_size=16,
            on_click=self.regresar
        )
        buttonAumentarMarcadorIzquierdo = TextButton(
            content=Text("+", size=18, color="#001f60", font_family="Nunito Bold"),
            style=ButtonStyle(
                padding=padding.all(0)
            ),
            height=30,
            width=30,
            on_click=self.aumentarMarcadorIzquierdo
        )
        buttonDisminuirMarcadorIzquierdo = TextButton(
            content=Text("-", size=18, color="#001f60", font_family="Nunito Bold"),
            style=ButtonStyle(
                padding=padding.all(0)
            ),
            height=30,
            width=30,
            on_click=self.disminuirMarcadorIzquierdo
        )
        buttonAumentarMarcadorDerecho = TextButton(
            content=Text("+", size=18, color="#001f60", font_family="Nunito Bold"),
            style=ButtonStyle(
                padding=padding.all(0)
            ),
            height=30,
            width=30,
            on_click=self.aumentarMarcadorDerecho
        )
        buttonDisminuirMarcadorDerecho = TextButton(
            content=Text("-", size=18, color="#001f60", font_family="Nunito Bold"),
            style=ButtonStyle(
                padding=padding.all(0)
            ),
            height=30,
            width=30,
            on_click=self.disminuirMarcadorDerecho
        )
        buttonActividadTiempoIzquierda = ElevatedButton(
            content=Text(
                value="T",
                size=16,
                color=colors.WHITE
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            width=50
        )
        buttonActividadCambioIzquierda = ElevatedButton(
            content=Text(
                value="C",
                size=16,
                color=colors.WHITE
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            width=50
        )
        buttonActividadTiempoDerecha = ElevatedButton(
            content=Text(
                value="T",
                size=16,
                color=colors.WHITE
            ),
            bgcolor="#D50037",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            width=50
        )
        buttonActividadCambioDerecha = ElevatedButton(
            content=Text(
                value="C",
                size=16,
                color=colors.WHITE
            ),
            bgcolor="#D50037",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            width=50
        )
        buttonAccionSaque = ElevatedButton(
            content=Text(
                value="Saque",
                size=14,
                color=colors.WHITE
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            width=100,
            on_click=self.agregarAccion,
            data="S"
        )
        buttonAccionPase = ElevatedButton(
            content=Text(
                value="Pase",
                size=14,
                color=colors.WHITE
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            width=100,
            on_click=self.agregarAccion,
            data="P"
        )
        buttonAccionAcomodo = ElevatedButton(
            content=Text(
                value="Acomodo",
                size=14,
                color=colors.WHITE
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            width=100,
            on_click=self.agregarAccion,
            data="A"
        )
        buttonAccionRemate = ElevatedButton(
            content=Text(
                value="Remate",
                size=14,
                color=colors.WHITE
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            width=100,
            on_click=self.agregarAccion,
            data="R"
        )
        buttonAccionBloqueo = ElevatedButton(
            content=Text(
                value="Bloqueo",
                size=14,
                color=colors.WHITE
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            width=100,
            on_click=self.agregarAccion,
            data="B"
        )
        buttonDeshacerUltimaAccion = ElevatedButton(
            content=Icon(name=icons.UNDO, color=colors.WHITE),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5),
                padding=padding.symmetric(5, 5)
            ),
            tooltip="Deshacer última acción"
        )
        buttonPuntoEquipoIzquierda = ElevatedButton(
            content=Text(value="Pt", color=colors.WHITE),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5),
                padding=padding.symmetric(5, 5)
            ),
            tooltip="Punto para equipo A",
            on_click=self.terminarPunto,
            data="A"
        )
        buttonPuntoEquipoDerecha = ElevatedButton(
            content=Text(value="Pt", color=colors.WHITE),
            bgcolor="#D50037",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5),
                padding=padding.symmetric(5, 5)
            ),
            tooltip="Punto para equipo B",
            on_click=self.terminarPunto,
            data="B"
        )

        columnBotonesMarcadorIzquierdo = Column(
            controls=[
                buttonAumentarMarcadorIzquierdo,
                buttonDisminuirMarcadorIzquierdo
            ],
            spacing=0
        )
        columnBotonesMarcadorDerecho = Column(
            controls=[
                buttonAumentarMarcadorDerecho,
                buttonDisminuirMarcadorDerecho
            ],
            spacing=0
        )

        containerMarcadorIzquierdo = Container(
            content=self.textMarcadorPropio,
            padding=padding.symmetric(5, 10),
            bgcolor="#001f60",
            border_radius=12.5
        )
        containerMarcadorDerecho = Container(
            content=self.textMarcadorContrario,
            padding=padding.symmetric(5, 10),
            bgcolor="#D50037",
            border_radius=12.5
        )
        containerNombreEquipoPropio = Container(
            content=self.textEquipoPropio,
            padding=padding.only(0, 5, 0, 0),
            border=border.only(bottom=BorderSide(1, "#001f60"))
        )
        containerNombreEquipoContrario = Container(
            content=self.textEquipoContrario,
            padding=padding.only(0, 5, 0, 0),
            border=border.only(bottom=BorderSide(1, "#D50037"))
        )
        containerJugadoresPropios = Container(
            content=self.columnListaJugadoresPropios,
            margin=margin.symmetric(0, 15),
            bgcolor=colors.WHITE,
            expand=True
        )
        containerJugadoresContrarios = Container(
            content=self.columnListaJugadoresContrarios,
            margin=margin.symmetric(0, 15),
            bgcolor=colors.WHITE,
            expand=True
        )
        self.containerImagenCancha = Container(
            content=self.stackCancha,
            margin=margin.symmetric(10, 50),
            expand=True,
            #border=border.all(1, color=colors.BLACK)
        )
        containerEncabezadoComandos = Container(
            content=encabezadoComandos,
            bgcolor="#001f60",
            alignment=alignment.center,
            padding=2.5
        )
        containerEncabezadoLogs = Container(
            content=encabezadoLogs,
            bgcolor="#001f60",
            alignment=alignment.center,
            padding=2.5
        )
        containerInputComandos = Container(
            content=self.inputComandos,
            bgcolor="#D9D9D9",
            border_radius=12.5,
            expand=True,
            border=border.all(1, color="#001f60")
        )
        containerLogs = Container(
            content=self.listViewLogs,
            margin=margin.symmetric(15, 20),
            expand=True,
            bgcolor="#D9D9D9",
            padding=10,
            border_radius=12.5
        )
        containerButtonDeshacer = Container(
            content=buttonDeshacerUltimaAccion,
            margin=margin.only(0, 20, 20, 20)
        )

        rowMenuOpciones = Row(
            controls=[
                buttonRegresar,
                self.textNumeroSet,
                buttonRegresar
            ],
            alignment="spaceBetween"
        )
        rowBotonesIzquierdos = Row(
            controls=[
                buttonActividadTiempoIzquierda,
                buttonActividadCambioIzquierda
            ]
        )
        rowBotonesDerechos = Row(
            controls=[
                buttonActividadTiempoDerecha,
                buttonActividadCambioDerecha
            ]
        )
        rowMarcadores = Row(
            controls=[
                rowBotonesIzquierdos,
                Row(
                    controls=[
                        columnBotonesMarcadorIzquierdo,
                        containerMarcadorIzquierdo,
                        Text("-", size=18, color="#001f60", font_family="Nunito Bold"),
                        containerMarcadorDerecho,
                        columnBotonesMarcadorDerecho
                    ],
                    expand=True,
                    alignment="center"
                ),
                rowBotonesDerechos
            ],
            alignment="center"
        )
        rowBotonesAccion = Row(
            controls=[
                buttonAccionSaque,
                buttonAccionPase,
                buttonAccionAcomodo,
                buttonAccionRemate,
                buttonAccionBloqueo
            ],
            alignment="spaceEvenly"
        )
        rowLogs = Row(
            controls=[
                containerLogs,
                containerButtonDeshacer
            ],
            vertical_alignment="center",
            expand=True,
            spacing=0
        )
        rowComandos = Row(
            controls=[
                buttonPuntoEquipoIzquierda,
                containerInputComandos,
                buttonPuntoEquipoDerecha
            ]
        )

        containerComandosButtons = Container(
            content=rowComandos,
            expand=True,
            padding=25,
            alignment=alignment.center
        )
        containerMarcadores = Container(
            content=rowMarcadores,
            padding=padding.symmetric(0, 20)
        )

        columnCancha = Column(
            controls=[
                containerMarcadores,
                self.containerImagenCancha,
                rowBotonesAccion
            ],
            horizontal_alignment="center"
        )
        columnEquipoPropio = Column(
            controls=[
                containerNombreEquipoPropio,
                containerJugadoresPropios
            ],
            horizontal_alignment="center",
            spacing=0
        )
        columnEquipoContrario = Column(
            controls=[
                containerNombreEquipoContrario,
                containerJugadoresContrarios
            ],
            horizontal_alignment="center",
            spacing=0
        )
        columnComandos = Column(
            controls=[
                containerEncabezadoComandos,
                containerComandosButtons
            ],
            spacing=0,
            expand=True,
            alignment="start"
        )
        columnLogs = Column(
            controls=[
                containerEncabezadoLogs,
                rowLogs
            ],
            spacing=0,
            expand=True,
            alignment="start"
        )

        containerCancha = Container(
            content=columnCancha,
            expand=True,
            padding=padding.only(0, 0, 0, 20)
        )
        containerEquipoPropio = Container(
            content=columnEquipoPropio,
            bgcolor=colors.WHITE
        )
        containerEquipoContrario = Container(
            content=columnEquipoContrario,
            bgcolor=colors.WHITE
        )

        rowEquiposCancha = Row(
            controls=[
                containerEquipoPropio,
                containerCancha,
                containerEquipoContrario
            ],
            spacing=0,
            alignment="spaceBetween",
            expand=True
        )
        rowComandosLogs = Row(
            controls=[
                columnComandos,
                columnLogs
            ],
            spacing=0
        )

        containerMenuOpciones = Container(
            content=rowMenuOpciones,
            bgcolor="#001F60",
            alignment=alignment.center,
            padding=5
        )
        containerEquiposCancha = Container(
            content=rowEquiposCancha,
            alignment=alignment.center,
            expand=True
        )
        containerComandosLogs = Container(
            content=rowComandosLogs,
            alignment=alignment.center,
            height=150,
            bgcolor=colors.WHITE
        )

        columnRegistrarEquipoVista = Column(
            controls=[
                containerMenuOpciones,
                containerEquiposCancha,
                containerComandosLogs
            ],
            spacing=0
        )

        containerRegistrarEquipoVista = Container(
            content=columnRegistrarEquipoVista
        )

        return containerRegistrarEquipoVista

    def obtenerContenedoresJugadores(self, contrario: bool):
        if contrario:
            jugadores = self.obtenerJugadoresContrarios()
            color = "#D50037"
        else:
            jugadores = self.obtenerJugadoresPropios()
            color = "#001f60"

        filasJugadores = []

        for jugador in jugadores:
            filasJugadores.append(
                Container(
                    content=Row(
                        controls=[
                            Text(
                                value=jugador.getNumero(),
                                size=14,
                                color=color,
                                text_align="start"
                            ),
                            Text(
                                value=jugador.getNombre(),
                                size=14,
                                color=color,
                                text_align="start"
                            ),
                            Container(

                            )
                        ],
                        expand=True
                    ),
                    padding=padding.symmetric(5, 0)
                )
            )

        if contrario:
            self.listaJugadoresContrarios = filasJugadores
        else:
            self.listaJugadoresPropios = filasJugadores

    def iniciarContenedoresZonas(self):
        columnZonasAtrasNumeros = Column(
            controls=[
                self.construirContenedoresZonasEnCancha(False, "1"),
                self.construirContenedoresZonasEnCancha(False, "2"),
                self.construirContenedoresZonasEnCancha(False, "3")
            ],
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True
        )
        columnZonasCentroNumeros = Column(
            controls=[
                self.construirContenedoresZonasEnCancha(False, "4"),
                self.construirContenedoresZonasEnCancha(False, "5"),
                self.construirContenedoresZonasEnCancha(False, "6")
            ],
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True
        )
        columnZonasDelanteNumeros = Column(
            controls=[
                self.construirContenedoresZonasEnCancha(False, "7"),
                self.construirContenedoresZonasEnCancha(False, "8"),
                self.construirContenedoresZonasEnCancha(False, "9")
            ],
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True
        )
        columnZonasAtrasLetras = Column(
            controls=[
                self.construirContenedoresZonasEnCancha(True, "A"),
                self.construirContenedoresZonasEnCancha(True, "B"),
                self.construirContenedoresZonasEnCancha(True, "C")
            ],
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True
        )
        columnZonasCentroLetras = Column(
            controls=[
                self.construirContenedoresZonasEnCancha(True, "D"),
                self.construirContenedoresZonasEnCancha(True, "E"),
                self.construirContenedoresZonasEnCancha(True, "F")
            ],
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True
        )
        columnZonasDelanteLetras = Column(
            controls=[
                self.construirContenedoresZonasEnCancha(True, "G"),
                self.construirContenedoresZonasEnCancha(True, "H"),
                self.construirContenedoresZonasEnCancha(True, "I")
            ],
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True
        )

        rowZonasIzquierda = Row(
            controls=[
                Container(
                    content=columnZonasAtrasNumeros,
                    expand=1,
                    alignment=alignment.center
                ),
                Container(
                    content=columnZonasCentroNumeros,
                    expand=1,
                    alignment=alignment.center
                ),
                Container(
                    content=columnZonasDelanteNumeros,
                    expand=1,
                    alignment=alignment.center
                )
            ],
            expand=True,
            alignment="center",
            spacing=0
        )
        rowZonasDerecha = Row(
            controls=[
                Container(
                    content=columnZonasDelanteLetras,
                    expand=1,
                    alignment=alignment.center
                ),
                Container(
                    content=columnZonasCentroLetras,
                    expand=1,
                    alignment=alignment.center
                ),
                Container(
                    content=columnZonasAtrasLetras,
                    expand=1,
                    alignment=alignment.center
                )
            ],
            expand=True,
            alignment="center",
            spacing=0
        )

        rowMallaZonas = Row(
            controls=[
                rowZonasIzquierda,
                rowZonasDerecha
            ],
            alignment="spaceEvenly",
            expand=True
        )
        columnMallaZonas = Column(
            controls=[
                rowMallaZonas
            ],
            alignment="center",
            expand=True
        )

        self.containerZonasCancha = Container(
            content=columnMallaZonas,
            expand=True,
            margin=margin.only(29, 24, 31, 25)
        )

        return self.containerZonasCancha

    def iniciarContenedoresJugadoresCancha(self):
        columnJugadoresZaguerosIzquierda = Column(
            controls=self.construirColumnaZagueros(False),
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True
        )
        columnJugadoresDelanterosIzquierda = Column(
            controls=self.construirColumnaDelanteros(False),
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True
        )
        columnJugadoresZaguerosDerecha = Column(
            controls=self.construirColumnaZagueros(True),
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True
        )
        columnJugadoresDelanterosDerecha = Column(
            controls=self.construirColumnaDelanteros(True),
            alignment="spaceEvenly",
            horizontal_alignment="center",
            expand=True
        )
        rowJugadoresIzquierda = Row(
            controls=[
                Container(
                    content=columnJugadoresZaguerosIzquierda,
                    expand=2,
                    alignment=alignment.center
                ),
                Container(
                    content=columnJugadoresDelanterosIzquierda,
                    expand=1,
                    alignment=alignment.center
                )
            ],
            expand=True,
            alignment="center",
            spacing=0
        )
        rowJugadoresDerecha = Row(
            controls=[
                Container(
                    content=columnJugadoresDelanterosDerecha,
                    expand=1,
                    alignment=alignment.center
                ),
                Container(
                    content=columnJugadoresZaguerosDerecha,
                    expand=2,
                    alignment=alignment.center
                )
            ],
            expand=True,
            alignment="center",
            spacing=0
        )

        rowMallaJugadores = Row(
            controls=[
                rowJugadoresIzquierda,
                rowJugadoresDerecha
            ],
            alignment="spaceEvenly",
            expand=True
        )
        columnMallaJugadores = Column(
            controls=[
                rowMallaJugadores
            ],
            alignment="center",
            expand=True
        )

        self.containerJugadoresEnCancha = Container(
            content=columnMallaJugadores,
            expand=True,
            margin=margin.only(53, 26, 55, 27)
        )

        return self.containerJugadoresEnCancha

    def obtenerNombreEquipoPropio(self):
        from Controllers.RegistrarPartidoControl import RegistrarPartidoControlador
        controlador = RegistrarPartidoControlador(self.pagina)
        return controlador.obtenerNombreEquipoPropio()

    def obtenerJugadoresPropios(self):
        from Controllers.RegistrarPartidoControl import RegistrarPartidoControlador
        controlador = RegistrarPartidoControlador(self.pagina)
        return controlador.obtenerJugadoresPropios()

    def obtenerNombreEquipoContrario(self):
        from Controllers.RegistrarPartidoControl import RegistrarPartidoControlador
        controlador = RegistrarPartidoControlador(self.pagina)
        return controlador.obtenerNombreEquipoContrario()

    def obtenerJugadoresContrarios(self):
        from Controllers.RegistrarPartidoControl import RegistrarPartidoControlador
        controlador = RegistrarPartidoControlador(self.pagina)
        return controlador.obtenerJugadoresContrarios()

    def regresar(self, e):
        from Controllers.RegistrarPartidoControl import RegistrarPartidoControlador
        controlador = RegistrarPartidoControlador(self.pagina)
        self.pagina.session.remove("puntos")
        self.pagina.session.remove("sets")
        self.pagina.session.remove("partidoRegistrado")
        controlador.regresar()

    def setLogs(self):
        logs = []
        for i in range(0, 50):
            logs.append(Text(f"Jugador va en {i}"))

        return logs

    def definirJugadoresEnCancha(self, contrario: bool):
        if contrario:
            jugadores = [
                self.obtenerJugadoresContrarios()[0],
                self.obtenerJugadoresContrarios()[1],
                self.obtenerJugadoresContrarios()[2],
                self.obtenerJugadoresContrarios()[3],
                self.obtenerJugadoresContrarios()[4],
                self.obtenerJugadoresContrarios()[5]
            ]
        else:
            jugadores = [
                self.obtenerJugadoresPropios()[0],
                self.obtenerJugadoresPropios()[1],
                self.obtenerJugadoresPropios()[2],
                self.obtenerJugadoresPropios()[3],
                self.obtenerJugadoresPropios()[4],
                self.obtenerJugadoresPropios()[5]
            ]
        return jugadores

    def construirContenedoresJugadoresEnCancha(self, contrario: bool):
        if contrario:
            jugadores = self.jugadoresContrariosEnCancha
            self.contenedoresJugadoresContrariosEnCancha.clear()
            contenedores = self.contenedoresJugadoresContrariosEnCancha
            color = "#D50037"
        else:
            jugadores = self.jugadoresPropiosEnCancha
            self.contenedoresJugadoresPropiosEnCancha.clear()
            contenedores = self.contenedoresJugadoresPropiosEnCancha
            color = "#001F60"

        for jugador in jugadores:
            contenedores.append(
                Container(
                    content=Text(value=f"{jugador.getNumero()}", color=colors.WHITE),
                    width=45,
                    height=45,
                    border_radius=50,
                    bgcolor=color,
                    alignment=alignment.center,
                    on_hover=self.jugadorHover,
                    on_click=self.jugadorClickeado,
                    data={
                        "jugador": jugador,
                        "contrario": contrario
                    }
                )
            )

    def construirContenedoresZonasEnCancha(self, contrario: bool, zona: str):
        if not contrario:
            color = "#001f60"
        else:
            color = "#D50037"

        return Row(
            controls=[
                Container(
                    content=Text(zona, color=colors.WHITE),
                    bgcolor=color,
                    expand=True,
                    alignment=alignment.center,
                    opacity=0.2,
                    on_hover=self.zonaOnHover,
                    on_click=self.zonaClickeada,
                    data=zona
                )
            ],
            expand=1
        )

    def construirColumnaZagueros(self, contrario: bool):
        if contrario:
            return [
                self.contenedoresJugadoresContrariosEnCancha[0],
                self.contenedoresJugadoresContrariosEnCancha[5],
                self.contenedoresJugadoresContrariosEnCancha[4]
            ]
        else:
            return [
                self.contenedoresJugadoresPropiosEnCancha[4],
                self.contenedoresJugadoresPropiosEnCancha[5],
                self.contenedoresJugadoresPropiosEnCancha[0]
            ]

    def construirColumnaDelanteros(self, contrario: bool):
        if contrario:
            return [
                self.contenedoresJugadoresContrariosEnCancha[1],
                self.contenedoresJugadoresContrariosEnCancha[2],
                self.contenedoresJugadoresContrariosEnCancha[3]
            ]
        else:
            return [
                self.contenedoresJugadoresPropiosEnCancha[3],
                self.contenedoresJugadoresPropiosEnCancha[2],
                self.contenedoresJugadoresPropiosEnCancha[1]
            ]

    def jugadorHover(self, e):
        e.control.opacity = 0.75 if e.data == "true" else 1.0
        self.update()

    def zonaOnHover(self, e):
        e.control.opacity = 0.5 if e.data == "true" else 0.2
        self.update()

    def reescalarZonas(self, e):
        if not self.reescalado:
            self.containerZonasCancha.margin = margin.only(53, 26, 55, 27)
            self.containerJugadoresEnCancha.margin = margin.only(53, 26, 55, 27)
        else:
            self.containerZonasCancha.margin = margin.only(29, 24, 31, 25)
            self.containerJugadoresEnCancha.margin = margin.only(29, 24, 31, 25)
        self.update()
        self.reescalado = not self.reescalado

    def jugadorClickeado(self, e):
        self.quitarBordesContenedores()
        self.jugador = e.control.data.get('jugador')
        self.contrario = True if e.control.data.get("contrario") else False
        if self.accionesIniciadas:
            self.accionEnProceso += "B" if e.control.data.get("contrario") else "A"
            self.accionEnProceso += f"{e.control.data.get('jugador').getNumero()}:"
        else:
            self.accionEnProceso = "B" if e.control.data.get("contrario") else "A"
            self.accionEnProceso += f"{e.control.data.get('jugador').getNumero()}:"
        e.control.border = border.all(2, color=colors.WHITE)
        self.jugadorSeleccionado = e.control
        self.inputComandos.hint_text = self.accionEnProceso
        self.accionesIniciadas = True
        self.update()

    def agregarAccion(self, e):
        self.quitarBordesContenedores()
        if self.accionesIniciadas and not self.zonasPorSeleccionar:
            self.accionEnProceso += f"{e.control.data}"
            self.tipoAccion = e.control.data
            self.inputComandos.hint_text = self.accionEnProceso
            self.contenidoCancha = self.iniciarContenedoresZonas()
            self.stackCancha.controls = [
                self.imagenCancha,
                self.contenidoCancha
            ]
            self.zonasPorSeleccionar = True
            self.update()

    def zonaClickeada(self, e):
        if self.zonaInicial == "":
            self.zonaInicial = e.control.data
            self.accionEnProceso += self.zonaInicial + "-"
            self.inputComandos.hint_text = f"{self.accionEnProceso}"
            e.control.border = border.all(2, color=colors.WHITE)
            self.update()
        elif self.zonaFinal == "":
            self.zonaFinal = e.control.data
            self.accionEnProceso += self.zonaFinal
            self.inputComandos.hint_text = f"{self.accionEnProceso}"
            e.control.border = border.all(2, color=colors.WHITE)
            self.update()
            self.terminarAccion()

    def terminarAccion(self):
        if self.tipoAccion == "S":
            accionAgregar = Saque(self.puntoActual.getId(), self.jugador.getId(), "++",
                                  self.zonaInicial, self.zonaFinal, self.contrario)
        elif self.tipoAccion == "P":
            accionAgregar = Pase(self.puntoActual.getId(), self.jugador.getId(), "++",
                                  self.zonaInicial, self.zonaFinal, self.contrario)
        elif self.tipoAccion == "A":
            accionAgregar = Acomodo(self.puntoActual.getId(), self.jugador.getId(), "++",
                                 self.zonaInicial, self.zonaFinal, self.contrario)
        elif self.tipoAccion == "R":
            accionAgregar = Remate(self.puntoActual.getId(), self.jugador.getId(), "++",
                                 self.zonaInicial, self.zonaFinal, self.contrario)
        else:
            accionAgregar = Pase(self.puntoActual.getId(), self.jugador.getId(), "++",
                                 self.zonaInicial, self.zonaFinal, self.contrario)

        self.puntoActual.agregarAccion(accionAgregar)

        self.accionesIniciadas = False
        self.zonasPorSeleccionar = False
        self.accionEnProceso += "."
        self.accionesEnPunto += self.accionEnProceso
        self.traducirComando()

        self.accionEnProceso = ""
        self.zonaInicial = ""
        self.zonaFinal = ""

        self.inputComandos.hint_text = self.accionesEnPunto
        self.contenidoCancha = self.iniciarContenedoresJugadoresCancha()
        self.stackCancha.controls = [
            self.imagenCancha,
            self.contenidoCancha
        ]
        self.update()

    def aumentarMarcadorIzquierdo(self, e):
        self.marcadorPropio += 1
        self.textMarcadorPropio.value = f"{self.marcadorPropio}"
        self.update()

    def aumentarMarcadorDerecho(self, e):
        self.marcadorContrario += 1
        self.textMarcadorContrario.value = f"{self.marcadorContrario}"
        self.update()

    def disminuirMarcadorIzquierdo(self, e):
        if self.marcadorPropio > 0:
            self.marcadorPropio -= 1
        else:
            self.marcadorPropio = 0
        self.textMarcadorPropio.value = f"{self.marcadorPropio}"
        self.update()

    def disminuirMarcadorDerecho(self, e):
        if self.marcadorContrario > 0:
            self.marcadorContrario -= 1
        else:
            self.marcadorContrario = 0
        self.textMarcadorContrario.value = f"{self.marcadorContrario}"
        self.update()

    def quitarBordesContenedores(self):
        if self.jugadorSeleccionado is not None:
            self.jugadorSeleccionado.border = None

    def traducirComando(self):
        from Controllers.RegistrarPartidoControl import RegistrarPartidoControlador
        controlador = RegistrarPartidoControlador(self.pagina)
        lado = "A"
        traduccion = controlador.registrarAccion(self.accionEnProceso, lado)
        self.listaLogs.append(
            Text(f"\t{traduccion}")
        )
        self.listViewLogs.controls = self.listaLogs
        self.update()

    def iniciarPartido(self):
        idPartido = self.pagina.session.get("partidoRegistrado").getId()
        nuevoSet = Set(self.numeroSet, idPartido, self.puntosSet)
        nuevoSet.setId(1)
        self.setActual = nuevoSet
        self.puntoActual = Punto(self.setActual.getId(), 0, 0)
        self.iniciarSet()

    def iniciarSet(self):
        self.marcadorPropio = 0
        self.marcadorContrario = 0
        self.listaLogs.append(Text(f"Punto {len(self.listaLogs) + 1}"))

    def iniciarPunto(self):
        idAnterior = self.puntoActual.getId()
        self.puntoActual = Punto(self.setActual.getId(), self.marcadorPropio, self.marcadorContrario)
        self.puntoActual.setId(idAnterior + 1)

    def terminarSet(self):
        from Controllers.RegistrarPartidoControl import RegistrarPartidoControlador
        controlador = RegistrarPartidoControlador(self.pagina)
        controlador.agregarSet(self.setActual)
        self.listaLogs = []
        self.listViewLogs.controls = self.listaLogs
        self.update()
        self.numeroSet = self.numeroSet + 1
        if self.numeroSet == self.setsObjetivo:
            self.puntosSet = 15
        idPartido = self.pagina.session.get("partidoRegistrado").getId()
        idSetActual = self.setActual.getId()
        nuevoSet = Set(self.numeroSet, idPartido, self.puntosSet)
        nuevoSet.setId(idSetActual)
        self.setActual = nuevoSet
        self.textNumeroSet.value = f"Set {self.numeroSet}"
        self.update()
        self.iniciarSet()

    def terminarPunto(self, e):
        if e.control.data == "A":
            self.aumentarMarcadorIzquierdo(e)
            self.puntoActual.setResultado(True)
        elif e.control.data == "B":
            self.aumentarMarcadorDerecho(e)
            self.puntoActual.setResultado(False)
        self.setActual.agregarPunto(self.puntoActual)
        if self.marcadorPropio == 25 or ((self.marcadorPropio - self.marcadorContrario >= 2)
                                         and self.marcadorPropio >= 24):
            self.terminarSet()
        elif self.marcadorContrario == 25 or ((self.marcadorContrario - self.marcadorPropio >= 2)
                                         and self.marcadorContrario >= 24):
            self.terminarSet()
        else:
            self.listaLogs.append(Text(f"Punto {self.puntoActual.getId()}"))
            self.listViewLogs.controls = self.listaLogs
            self.update()
        self.inputComandos.hint_text = ""
        self.accionesEnPunto = ""
        self.accionEnProceso = ""
        self.zonaInicial = ""
        self.zonaFinal = ""
        self.iniciarPunto()
