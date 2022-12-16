from flet import *
from flet import colors, border, margin, padding, icons
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder


class RegistrarEquipoVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.listaTemporalJugadores = []
        self.jugadorEditar = None
        self.filasJugadores = []
        self.columnListaJugadores = None
        self.dialogEquipo: AlertDialog = None
        self.inputNumero = None
        self.inputNombre = None
        self.inputPosicion = None
        self.inputCapitan = None
        self.inputGenero = None
        self.inputEditarCapitanCambiado: bool = False
        self.inputNombreEquipo = None
        self.inputEntidad = None
        self.inputCategoria = None
        self.inputRama = None
        self.inputTipo = None

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
        tituloEncabezado = Text(
            value="Registrar Equipo",
            color="#D9D9D9",
            size=32,
            font_family="Nunito",
            text_align="center"
        )
        tituloInputs = Text(
            value="Nuevo Equipo",
            color="#001f60",
            size=28,
            font_family="Nunito",
            text_align="center"
        )
        encabezadoNumero = Text(
            value="No.",
            color="#001f60",
            size=18,
            font_family="Nunito",
            expand=1,
            text_align="center"
        )
        encabezadoJugador = Text(
            value="Jugador",
            color="#001f60",
            size=18,
            font_family="Nunito",
            expand=3,
            text_align="center"
        )
        encabezadoPosicion = Text(
            value="Posición",
            color="#001f60",
            size=18,
            font_family="Nunito",
            expand=2,
            text_align="center"
        )
        encabezadoGenero = Text(
            value="Género",
            color="#001f60",
            size=18,
            font_family="Nunito",
            expand=1,
            text_align="center"
        )
        labelNombre = Text(
            value="Nombre del Equipo",
            color="#001f60",
            size=18,
            font_family="Nunito",
            text_align="center"
        )
        labelEntidad = Text(
            value="Entidad que Representa",
            color="#001f60",
            size=18,
            font_family="Nunito",
            text_align="center"
        )
        labelCategoria = Text(
            value="Categoría",
            color="#001f60",
            size=18,
            font_family="Nunito",
            text_align="center"
        )
        labelRama = Text(
            value="Rama",
            color="#001f60",
            size=18,
            font_family="Nunito",
            text_align="center"
        )
        labelTipo = Text(
            value="Tipo de Equipo",
            color="#001f60",
            size=18,
            font_family="Nunito",
            text_align="center"
        )

        self.inputNombreEquipo = TextField(
            color="#001f60",
            text_size=14,
            border_radius=12.5,
            width=300,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=10
        )
        self.inputEntidad = TextField(
            color="#001f60",
            text_size=14,
            border_radius=12.5,
            width=300,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=10
        )
        self.inputCategoria = TextField(
            color="#001f60",
            text_size=14,
            border_radius=12.5,
            width=300,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=10
        )
        self.inputRama = TextField(
            color="#001f60",
            text_size=14,
            border_radius=12.5,
            width=300,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=10
        )
        self.inputTipo = TextField(
            color="#001f60",
            text_size=14,
            border_radius=12.5,
            width=300,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=10
        )

        buttonRegresar = IconButton(
            icon=icons.KEYBOARD_RETURN_ROUNDED,
            icon_color="#b3b3cc",
            icon_size=16,
            on_click=self.regresar
        )
        buttonRegistrarEquipo = ElevatedButton(
            content=Text(
                value="Registrar Equipo",
                size=22,
                color="#D9D9D9"
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            ),
            on_click=self.registrarEquipo
        )
        buttonRegistrarJugador = ElevatedButton(
            content=Text(
                value="Añadir Jugador",
                size=12,
                color="#D9D9D9"
            ),
            bgcolor="#001f60",
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5),
                padding=padding.symmetric(3, 10)
            ),
            on_click=self.abrirDialogNuevoJugador
        )

        containerTituloEncabezado = Container(
            content=tituloEncabezado,
            expand=True
        )

        rowEncabezadoVista = Row(
            controls=[
                Container(
                    content=buttonRegresar,
                ),
                containerTituloEncabezado,
                Container(
                )
            ],
            expand=True
        )

        containerEncabezadoVista = Container(
            content=rowEncabezadoVista,
            bgcolor="#001f60",
            padding=padding.symmetric(10, 25)
        )

        columnInputs = Column(
            controls=[
                tituloInputs,
                Column(
                    [
                        labelNombre,
                        Container(
                            content=self.inputNombreEquipo,
                            bgcolor=colors.WHITE,
                            border_radius=12.5
                        )
                    ],
                    horizontal_alignment="center"
                ),
                Column(
                    [
                        labelEntidad,
                        Container(
                            content=self.inputEntidad,
                            bgcolor=colors.WHITE,
                            border_radius=12.5
                        )
                    ],
                    horizontal_alignment="center"
                ),
                Column(
                    [
                        labelCategoria,
                        Container(
                            content=self.inputCategoria,
                            bgcolor=colors.WHITE,
                            border_radius=12.5
                        )
                    ],
                    horizontal_alignment="center"
                ),
                Column(
                    [
                        labelRama,
                        Container(
                            content=self.inputRama,
                            bgcolor=colors.WHITE,
                            border_radius=12.5
                        )
                    ],
                    horizontal_alignment="center"
                ),
                Column(
                    [
                        labelTipo,
                        Container(
                            content=self.inputTipo,
                            bgcolor=colors.WHITE,
                            border_radius=12.5
                        )
                    ],
                    horizontal_alignment="center"
                )
            ],
            alignment="spaceEvenly",
            expand=True,
            horizontal_alignment="center"
        )

        rowEncabezadoTablaJugadores = Row(
            controls=[
                encabezadoNumero,
                encabezadoJugador,
                encabezadoPosicion,
                encabezadoGenero,
                buttonRegistrarJugador
            ],
            expand=True
        )

        containerEncabezadoTablaJugadores = Container(
            content=rowEncabezadoTablaJugadores,
            alignment=alignment.center,
            border=border.only(bottom=BorderSide(2, "#001f60")),
            margin=margin.symmetric(0, 5),
            padding=padding.symmetric(5, 15)
        )
        containerButtonRegistrarEquipo = Container(
            content=buttonRegistrarEquipo,
            alignment=alignment.center_right,
            padding=10
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

        columnTablaJugadoresButtonRegistrarEquipo = Column(
            controls=[
                containerTablaJugadores,
                containerButtonRegistrarEquipo
            ],
        )

        containerColumnInputs = Container(
            content=columnInputs,
            padding=padding.symmetric(25, 0),
            expand=2
        )
        containerColumnTablaJugadoresButtonRegistrarEquipo = Container(
            content=columnTablaJugadoresButtonRegistrarEquipo,
            bgcolor=colors.WHITE,
            expand=4
        )

        rowInputsTablaJugadores = Row(
            controls=[
                containerColumnInputs,
                containerColumnTablaJugadoresButtonRegistrarEquipo
            ],
            expand=True,
            vertical_alignment="start",
            spacing=0
        )

        containerRegistrarEquipo = Container(
            content=Column(
                [
                    containerEncabezadoVista,
                    rowInputsTablaJugadores
                ],
                spacing=0
            )
        )

        return containerRegistrarEquipo

    def obtenerContenedoresJugadores(self):
        self.filasJugadores.clear()
        for jugador in self.listaTemporalJugadores:
            self.filasJugadores.append(
                Container(
                    content=Row(
                        controls=[
                            Text(
                                value=jugador.getNumero(),
                                size=14,
                                color="#001f60",
                                expand=1,
                                text_align="center"
                            ),
                            Row(
                                controls=[
                                    Text(
                                        value=f"{jugador.getNombre()}",
                                        size=14,
                                        color="#001f60",
                                        text_align="center"
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
                                vertical_alignment="center",
                                alignment="center"
                            ),
                            Text(
                                value=jugador.getPosicion(),
                                size=14,
                                color="#001f60",
                                expand=2,
                                text_align="center"
                            ),
                            Text(
                                value=jugador.getGenero(),
                                size=14,
                                color="#001f60",
                                expand=1,
                                text_align="center"
                            )
                            ,
                            Row(
                                controls=[
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
        self.inputGenero = Dropdown(options=[dropdown.Option("M"),dropdown.Option("F")],
            border_width=0, content_padding=10, filled=True, bgcolor="#D9D9D9", text_size=14, color="#001f60",
            counter_text="Hola", counter_style=TextStyle(size=0), border_radius=12.5, expand=1)
        self.inputCapitan = Switch()

        self.dialogEquipo.title = Text("Añadir Jugador", text_align="center", color="#001f60")
        self.dialogEquipo.content = Column(
            controls=[
                Row(
                    controls=[
                        Text("No.", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Nombre", expand=4, text_align="center", color="#001f60", size=16),
                        Text("Genero", text_align="center", color="#001f60", size=16),
                        Text("Posición", expand=3, text_align="center", color="#001f60", size=16),
                        Text("Capitán", text_align="center", color="#001f60", size=16)
                    ]
                ),
                Row(
                    controls=[
                        self.inputNumero,
                        self.inputNombre,
                        self.inputGenero,
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
        self.jugadorEditar = jugador
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
        numero = int(self.inputNumero.value) if self.inputNumero != "" else self.inputNumero
        nombre = self.inputNombre.value
        posicion = self.inputPosicion.value
        capitan = self.inputCapitan.value
        genero = self.inputGenero.value if self.inputGenero.value is not None else ""

        jugador = {
            "numero": numero,
            "nombre": nombre,
            "posicion": posicion,
            "capitan": capitan,
            "genero": genero
        }

        from Controllers.RegistrarEquipoControl import RegistrarEquipoControlador
        controlador = RegistrarEquipoControlador(self.pagina)
        if controlador.validarInsertarJugadorVacio(jugador):
            self.abrirErrorDialog("No se puede haber campos vacíos")
        else:
            self.dialogEquipo.open = False
            self.pagina.update()
            self.insertarJugador(jugador)

    def insertarJugador(self, jugador):
        from Controllers.RegistrarEquipoControl import RegistrarEquipoControlador
        controlador = RegistrarEquipoControlador(self.pagina)
        self.listaTemporalJugadores.append(controlador.crearJugador(jugador))
        self.abrirDialogExito("Jugador agregado con éxito")
        self.obtenerContenedoresJugadores()
        self.update()

    def aceptarEditarJugador(self, e):
        jugadorNoEditado = e.control.data

        numero = int(self.inputNumero.value) if self.inputNumero != "" else self.inputNumero
        nombre = self.inputNombre.value
        posicion = self.inputPosicion.value
        capitan = self.inputCapitan.value

        jugadorEditado = {
            "numero": numero,
            "nombre": nombre,
            "posicion": posicion,
            "capitan": capitan
        }

        from Controllers.RegistrarEquipoControl import RegistrarEquipoControlador
        controlador = RegistrarEquipoControlador(self.pagina)
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
        for i, jugadorBase in enumerate(self.listaTemporalJugadores):
            if(jugadorBase.getNombre() == self.jugadorEditar.getNombre()
                    and jugadorBase.getNumero() == self.jugadorEditar.getNumero()):
                self.listaTemporalJugadores[i] = jugador
        self.abrirDialogExito("Jugador editado con éxito")
        self.obtenerContenedoresJugadores()
        self.update()

    def aceptarBorrarJugador(self, e):
        jugadorBorrado = e.control.data
        for jugador in self.listaTemporalJugadores:
            if(jugador.getNombre() == jugadorBorrado.getNombre()
                    and jugador.getNumero() == jugadorBorrado.getNumero()):
                self.listaTemporalJugadores.remove(jugador)
        self.abrirDialogExito("Jugador borrado con éxito")
        self.obtenerContenedoresJugadores()
        self.update()

    def inputEditarCapitanChanged(self, e):
        self.inputEditarCapitanCambiado = not self.inputEditarCapitanCambiado

    def registrarEquipo(self, e):
        nombre = self.inputNombreEquipo.value
        categoria = self.inputCategoria.value
        rama = self.inputRama.value
        tipo = self.inputTipo.value
        entidad = self.inputEntidad.value
        jugadores = self.listaTemporalJugadores

        equipo = {
            "categoria": categoria,
            "contrario": False,
            "nombre_entidad": entidad,
            "nombre_equipo": nombre,
            "rama": rama,
            "tipo_equipo": tipo
        }

        from Controllers.RegistrarEquipoControl import RegistrarEquipoControlador
        controlador = RegistrarEquipoControlador(self.pagina)
        if not controlador.validarEquipoVacio(equipo):
            equipoRegistrado = controlador.insertarEquipo(equipo)
            if equipoRegistrado is not None:
                print("Equipo registrado con éxito")
                if controlador.asociarUsuario(equipoRegistrado):
                    self.agregarJugadores(jugadores, equipoRegistrado.getId())
                    self.abrirDialogExito("Equipo Registrado con Éxito")
                    controlador.regresar()
        else:
            self.abrirErrorDialog("No puede haber campos vacíos")

    def agregarJugadores(self, jugadores, idEquipo):
        from Controllers.RegistrarEquipoControl import RegistrarEquipoControlador
        controlador = RegistrarEquipoControlador(self.pagina)
        for jugador in jugadores:
            jugadorJSN = {
                "capitan": jugador.isCapitan(),
                "genero": jugador.getGenero(),
                "lesiones": False,
                "no_jugador": jugador.getNumero(),
                "nombre": jugador.getNombre(),
                "posicion": jugador.getPosicion(),
                "titular": False
            }
            jugadoreRegistrado = controlador.agregarJugador(jugadorJSN)
            if jugadoreRegistrado is not None:
                if controlador.asociarJugador(jugadoreRegistrado.getId(), idEquipo):
                    print(f"Jugador {jugadoreRegistrado.getNombre()} registrado con éxito")

    def regresar(self, e):
        from Controllers.RegistrarEquipoControl import RegistrarEquipoControlador
        controlador = RegistrarEquipoControlador(self.pagina)
        controlador.regresar()
