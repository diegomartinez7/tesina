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

        self.inputNombreCompetencia = None
        self.inputInicio = None
        self.inputFin = None
        self.inputTipo = None
        self.dialogEquipo: AlertDialog = None

    def build(self):
        self.expand = True
        self.configurarDialog()
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
            on_click=self.abrirDialogNuevaCompetencia
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
                                        data=competencia,
                                        on_click=self.abrirDialogEditarCompetencia
                                    ),
                                    IconButton(
                                        icon=icons.DELETE,
                                        icon_color="#d50037",
                                        tooltip="Borrar Competencia",
                                        data=competencia,
                                        on_click=self.abrirDialogBorrarCompetencia
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

    def iniciarDialogNuevaCompetencia(self):
        self.inputNombreCompetencia = TextField(text_size=14, content_padding=10, color="#001f60",
                                     expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     border_width=0)
        self.inputTipo = TextField(text_size=14, content_padding=10, color="#001f60",
                                     expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     border_width=0)
        self.inputInicio = TextField(text_size=14, content_padding=10, color="#001f60",
                                        expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                        border_width=0)
        self.inputFin = TextField(text_size=14, content_padding=10, color="#001f60",
                                     expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     border_width=0)

        self.dialogEquipo.title = Text("Añadir Competencia", text_align="center", color="#001f60")
        self.dialogEquipo.content = Column(
            controls=[
                Row(
                    controls=[
                        Text("Nombre", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Tipo", expand=1, text_align="center", color="#001f60", size=16),

                    ]
                ),
                Row(
                    controls=[
                        self.inputNombreCompetencia,
                        self.inputTipo,
                    ]
                ),
                Row(
                    controls=[
                        Text("Inicio", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Fin", expand=1, text_align="center", color="#001f60", size=16),
                    ]
                ),
                Row(
                    controls=[
                        self.inputInicio,
                        self.inputFin
                    ]
                )
            ],
            height=180,
            width=650
        )
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#00BC06"), on_click=self.aceptarInsertarCompetencia),
            TextButton(content=Text("Cancelar", color="#d50037"), on_click=self.cerrarDialog)
        ]

    def iniciarDialogEditarCompetencia(self, competencia):
        self.inputNombreCompetencia = TextField(text_size=14, content_padding=10, color="#001f60",
                                                expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                                border_width=0, hint_text=competencia.getNombre())
        self.inputTipo = TextField(text_size=14, content_padding=10, color="#001f60",
                                   expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                   border_width=0, hint_text=competencia.getTipo())
        self.inputInicio = TextField(text_size=14, content_padding=10, color="#001f60",
                                     expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                     border_width=0, hint_text=competencia.getInicio())
        self.inputFin = TextField(text_size=14, content_padding=10, color="#001f60",
                                  expand=1, border_radius=12.5, filled=True, bgcolor="#D9D9D9",
                                  border_width=0, hint_text=competencia.getFin())

        self.dialogEquipo.title = Text("Editar Equipo", text_align="center", color="#001f60")
        self.dialogEquipo.content = Column(
            controls=[
                Row(
                    controls=[
                        Text("Nombre", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Tipo", expand=1, text_align="center", color="#001f60", size=16),

                    ]
                ),
                Row(
                    controls=[
                        self.inputNombreCompetencia,
                        self.inputTipo,
                    ]
                ),
                Row(
                    controls=[
                        Text("Inicio", expand=1, text_align="center", color="#001f60", size=16),
                        Text("Fin", expand=1, text_align="center", color="#001f60", size=16)
                    ]
                ),
                Row(
                    controls=[
                        self.inputInicio,
                        self.inputFin
                    ]
                )
            ],
            height=180,
            width=650
        )
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#00BC06"), on_click=self.aceptarEditarCompetencia, data=competencia),
            TextButton(content=Text("Cancelar", color="#d50037"), on_click=self.cerrarDialog)
        ]

    def iniciarDialogBorrarCompetencia(self, competencia):
        self.dialogEquipo.title = Icon(name=icons.WARNING, color="#ffa400")
        self.dialogEquipo.content = Text(f"¿Deseas borrar a {competencia.getNombre()}?", text_align="center", size=20)
        self.dialogEquipo.actions = [
            TextButton(content=Text("Aceptar", color="#001f60"), on_click=self.aceptarBorrarCompetencia, data=competencia),
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

    def abrirDialogNuevaCompetencia(self, e):
        self.iniciarDialogNuevaCompetencia()
        self.dialogEquipo.open = True
        self.pagina.update()

    def abrirDialogEditarCompetencia(self, e):
        competencia = e.control.data
        self.iniciarDialogEditarCompetencia(competencia)
        self.dialogEquipo.open = True
        self.pagina.update()

    def abrirDialogBorrarCompetencia(self, e):
        competencia = e.control.data
        self.iniciarDialogBorrarCompetencia(competencia)
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

    def aceptarInsertarCompetencia(self, e):
        nombre = self.inputNombreCompetencia.value
        tipo = self.inputTipo.value
        inicio = self.inputInicio.value
        fin = self.inputFin.value

        competencia = {
            "nombre": nombre,
            "id_equipo": True,
            "fecha_inicio": inicio,
            "fecha_fin": fin,
            "id_tipo": tipo,
            "activa": True
        }

        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        if controlador.validarInsertarCompetenciaVacia(competencia):
            self.abrirErrorDialog("No se puede haber campos vacíos")
        else:
            self.dialogEquipo.open = False
            self.pagina.update()
            self.insertarCompetencia(competencia)

    def insertarCompetencia(self, competencia):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        if controlador.insertarCompetencia(competencia):
            self.abrirDialogExito("Competencia agregada con éxito")
            self.obtenerContenedoresCompetencias()
            self.update()
        else:
            self.abrirErrorDialog("No se pudo insertar la competencia \n Valide que los datos no sean iguales")

    def aceptarEditarCompetencia(self, e):
        competenciaNoEditada = e.control.data

        nombre = self.inputNombreCompetencia.value
        tipo = self.inputTipo.value
        inicio = self.inputInicio.value
        fin = self.inputFin.value

        competenciaEditada = {
            "nombre": nombre,
            "id_equipo": True,
            "fecha_inicio": inicio,
            "fecha_fin": fin,
            "id_tipo": tipo,
            "activa": True
        }

        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        if controlador.validarEditarCompetenciaVacia(competenciaEditada):
            self.abrirErrorDialog("No se ha cambiado nada la competencia")
        elif controlador.vaildarCompetenciasIguales(competenciaEditada, competenciaNoEditada):
            self.abrirErrorDialog("No se hizo ningún cambio")
        else:
            self.dialogEquipo.open = False
            self.pagina.update()
            competencia = controlador.construirCompetenciaEditada(competenciaEditada, competenciaNoEditada)
            self.editarCompetencia(competencia)

    def editarCompetencia(self, competencia):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        controlador.editarCompetencia(competencia)
        self.abrirDialogExito("Competencia editado con éxito")
        self.obtenerContenedoresCompetencias()
        self.update()

    def aceptarBorrarCompetencia(self, e):
        competencia = e.control.data
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        controlador.borrarCompetencia(competencia)
        self.abrirDialogExito("Competencia borrada con éxito")
        self.obtenerContenedoresCompetencias()
        self.update()

    def obtenerCompetencias(self):
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        controlador = MenuEquipoControlador(self.pagina)
        return controlador.obtenerCompetencias()
