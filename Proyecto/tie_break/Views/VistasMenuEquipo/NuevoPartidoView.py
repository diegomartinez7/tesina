from flet import *
from flet import padding, icons, margin, colors, border
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder


class NuevoPartidoView(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.textEquipoPropio = None
        self.textEquipoRivalSeleccionado = None
        self.listaEquiposRivales = []
        self.listaCompetencias = []
        self.equipoSeleccionado = None
        self.competenciaSeleccionada = None

        self.textEquipoContrario = None
        self.listaJugadoresPropios = []
        self.listaJugadoresContrarios = []
        self.columnListaJugadoresPropios = None
        self.columnListaJugadoresContrarios = None

    def build(self):
        self.expand = True
        self.listaEquiposRivales = self.obtenerListaEquipos()
        self.listaCompetencias = self.obtenerListaCompetencias()
        self.textEquipoPropio = Text(
            value=self.pagina.session.get("equipo").getNombre(),
            size=20,
            color=colors.WHITE
        )

        self.textEquipoRivalSeleccionado = Text(
            value="Seleccionar Equipo",
            size=20,
            color=colors.WHITE
        )
        self.obtenerContenedoresJugadores(False)
        self.columnListaJugadoresPropios = Column(
            controls=self.listaJugadoresPropios,
            spacing=0,
            expand=True
        )
        self.columnListaJugadoresContrarios = Column(
            controls=self.listaJugadoresContrarios,
            spacing=0,
            expand=True
        )
        return self.inicializarComponentes()

    def inicializarComponentes(self):
        labelInputCompetecnia = Text(
            value="Competencia",
            color="#001f60",
            size=16,
            font_family="Nunito"
        )
        labelInputUbicacion = Text(
            value="Ubicación",
            color="#001f60",
            size=16,
            font_family="Nunito"
        )
        labelInputFecha = Text(
            value="Fecha",
            color="#001f60",
            size=16,
            font_family="Nunito"
        )
        labelInputPuntos = Text(
            value="Puntos por set",
            color="#001f60",
            size=16,
            font_family="Nunito"
        )
        labelInputSets = Text(
            value="Sets",
            color="#001f60",
            size=16,
            font_family="Nunito"
        )

        dropdownCompetencias = Dropdown(
            width=400,
            options=self.obtenerContenedoresCompetencias(),
            color="#001f60",
            text_size=14,
            border_radius=12.5,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=10
        )
        inputUbicacion = TextField(
            color="#001f60",
            text_size=14,
            border_radius=12.5,
            width=250,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=10
        )
        inputFecha = TextField(
            color="#001f60",
            text_size=14,
            border_radius=12.5,
            width=250,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=10
        )
        inputPuntos = TextField(
            color="#001f60",
            text_size=14,
            border_radius=12.5,
            width=75,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=10
        )
        dropdownSets = Dropdown(
            width=75,
            options=[
                dropdown.Option("2/3"),
                dropdown.Option("3/5")
            ],
            color="#001f60",
            text_size=14,
            border_radius=12.5,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=10
        )

        containerCompetencias = Container(
            content=Column(
                controls=[
                    labelInputCompetecnia,
                    Container(
                        content=dropdownCompetencias,
                        bgcolor=colors.WHITE,
                        border_radius=12.5
                    )
                ],
                spacing=10,
                horizontal_alignment="center"
            )
        )
        containerUbicacion = Container(
            content=Column(
                controls=[
                    labelInputUbicacion,
                    Container(
                        content=inputUbicacion,
                        bgcolor=colors.WHITE,
                        border_radius=12.5
                    )
                ],
                spacing=10,
                horizontal_alignment="center"
            )
        )
        containerFecha = Container(
            content=Column(
                controls=[
                    labelInputFecha,
                    Container(
                        content=inputFecha,
                        bgcolor=colors.WHITE,
                        border_radius=12.5
                    )
                ],
                spacing=10,
                horizontal_alignment="center"
            )
        )
        containerPuntos = Container(
            content=Column(
                controls=[
                    labelInputPuntos,
                    Container(
                        content=inputPuntos,
                        bgcolor=colors.WHITE,
                        border_radius=12.5
                    )
                ],
                spacing=10,
                horizontal_alignment="center"
            )
        )
        containerSets = Container(
            content=Column(
                controls=[
                    labelInputSets,
                    Container(
                        content=dropdownSets,
                        bgcolor=colors.WHITE,
                        border_radius=12.5
                    )
                ],
                spacing=10,
                horizontal_alignment="center"
            )
        )

        rowNombreEquipoPropio = Row(
            [
                self.textEquipoPropio
            ],
            alignment="center"
        )
        rowNombreEquipoContrario = Row(
            [
                self.textEquipoRivalSeleccionado,
                Icon(
                    name=icons.ARROW_DROP_DOWN,
                    size=20,
                    color=colors.WHITE
                )
            ],
            alignment="center"
        )
        rowInputCompetencia = Row(
            [
                containerCompetencias
            ],
            alignment="center"
        )
        rowInputUbicacionFecha = Row(
            [
                containerUbicacion,
                containerFecha
            ],
            alignment="spaceEvenly"
        )
        rowInputPuntosSets = Row(
            [
                containerPuntos,
                containerSets
            ],
            alignment="spaceEvenly"
        )

        buttonNuevoRival = ElevatedButton(
            content=Text(
                value="Nuevo Rival",
                size=14,
                color="#ffa400"
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            # on_click=self.abrirDialogNuevoJugador
        )
        buttonIniciarPartido = ElevatedButton(
            content=Text(
                value="Iniciar Partido",
                size=16,
                color="#ffa400"
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            on_click=self.iniciarPartido
        )

        containerNombreEquipoPropio = Container(
            content=rowNombreEquipoPropio,
            padding=padding.only(0, 5, 0, 5),
            bgcolor="#001f60"
        )
        containerNombreEquipoContrario = Container(
            content=rowNombreEquipoContrario,
            padding=padding.only(0, 5, 0, 5),
            bgcolor="#D50037"
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
        containerButtonNuevoRival = Container(
            content=buttonNuevoRival,
            alignment=alignment.center,
            padding=10,
            bgcolor=colors.WHITE,
            margin=margin.symmetric(0, 50),
        )

        columnEquipoPropio = Column(
            controls=[
                containerNombreEquipoPropio,
                containerJugadoresPropios
            ],
            horizontal_alignment="center",
            spacing=0,
            expand=True
        )

        dropdownEquiposRivales = PopupMenuButton(
            content=containerNombreEquipoContrario,
            items=self.obtenerContenedoresNombresEquipos(),
            tooltip="Ver opciones"
        )

        columnEquipoContrario = Column(
            controls=[
                dropdownEquiposRivales,
                containerJugadoresContrarios,
                containerButtonNuevoRival
            ],
            horizontal_alignment="center",
            spacing=0,
            expand=True
        )
        columnDatosPartido = Column(
            controls=[
                rowInputCompetencia,
                rowInputUbicacionFecha,
                rowInputPuntosSets,
                buttonIniciarPartido
            ],
            horizontal_alignment="center",
            alignment="spaceEvenly"
        )

        containerEquipoPropio = Container(
            content=columnEquipoPropio,
            bgcolor=colors.WHITE,
            width=300
        )
        containerEquipoContrario = Container(
            content=columnEquipoContrario,
            bgcolor=colors.WHITE,
            width=300
        )
        containerDatosPartido = Container(
            content=columnDatosPartido,
            expand=True,
            padding=padding.symmetric(10, 20)
        )

        rowNuevoEquipo = Row(
            controls=[
                containerEquipoPropio,
                containerDatosPartido,
                containerEquipoContrario
            ],
            spacing=0,
            expand=True
        )
        columnNuevoEquipo = Column(
            controls=[
                rowNuevoEquipo
            ],
            expand=True,
            spacing=0
        )

        containerNuevoEquipo = Container(
            content=columnNuevoEquipo
        )

        return containerNuevoEquipo

    def obtenerContenedoresNombresEquipos(self):
        itemsEquipos = []

        for equipo in self.listaEquiposRivales:
            itemsEquipos.append(
                PopupMenuItem(
                    content=Text(
                        value=equipo.getNombre(),
                        size=16,
                        color="#001f60"
                    ),
                    on_click=self.equipoElegido,
                    data=equipo
                )
            )

        return itemsEquipos

    def obtenerContenedoresCompetencias(self):
        itemsCompetencias = []

        for competencia in self.listaCompetencias:
            itemsCompetencias.append(
                dropdown.Option(
                    competencia.getNombre()
                )
            )

        return itemsCompetencias

    def obtenerContenedoresJugadores(self, contrario: bool):
        if contrario:
            jugadores = self.obtenerJugadoresContrarios(self.equipoSeleccionado)
            color = "#001f60"
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

    def equipoElegido(self, e):
        self.equipoSeleccionado = e.control.data
        self.textEquipoRivalSeleccionado.value = self.equipoSeleccionado.getNombre()
        self.obtenerContenedoresJugadores(True)
        self.columnListaJugadoresContrarios.controls = self.listaJugadoresContrarios
        self.update()

    def obtenerListaEquipos(self):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerRivales()

    def obtenerListaCompetencias(self):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerCompetencias()

    def obtenerJugadoresContrarios(self, equipo):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerJugadoresContrarios(equipo)

    def obtenerJugadoresPropios(self):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerJugadores()

    def iniciarPartido(self, e):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        controlador.registrarPartido(self.equipoSeleccionado)
