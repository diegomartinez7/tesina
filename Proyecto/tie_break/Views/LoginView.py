from flet import *
from flet import colors, icons, margin, padding
from flet.buttons import RoundedRectangleBorder


class LoginVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.dialogInfo = AlertDialog(
            modal=True,
            title=Text("¡Hola!", color="#001f60", text_align="center"),
            content=Text(
                value="informacionSistema",
                color="#001f60"
            ),
            actions=[
                TextButton("Aceptar", on_click=self.cerrarDialog)
            ],
            actions_alignment="center",
            on_dismiss=self.cerrarDialog
        )
        self.inputUsuario = TextField(
            color="#001f60",
            text_size=16,
            border_radius=12.5,
            width=400,
            border_color=colors.WHITE,
            focused_border_color="#001f60"
        )
        self.inputPassword = TextField(
            password=True,
            can_reveal_password=True,
            color="#001f60",
            text_size=16,
            border_radius=12.5,
            width=400,
            border_color=colors.WHITE,
            focused_border_color="#001f60"
        )
        self.labelMensajeError = Text(
            value="Datos Inválidos",
            color="#d50037",
            size=16,
            font_family="Nunito",
            visible=False
        )

    def build(self):
        self.expand = True
        return self.inicializarComponentes()

    def inicializarComponentes(self):
        tituloSistema = Text(
            value="SSE Voley",
            color="#001f60",
            size=96,
            font_family="Nunito"
        )
        labelUsuario = Text(
            value="Usuario",
            color="#001f60",
            size=30,
            font_family="Nunito"
        )
        labelPassword = Text(
            value="Contraseña",
            color="#001f60",
            size=30,
            font_family="Nunito"
        )


        buttonIniciarSesion = ElevatedButton(
            content=Text(
                value="Iniciar Sesión",
                size=24
            ),
            bgcolor="#001f60",
            color="#D9D9D9",
            on_click=self.clickIniciarSesion,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5)
            )
        )
        buttonRegistrarse = TextButton(
            content=Text(
                value="Registrarse",
                size=18,
                color="#001f60"
            ),
            on_click=self.clickRegistro
        )
        buttonInfo = IconButton(
            icon=icons.INFO_OUTLINED,
            icon_color="#001f60",
            icon_size=36,
            on_click=self.clickInfo
        )

        containerLabelUsuario = Container(
            content=labelUsuario,
            margin=margin.only(0, 10, 0, 0),
        )

        containerInputUsuario = Container(
            content=self.inputUsuario,
            bgcolor=colors.WHITE,
            border_radius=12.5
        )

        containerLabelPassword = Container(
            content=labelPassword,
            margin=margin.only(0, 10, 0, 0)
        )

        containerinputPassword = Container(
            content=self.inputPassword,
            bgcolor=colors.WHITE,
            border_radius=12.5
        )

        containerLabelMensajeError = Container(
            content=self.labelMensajeError
        )

        containerButtonIniciarSesion = Container(
            content=buttonIniciarSesion,
            margin=margin.only(0, 20, 0, 0)
        )

        contanerButtonInfo = Container(
            content=buttonInfo,
            alignment=alignment.bottom_right,
        )

        columnElementosPrincipales = Column([
            containerLabelUsuario,
            containerInputUsuario,
            containerLabelPassword,
            containerinputPassword,
            containerLabelMensajeError,
            containerButtonIniciarSesion,
            buttonRegistrarse
        ], horizontal_alignment="center")

        containerLoginVista = Container(
            content= Column(
                controls=[
                    tituloSistema,
                    columnElementosPrincipales,
                    contanerButtonInfo
                ],
                horizontal_alignment="center",
                alignment="spaceBetween"
            ),
            padding=50
        )

        return containerLoginVista

    def clickInfo(self, e):
        informacionSistema = "Este sistema fue desarrollado por Sergio Ruvalcaba Lozano y Christopher Diego Martínez " \
                             "Bernal \ncomo proyecto integrador de los conocimientos adquiridos en la carrera de " \
                             "Ingeniería en Sistemas Computacionales.\n\n" \
                             "El objetivo del sistema es proveer a entrenadores de voleibol de herramietnas que " \
                             "faciliten la gestión de sus equipos \ny la recolección de información durante los " \
                             "juegos que estos disputen, para así tener información que permita tomar " \
                             "\nlas mejores decisiones."

        self.dialogInfo.content = Text(
            value=informacionSistema,
            color="#001f60",
            text_align="center"
        )
        self.pagina.dialog = self.dialogInfo
        self.dialogInfo.open = True
        self.pagina.update()

    def clickRegistro(self, e):
        from Controllers.LoginControl import LoginControlador
        controlador = LoginControlador(self.pagina)
        controlador.registrarse()

    def clickIniciarSesion(self, e):
        from Controllers.LoginControl import LoginControlador
        controlador = LoginControlador(self.pagina)

        if self.inputUsuario.value == "" or self.inputPassword.value == "":
            if self.inputUsuario.value == "":
                self.errorUsuario()
            if self.inputPassword.value == "":
                self.errorPassword()
            self.setMensajeError("¡Los datos no pueden estar vacíos!")
        else:
            if controlador.revisarCredenciales(self.inputUsuario.value, self.inputPassword.value):
                self.update()
                controlador.iniciarSesion()
            else:
                self.errorUsuario()
                self.errorPassword()
                self.setMensajeError("¡Datos de usuario incorrectos!")

    def errorUsuario(self):
        self.inputUsuario.border_color = colors.RED
        self.update()

    def errorPassword(self):
        self.inputPassword.border_color = colors.RED
        self.update()

    def setMensajeError(self, mensaje):
        self.labelMensajeError.value = mensaje
        self.labelMensajeError.visible = True
        self.update()

    def cerrarDialog(self, e):
        self.dialogInfo.open = False
        self.pagina.update()
