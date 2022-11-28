from flet import *
from flet import UserControl, padding, border, icons, margin, colors
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder

# hace falta agregar la funcionalidad al botón de ver jugador
# hacer validaciones para sólo tener un capitán a la vez

class JugadoresVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.filasJugadores = []
        self.columnListaJugadores = None

        self.inputNumero = None
        self.inputNombre = None
        self.inputPosicion = None
        self.inputCapitan = None
        self.inputGenero = None
        self.dialogEquipo: AlertDialog = None

        self.inputEditarCapitanCambiado: bool = False

    def build(self):
        self.expand = True
        self.configurarDialog()
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

        buttonNuevoJugador = ElevatedButton(
            content=Text(
                value="Nuevo Jugador",
                size=16,
                color="#ffa400"
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            on_click=self.abrirDialogNuevoJugador
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

        containerButtonNuevoJugador = Container(
            content=buttonNuevoJugador,
            alignment=alignment.center_right,
            padding=10,
            bgcolor=colors.WHITE,
            margin=margin.symmetric(0, 50),
        )

        columnTablaJugadores = Column(
            controls=[
                containerEncabezado,
                containerListaJugadores,
                containerButtonNuevoJugador
            ],
            spacing=0,
            expand=True
        )

        containerJugadoresVista = Container(
            content=columnTablaJugadores
        )

        return containerJugadoresVista

    def obtenerContenedoresJugadores(self):
        self.filasJugadores.clear()
        for jugador in self.obtenerJugadores():
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
                                        tooltip="Ver Jugador",
                                        data=jugador
                                    ),
                                    IconButton(
                                        icon=icons.EDIT_NOTE,
                                        icon_color="#ffa400",
                                        tooltip="Editar Jugador",
                                        data=jugador,
                                        on_click=self.abrirDialogEditarJugador
                                    ),
                                    IconButton(
                                        icon=icons.DELETE,
                                        icon_color="#d50037",
                                        tooltip="Borrar Jugador",
                                        data=jugador,
                                        on_click=self.abrirDialogBorrarJugador
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

    def configurarDialog(self):
        self.dialogEquipo = AlertDialog(
            modal=True,
            title=Text("Añadir Jugador", text_align="center", color="#001f60"),
            content=Text("Aquí va el contenido del dialog"),
            actions=[
                TextButton(content=Text("Aceptar", color="#00BC06")),
                TextButton(content=Text("Cancelar", color="#d50037"))
            ],
            actions_alignment="center"
        )
        self.pagina.dialog = self.dialogEquipo

    def iniciarDialogNuevoJugador(self):
        self.inputNumero = TextField(max_length=3, text_size=14, content_padding=10, color="#001f60",
                                     expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     counter_text=None, counter_style=TextStyle(size=0), border_width=0)
        self.inputNombre = TextField(text_size=14, content_padding=10, color="#001f60",
                                     expand=4, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     counter_text="Hola", counter_style=TextStyle(size=0), border_width=0)
        self.inputPosicion = TextField(text_size=14, content_padding=10, color="#001f60",
                                       expand=3, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                       counter_text="Hola", counter_style=TextStyle(size=0), border_width=0)
        # self.inputGenero = Dropdown(options=[dropdown.Option("M"),dropdown.Option("F")],
        #     border_width=0, content_padding=10, filled=True, bgcolor="#D9D9D9", text_size=14, color="#001f60",
        #     counter_text="Hola", counter_style=TextStyle(size=0), border_radius=12.5, expand=1)
        self.inputCapitan = Switch()

        self.dialogEquipo.title = Text("Añadir Jugador", text_align="center", color="#001f60")
        self.dialogEquipo.content = Column(
            controls=[
                Row(
                    controls=[
                        Text("No.", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Nombre", expand=4, text_align="center", color="#001f60", size=16),
                        #Text("Genero", text_align="center", color="#001f60", size=16),
                        Text("Posición", expand=3, text_align="center", color="#001f60", size=16),
                        Text("Capitán", text_align="center", color="#001f60", size=16)
                    ]
                ),
                Row(
                    controls=[
                        self.inputNumero,
                        self.inputNombre,
                        #self.inputGenero,
                        self.inputPosicion,
                        self.inputCapitan
                    ]
                )
            ],
            height=75,
            width=600
        )
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#00BC06"), on_click=self.aceptarInsertarJugador),
            TextButton(content=Text("Cancelar", color="#d50037"), on_click=self.cerrarDialog)
        ]

    def iniciarDialogEditarJugador(self, jugador):
        self.inputNumero = TextField(max_length=3, text_size=14, content_padding=10, color="#001f60",
                                     expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     counter_text=None, counter_style=TextStyle(size=0), border_width=0,
                                     hint_text=jugador.getNumero())
        self.inputNombre = TextField(text_size=14, content_padding=10, color="#001f60",
                                     expand=4, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     counter_text="Hola", counter_style=TextStyle(size=0), border_width=0,
                                     hint_text=jugador.getNombre())
        self.inputPosicion = TextField(text_size=14, content_padding=10, color="#001f60",
                                       expand=3, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                       counter_text="Hola", counter_style=TextStyle(size=0), border_width=0,
                                       hint_text=jugador.getPosicion())
        self.inputCapitan = Switch(value=jugador.isCapitan(), on_change=self.inputEditarCapitanChanged)

        self.inputEditarCapitanCambiado = False

        self.dialogEquipo.title = Text("Editar Jugador", text_align="center", color="#001f60")
        self.dialogEquipo.content = Column(
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
                        self.inputNumero,
                        self.inputNombre,
                        self.inputPosicion,
                        self.inputCapitan
                    ]
                )
            ],
            height=75,
            width=600
        )
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#00BC06"), on_click=self.aceptarEditarJugador, data=jugador),
            TextButton(content=Text("Cancelar", color="#d50037"), on_click=self.cerrarDialog)
        ]

    def iniciarDialogBorrarJugador(self, jugador):
        self.dialogEquipo.title = Icon(name=icons.WARNING, color="#ffa400")
        self.dialogEquipo.content = Text(f"¿Deseas borrar a {jugador.getNombre()}?", text_align="center", size=20)
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#001f60"), on_click=self.aceptarBorrarJugador, data=jugador),
            TextButton(content=Text("Cancelar", color="#001f60"), on_click=self.cerrarDialog)
        ]

    def iniciarDialogError(self, msg):
        self.dialogEquipo.title = Text("¡Error!", text_align="center", color="#d50037")
        self.dialogEquipo.content = Text(msg, text_align="center", size=20)
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#001f60"), on_click=self.cerrarDialog)
        ]

    def iniciarDialogExito(self, msg):
        self.dialogEquipo.title = Icon(name=icons.DONE, color="#00BC06")
        self.dialogEquipo.content = Text(msg, text_align="center", size=20)
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#001f60"), on_click=self.cerrarDialog)
        ]

    def abrirDialogNuevoJugador(self, e):
        self.iniciarDialogNuevoJugador()
        self.dialogEquipo.open = True
        self.pagina.update()

    def abrirDialogEditarJugador(self, e):
        jugador = e.control.data
        self.iniciarDialogEditarJugador(jugador)
        self.dialogEquipo.open = True
        self.pagina.update()

    def abrirDialogBorrarJugador(self, e):
        jugador = e.control.data
        self.iniciarDialogBorrarJugador(jugador)
        self.dialogEquipo.open = True
        self.pagina.update()

    def abrirErrorDialog(self, msg):
        self.iniciarDialogError(msg)
        self.dialogEquipo.open = True
        self.pagina.update()

    def abrirDialogExito(self, msg):
        self.iniciarDialogExito(msg)
        self.dialogEquipo.open = True
        self.pagina.update()

    def cerrarDialog(self, e):
        self.dialogEquipo.open = False
        self.pagina.update()

    def aceptarInsertarJugador(self, e):
        numero = self.inputNumero.value
        nombre = self.inputNombre.value
        posicion = self.inputPosicion.value
        capitan = self.inputCapitan.value

        jugador = {
            "numero": numero,
            "nombre": nombre,
            "posicion": posicion,
            "capitan": capitan
        }

        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        if controlador.validarInsertarJugadorVacio(jugador):
            self.abrirErrorDialog("No se puede haber campos vacíos")
        else:
            self.dialogEquipo.open = False
            self.pagina.update()
            self.insertarJugador(jugador)

    def insertarJugador(self, jugador):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        if controlador.insertarJugador(jugador):
            self.abrirDialogExito("Jugador agregado con éxito")
            self.obtenerContenedoresJugadores()
            self.update()
        else:
            self.abrirErrorDialog("No se pudo insertar el jugador \n Valide que el nombre y el número no sean iguales")

    def aceptarEditarJugador(self, e):
        jugadorNoEditado = e.control.data

        numero = self.inputNumero.value
        nombre = self.inputNombre.value
        posicion = self.inputPosicion.value
        capitan = self.inputCapitan.value

        jugadorEditado = {
            "numero": numero,
            "nombre": nombre,
            "posicion": posicion,
            "capitan": capitan
        }

        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        if controlador.validarEditarJugadorVacio(jugadorEditado, self.inputEditarCapitanCambiado):
            self.abrirErrorDialog("No se ha cambiado nada del jugador")
        elif controlador.vaildarJugadoresIguales(jugadorEditado, jugadorNoEditado):
            self.abrirErrorDialog("No se hizo ningún cambio")
        else:
            self.dialogEquipo.open = False
            self.pagina.update()
            jugadorEditado = controlador.construirJugadorEditado(jugadorEditado, jugadorNoEditado)
            self.editarJugador(jugadorEditado)

    def editarJugador(self, jugador):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        controlador.editarJugador(jugador)
        self.abrirDialogExito("Jugador editado con éxito")
        self.obtenerContenedoresJugadores()
        self.update()

    def aceptarBorrarJugador(self, e):
        jugadorBorrado = e.control.data
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        controlador.borrarJugador(jugadorBorrado)
        self.abrirDialogExito("Jugador borrado con éxito")
        self.obtenerContenedoresJugadores()
        self.update()

    def inputEditarCapitanChanged(self, e):
        self.inputEditarCapitanCambiado = not self.inputEditarCapitanCambiado

    def obtenerJugadores(self):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerJugadores()


