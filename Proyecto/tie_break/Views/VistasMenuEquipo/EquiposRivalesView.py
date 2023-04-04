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

        self.inputNombreEquipo = None
        self.inputEntidad = None
        self.inputCategoria = None
        self.inputRama = None
        self.inputTipo = None
        self.dialogEquipo: AlertDialog = None

    def build(self):
        self.expand = True
        self.configurarDialog()
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
            on_click=self.abrirDialogNuevoRival
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
            bgcolor=colors.WHITE
            #bgcolor="#ffa400"
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
                                            on_click=self.abrirDialogEditarEquipo,
                                            data=rival
                                        ),
                                        IconButton(
                                            icon=icons.DELETE,
                                            icon_color="#d50037",
                                            tooltip="Borrar Equipo",
                                            on_click=self.abrirDialogBorrarEquipo,
                                            data=rival
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

    def configurarDialog(self):
        self.dialogEquipo = AlertDialog(
            modal=True,
            title=Text("Añadir Rival", text_align="center", color="#001f60"),
            content=Text("Aquí va el contenido del dialog"),
            actions=[
                TextButton(content=Text("Aceptar", color="#00BC06")),
                TextButton(content=Text("Cancelar", color="#d50037"))
            ],
            actions_alignment="center"
        )
        self.pagina.dialog = self.dialogEquipo

    def iniciarDialogNuevoRival(self):
        self.inputNombreEquipo = TextField(text_size=14, content_padding=10, color="#001f60",
                                     expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     border_width=0)
        self.inputEntidad = TextField(text_size=14, content_padding=10, color="#001f60",
                                     expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     border_width=0)
        self.inputCategoria = TextField(text_size=14, content_padding=10, color="#001f60",
                                        expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                        border_width=0)
        self.inputRama = TextField(text_size=14, content_padding=10, color="#001f60",
                                     expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     border_width=0)
        self.inputTipo = TextField(text_size=14, content_padding=10, color="#001f60",
                                     expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     border_width=0)

        self.dialogEquipo.title = Text("Añadir Equipo Rival", text_align="center", color="#001f60")
        self.dialogEquipo.content = Column(
            controls=[
                Row(
                    controls=[
                        Text("Nombre", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Entidad", expand=1, text_align="center", color="#001f60", size=16),

                    ]
                ),
                Row(
                    controls=[
                        self.inputNombreEquipo,
                        self.inputEntidad,
                    ]
                ),
                Row(
                    controls=[
                        Text("Categoría", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Rama", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Tipo", expand=1, text_align="center", color="#001f60", size=16),
                    ]
                ),
                Row(
                    controls=[
                        self.inputCategoria,
                        self.inputRama,
                        self.inputTipo
                    ]
                )
            ],
            height=180,
            width=650
        )
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#00BC06"), on_click=self.aceptarInsertarRival),
            TextButton(content=Text("Cancelar", color="#d50037"), on_click=self.cerrarDialog)
        ]

    def iniciarDialogEditarEquipo(self, equipo):
        self.inputNombreEquipo = TextField(text_size=14, content_padding=10, color="#001f60",
                                           expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                           border_width=0, hint_text=equipo.getNombre())
        self.inputEntidad = TextField(text_size=14, content_padding=10, color="#001f60",
                                      expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                      border_width=0, hint_text=equipo.getEntidadRepresentada())
        self.inputCategoria = TextField(text_size=14, content_padding=10, color="#001f60",
                                        expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                        border_width=0, hint_text=equipo.getCategoria())
        self.inputRama = TextField(text_size=14, content_padding=10, color="#001f60",
                                   expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                   border_width=0, hint_text=equipo.getRama())
        self.inputTipo = TextField(text_size=14, content_padding=10, color="#001f60",
                                   expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                   border_width=0, hint_text=equipo.getTipoEquipo())

        self.dialogEquipo.title = Text("Editar Equipo", text_align="center", color="#001f60")
        self.dialogEquipo.content = Column(
            controls=[
                Row(
                    controls=[
                        Text("Nombre", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Entidad", expand=1, text_align="center", color="#001f60", size=16),

                    ]
                ),
                Row(
                    controls=[
                        self.inputNombreEquipo,
                        self.inputEntidad,
                    ]
                ),
                Row(
                    controls=[
                        Text("Categoría", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Rama", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Tipo", expand=1, text_align="center", color="#001f60", size=16),
                    ]
                ),
                Row(
                    controls=[
                        self.inputCategoria,
                        self.inputRama,
                        self.inputTipo
                    ]
                )
            ],
            height=180,
            width=650
        )
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#00BC06"), on_click=self.aceptarEditarRival, data=equipo),
            TextButton(content=Text("Cancelar", color="#d50037"), on_click=self.cerrarDialog)
        ]

    def iniciarDialogBorrarEquipo(self, equipo):
        self.dialogEquipo.title = Icon(name=icons.WARNING, color="#ffa400")
        self.dialogEquipo.content = Text(f"¿Deseas borrar a {equipo.getNombre()}?", text_align="center", size=20)
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#001f60"), on_click=self.aceptarBorrarRival, data=equipo),
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

    def abrirDialogNuevoRival(self, e):
        self.iniciarDialogNuevoRival()
        self.dialogEquipo.open = True
        self.pagina.update()

    def abrirDialogEditarEquipo(self, e):
        equipo = e.control.data
        self.iniciarDialogEditarEquipo(equipo)
        self.dialogEquipo.open = True
        self.pagina.update()

    def abrirDialogBorrarEquipo(self, e):
        equipo = e.control.data
        self.iniciarDialogBorrarEquipo(equipo)
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

    def aceptarInsertarRival(self, e):
        nombre = self.inputNombreEquipo.value
        entidad = self.inputEntidad.value
        categoria = self.inputCategoria.value
        rama = self.inputRama.value
        tipo = self.inputTipo.value

        equipo = {
            "categoria": categoria,
            "contrario": True,
            "nombre_entidad": entidad,
            "nombre_equipo": nombre,
            "rama": rama,
            "tipo_equipo": tipo
        }

        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        if controlador.validarInsertarRivalVacio(equipo):
            self.abrirErrorDialog("No se puede haber campos vacíos")
        else:
            self.dialogEquipo.open = False
            self.pagina.update()
            self.insertarRival(equipo)

    def insertarRival(self, equipo):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        if controlador.insertarRival(equipo):
            self.abrirDialogExito("Rival agregado con éxito")
            self.obtenerContenedoresRivales()
            self.update()
        else:
            self.abrirErrorDialog("No se pudo insertar el rival \n Valide que los datos no sean iguales")

    def aceptarEditarRival(self, e):
        equipoNoEditado = e.control.data

        nombre = self.inputNombreEquipo.value
        entidad = self.inputEntidad.value
        categoria = self.inputCategoria.value
        rama = self.inputRama.value
        tipo = self.inputTipo.value

        equipoEditado = {
            "categoria": categoria,
            "contrario": True,
            "nombre_entidad": entidad,
            "nombre_equipo": nombre,
            "rama": rama,
            "tipo_equipo": tipo
        }

        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        if controlador.validarEditarRivalVacio(equipoEditado):
            self.abrirErrorDialog("No se ha cambiado nada del rival")
        elif controlador.vaildarRivalesIguales(equipoEditado, equipoNoEditado):
            self.abrirErrorDialog("No se hizo ningún cambio")
        else:
            self.dialogEquipo.open = False
            self.pagina.update()
            rivalEditado = controlador.construirRivalEditado(equipoEditado, equipoNoEditado)
            self.editarRival(rivalEditado)

    def editarRival(self, rival):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        controlador.editarRival(rival)
        self.abrirDialogExito("Rival editado con éxito")
        self.obtenerContenedoresRivales()
        self.update()

    def aceptarBorrarRival(self, e):
        rivalBorrado = e.control.data
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        controlador.borrarRival(rivalBorrado)
        self.abrirDialogExito("Rival borrado con éxito")
        self.obtenerContenedoresRivales()
        self.update()

    def obtenerRivales(self):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerRivales()

