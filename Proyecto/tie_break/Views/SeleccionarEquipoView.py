from flet import *
from flet import UserControl, Page, colors, padding, border, margin, icons
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder


class SeleccionarEquipoVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.listaEquipos = None
        self.equipoSeleccionado = None
        self.nombreEquipo = None
        self.tituloNombreEquipo = None
        self.filasJugadores = []
        self.columnListaJugadores = None
        self.jugadorAEditar = None

        self.dialogEditarJugador: AlertDialog = None

        self.inputEditarNumero = TextField(max_length=3, text_size=14, content_padding=5, color="#001f60",
                                      expand=1, border_radius=12.5,
                                      counter_text=None, counter_style=TextStyle(size=0), border_width=0)
        self.inputEditarNombre = TextField(text_size=14, content_padding=5, color="#001f60",
                                      expand=4, border_radius=12.5,
                                      counter_text="Hola", counter_style=TextStyle(size=0), border_width=0)
        self.inputEditarPosicion = TextField(text_size=14, content_padding=5, color="#001f60",
                                      expand=3, border_radius=12.5,
                                      counter_text="Hola", counter_style=TextStyle(size=0), border_width=0)
        self.inputEditarCapitan = Switch(on_change=self.inputEditarCapitanChanged)

        self.inputEditarCapitanCambiado: bool = False

    def build(self):
        self.expand = True
        self.listaEquipos = self.obtenerEquipos()
        self.equipoSeleccionado = self.listaEquipos[0]
        self.nombreEquipo = self.equipoSeleccionado.nombreEquipo
        self.tituloNombreEquipo = Text(
            value=f"{self.nombreEquipo}",
            color="#D9D9D9",
            size=32,
            font_family="Nunito"
        )
        self.obtenerContenedoresJugadores()
        self.columnListaJugadores = Column(
            controls=self.filasJugadores,
            scroll="auto",
            expand=True
        )
        self.obtenerContenedoresEquipos()
        return self.inicializarComponentes()

    def inicializarComponentes(self):
        tituloEquipos = Text(
            value="Equipos",
            color="#D9D9D9",
            size=40,
            font_family="Nunito",
            text_align="center"
        )
        encabezadoNumero = Text(
            value="No.",
            color="#001f60",
            size=24,
            font_family="Nunito",
            expand=1,
            text_align="center"
        )
        encabezadoJugador = Text(
            value="Jugador",
            color="#001f60",
            size=24,
            font_family="Nunito",
            expand=3,
            text_align="center"
        )
        encabezadoPosicion = Text(
            value="Posición",
            color="#001f60",
            size=24,
            font_family="Nunito",
            expand=2,
            text_align="center"
        )

        inputBuscarJugador = TextField(
            hint_text="Buscar Jugador",
            color="#001f60",
            text_size=16,
            border_radius=12.5,
            width=450,
            border_color=colors.WHITE,
            focused_border_color="#D9D9D9",
            content_padding=10
        )

        buttonRegresar = ElevatedButton(
            content=Row(
                controls=[
                    Icon(name=icons.KEYBOARD_RETURN_ROUNDED, color="#D9D9D9", size=22),
                    Text(value="Regresar", color="#D9D9D9", size=22)
                ],
                spacing=5
            ),
            width=150,
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            on_click=self.regresar
        )
        buttonSeleccionarEquipo = ElevatedButton(
            content=Text(
                value="Seleccionar equipo",
                size=22,
                color="#D9D9D9"
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            )
        )

        containerTituloEquipos = Container(
            content=tituloEquipos,
            expand=2
        )
        containerTituloNombreEquipo = Container(
            content=self.tituloNombreEquipo,
            padding=padding.symmetric(0, 5),
            expand=1
        )
        containerInputBuscarJugador = Container(
            content=inputBuscarJugador,
            border_radius=12.5,
            bgcolor=colors.WHITE,
            expand=1
        )
        containerButtonSeleccionarEquipo = Container(
            content=buttonSeleccionarEquipo,
            alignment=alignment.center_right,
            padding=10
        )
        containerButtonCerrarSesion = Container(
            content=buttonRegresar,
            alignment=alignment.center_left,
            padding=10
        )

        rowEquipoYBusqueda = Row(
            controls=[
                containerTituloNombreEquipo,
                containerInputBuscarJugador
            ],
            expand=4,
            alignment="spaceBetween"
        )
        rowEncabezadoVista = Row(
            controls=[
                containerTituloEquipos,
                rowEquipoYBusqueda
            ],
            expand=True
        )

        containerEncabezadoVista = Container(
            content=rowEncabezadoVista,
            bgcolor="#001f60",
            height=100,
            padding=padding.symmetric(0, 25)
        )

        columnListaDeEquipos = Column(
            controls=self.obtenerContenedoresEquipos(),
            alignment="center",
            scroll="auto",
            expand=True
        )

        containerColumnListaDeEquipos = Container(
            content=columnListaDeEquipos,
            padding=padding.symmetric(10, 0),
            expand=True
        )

        columnListaEquiposButtonCerrarSesion = Column(
            controls=[
                containerColumnListaDeEquipos,
                containerButtonCerrarSesion
            ],
            expand=2
        )

        rowEncabezadoTablaJugadores = Row(
            controls=[
                encabezadoNumero,
                encabezadoJugador,
                encabezadoPosicion,
                Container(
                    expand=1
                )
            ],
            expand=True
        )

        containerEncabezadoTablaJugadores = Container(
            content=rowEncabezadoTablaJugadores,
            height=75,
            alignment=alignment.center,
            border=border.only(bottom=BorderSide(2, "#001f60")),
            margin=margin.symmetric(0, 5),
            padding=padding.symmetric(0, 15)
        )

        columnTablaJugadores = Column(
            controls=[
                containerEncabezadoTablaJugadores,
                self.columnListaJugadores
            ]
        )

        containerTablaJugadores = Container(
            content=columnTablaJugadores,
            expand=True
        )

        columnTablaJugadoresButtonSeleccionarEquipo = Column(
            controls=[
                containerTablaJugadores,
                containerButtonSeleccionarEquipo
            ],
        )

        containerColumnTablaJugadoresButtonSeleccionarEquipo = Container(
            content=columnTablaJugadoresButtonSeleccionarEquipo,
            bgcolor=colors.WHITE,
            expand=4
        )

        rowListaEquiposTablaJugadores = Row(
            controls=[
                columnListaEquiposButtonCerrarSesion,
                containerColumnTablaJugadoresButtonSeleccionarEquipo
            ],
            expand=True,
            vertical_alignment="start",
            spacing=0
        )

        containerSeleccionarEquipoVista = Container(
            content=Column(
                [
                    containerEncabezadoVista,
                    rowListaEquiposTablaJugadores
                ],
                spacing=0
            )
        )

        return containerSeleccionarEquipoVista

    def obtenerContenedoresEquipos(self):
        contenedoresEquipos = []

        for equipo in self.listaEquipos:
            contenedoresEquipos.append(
                Container(
                    content=Text(
                        value=equipo.nombreEquipo,
                        text_align="start",
                        size=28,
                        color="#001f60"
                    ),
                    width=self.pagina.width,           # Solución algo rebuscada y nada optimizada, pero no encontré otra forma
                    margin=margin.symmetric(0, 10),
                    padding=padding.symmetric(10, 15),
                    bgcolor=colors.WHITE,
                    border_radius=12.5,
                    on_hover=self.containerEquipoOnHover,
                    on_click=self.containerEquipoOnClick
                )
            )

        return contenedoresEquipos

    def containerEquipoOnHover(self, e):
        e.control.bgcolor = "#001f60" if e.data == "true" else colors.WHITE
        e.control.content.color = "#D9D9D9" if e.data == "true" else "#001f60"
        e.control.update()

    def containerEquipoOnClick(self, e):
        equipoClickeado = self.equipoSeleccionado

        for equipo in self.listaEquipos:
            if e.control.content.value == equipo.nombreEquipo:
                equipoClickeado = equipo

        if not self.equipoSeleccionado:
            self.equipoSeleccionado = equipoClickeado
        elif not self.equipoSeleccionado.nombreEquipo == equipoClickeado.nombreEquipo:
            self.equipoSeleccionado = equipoClickeado

        self.tituloNombreEquipo.value = self.equipoSeleccionado.nombreEquipo
        self.obtenerContenedoresJugadores()
        self.update()

    def obtenerContenedoresJugadores(self):
        self.filasJugadores.clear()
        for jugador in self.equipoSeleccionado.getJugadores():
            self.filasJugadores.append(
                Container(
                    content=Row(
                        controls=[
                            Text(
                                value=jugador.getNumero(),
                                size=20,
                                color="#001f60",
                                expand=1,
                                text_align="center"
                            ),
                            Row(
                                controls=[
                                    Text(
                                        value=f"{jugador.getNombre()}",
                                        size=20,
                                        color="#001f60",
                                        text_align="center",
                                        expand=True
                                    ),
                                    Text(
                                        value=" C",
                                        size=20,
                                        color="#d50037",
                                        text_align="center",
                                        font_family="Nunito Bold",
                                        tooltip="Capitán del Equipo"
                                    ) if jugador.isCapitan() else Container(margin=0, padding=0, width=0)
                                ],
                                expand=3,
                                vertical_alignment="center"
                            ),
                            Text(
                                value=jugador.getPosicion(),
                                size=20,
                                color="#001f60",
                                expand=2,
                                text_align="center"
                            ),
                            Row(
                                controls=[
                                    IconButton(
                                        icon=icons.EDIT_NOTE,
                                        icon_color="#ffa400",
                                        on_click=self.abrirDialogEditarJugador,
                                        data=jugador
                                    ),
                                    IconButton(
                                        icon=icons.DELETE,
                                        icon_color="#d50037",
                                        on_click=self.borrarJugador,
                                        data=jugador
                                    )
                                ],
                                expand=1
                            )
                        ],
                        expand=True
                    ),
                    margin=margin.symmetric(5, 20),
                    border=border.only(bottom=BorderSide(1, "#001f60")),
                    padding=padding.symmetric(10, 0)
                )
            )

    def abrirDialogEditarJugador(self, e):
        jugador = e.control.data

        self.inputEditarNumero.hint_text = jugador.getNumero()
        self.inputEditarNombre.hint_text = jugador.getNombre()
        self.inputEditarPosicion.hint_text = jugador.getPosicion()
        self.inputEditarCapitan.value = jugador.isCapitan()

        self.inputEditarCapitanCambiado = False

        self.dialogEditarJugador = AlertDialog(
            modal=True,
            title=Text("Editar Jugador", text_align="center", color="#001f60"),
            content=Column(
                controls=[
                    Row(
                        controls=[
                            Text("No.", expand=1, text_align="center", color="#001f60", size=16),
                            Text("Nombre", expand=4, text_align="center", color="#001f60", size=16),
                            Text("Posición", expand=3, text_align="center", color="#001f60", size=16),
                            Text("Capitán", text_align="center", color="#001f60", size=16)
                        ]
                    ),
                    Row(
                        controls=[
                            self.inputEditarNumero,
                            self.inputEditarNombre,
                            self.inputEditarPosicion,
                            self.inputEditarCapitan
                        ]
                    )
                ],
                height=75,
                width=600
            ),
            actions=[
                TextButton(content=Text("Aceptar", color="#00BC06"), on_click=self.dialogEditarJugadorAceptado,
                           data=jugador),
                TextButton(content=Text("Cancelar", color="#d50037"), on_click=self.dialogEditarJugadorCancelado)
            ],
            actions_alignment="center"
        )
        self.pagina.dialog = self.dialogEditarJugador
        self.dialogEditarJugador.open = True
        self.pagina.update()

    def dialogEditarJugadorCancelado(self, e):
        self.dialogEditarJugador.open = False
        self.pagina.update()

    def dialogEditarJugadorAceptado(self, e):
        jugador = e.control.data

        if (self.inputEditarNumero.value == "" and self.inputEditarNombre.value == ""
                and self.inputEditarPosicion.value == "" and not self.inputEditarCapitanCambiado):
            self.dialogError("No se hizo nigún cambio")
        elif (self.inputEditarNumero.value == str(jugador.getNumero())
                and self.inputEditarNombre.value == jugador.getNombre()
                and self.inputEditarPosicion.value == jugador.getPosicion()
                and not self.inputEditarCapitanCambiado):
            self.dialogError("No se hizo nigún cambio")
        else:
            if not self.inputEditarNumero.value == "":
                jugador.setNumero(int(self.inputEditarNumero.value))
            if not self.inputEditarNombre.value == "":
                jugador.setNombre(self.inputEditarNombre.value)
            if not self.inputEditarPosicion.value == "":
                jugador.setPosicion(self.inputEditarPosicion.value)
            if self.inputEditarCapitanCambiado:
                jugador.setCapitan(self.inputEditarCapitan.value)

            self.dialogEditarJugador.open = False
            self.pagina.update()
            self.editarJugador(jugador)


    def dialogError(self, msg: str):
        self.dialogEditarJugador.title = Text("¡Error!", text_align="center", color="#d50037")
        self.dialogEditarJugador.content = Text(msg, text_align="center", size=20)
        self.dialogEditarJugador.actions = [
            TextButton(content=Text("Aceptar", color="#001f60"), on_click=self.dialogEditarJugadorCancelado)
        ]
        self.pagina.update()

    def inputEditarCapitanChanged(self, e):
        self.inputEditarCapitanCambiado = not self.inputEditarCapitanCambiado

    def obtenerEquipos(self):
        from Controllers.SeleccionarEquipoControl import SeleccionarEquipoControlador
        controlador = SeleccionarEquipoControlador(self.pagina)
        return controlador.obtenerEquipos()

    def borrarJugador(self, e):
        print(e.control.data.id)
        self.equipoSeleccionado.borrarJugador(e.control.data.id)
        self.obtenerContenedoresJugadores()
        self.update()

    def editarJugador(self, jugador):
        self.equipoSeleccionado.editarJugador(jugador)
        self.obtenerContenedoresJugadores()
        self.update()

    def regresar(self, e):
        from Controllers.SeleccionarEquipoControl import SeleccionarEquipoControlador
        controlador = SeleccionarEquipoControlador(self.pagina)
        controlador.regresar()
