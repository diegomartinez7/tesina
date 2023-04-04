from flet import *
from flet import Page, padding, colors, margin, icons
from flet.buttons import RoundedRectangleBorder


class RegistroVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.inputNombre = None
        self.inputApellido = None
        self.inputNombreUsuario = None
        self.inputPassword = None
        self.inputConfirmarPassword = None
        self.inputRolUsuario = None
        self.dialogResultados: AlertDialog = None

    def build(self):
        self.expand = True
        self.configurarDialog()
        return self.inicializarComponentes()

    def inicializarComponentes(self):
        tituloRegistrarse = Text(
            value="Registro de Usuario",
            color="#001f60",
            size=96,
            font_family="Nunito"
        )

        labelInputNombre = Text(
            value="Nombre",
            color="#001f60",
            size=20,
            font_family="Nunito"
        )
        labelInputApellido = Text(
            value="Apellido",
            color="#001f60",
            size=20,
            font_family="Nunito"
        )
        labelInputNombreUsuario = Text(
            value="Nombre de usuario",
            color="#001f60",
            size=20,
            font_family="Nunito"
        )
        labelInputRol = Text(
            value="Rol de usuario",
            color="#001f60",
            size=20,
            font_family="Nunito"
        )
        labelInputPassword = Text(
            value="Contraseña",
            color="#001f60",
            size=20,
            font_family="Nunito"
        )
        labelInputConfirmarPassword = Text(
            value="Confirmar contraseña",
            color="#001f60",
            size=20,
            font_family="Nunito"
        )

        self.inputNombre = TextField(
            color="#001f60",
            text_size=16,
            border_radius=12.5,
            width=300,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=15
        )
        self.inputApellido = TextField(
            color="#001f60",
            text_size=16,
            border_radius=12.5,
            width=300,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=15
        )
        self.inputNombreUsuario = TextField(
            color="#001f60",
            text_size=16,
            border_radius=12.5,
            width=300,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=15
        )
        self.inputPassword = TextField(
            password=True,
            can_reveal_password=True,
            color="#001f60",
            text_size=16,
            border_radius=12.5,
            width=300,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=15
        )
        self.inputConfirmarPassword = TextField(
            password=True,
            can_reveal_password=True,
            color="#001f60",
            text_size=16,
            border_radius=12.5,
            width=300,
            border_color=colors.WHITE,
            focused_border_color="#001f60",
            content_padding=15
        )
        self.inputRolUsuario = Dropdown(
            width=300,
            options=[
                dropdown.Option("Entrenador"),
                dropdown.Option("Auxiliar")
            ],
            border_radius=12.5,
            border_color=colors.WHITE,
            color="#001f60",
            focused_border_color="#001f60",
            text_size=16,
            content_padding=15
        )

        buttonRegistrarse = ElevatedButton(
            content=Text(
                value="Registrarse",
                size=24
            ),
            bgcolor="#001f60",
            color="#D9D9D9",
            width=200,
            style=ButtonStyle(
                shape=RoundedRectangleBorder(radius=12.5),
                padding=padding.symmetric(5, 0)
            ),
            on_click=self.clickRegistrarse
        )
        buttonRegresar = IconButton(
            icon=icons.KEYBOARD_RETURN_ROUNDED,
            icon_color="#001f60",
            icon_size=36,
            on_click=self.clickRegresar
        )

        containerInputNombre = Container(
            content=self.inputNombre,
            bgcolor=colors.WHITE,
            border_radius=12.5
        )
        containerInputApellido = Container(
            content=self.inputApellido,
            bgcolor=colors.WHITE,
            border_radius=12.5
        )
        containerInputNombreUsuario = Container(
            content=self.inputNombreUsuario,
            bgcolor=colors.WHITE,
            border_radius=12.5
        )
        containerInputRol = Container(
            content=self.inputRolUsuario,
            bgcolor=colors.WHITE,
            border_radius=12.5
        )
        containerPassword = Container(
            content=self.inputPassword,
            bgcolor=colors.WHITE,
            border_radius=12.5
        )
        containerConfirmarPassword = Container(
            content=self.inputConfirmarPassword,
            bgcolor=colors.WHITE,
            border_radius=12.5
        )
        containerButtonRegistrarse = Container(
            content=buttonRegistrarse,
            margin=margin.symmetric(30, 0)
        )

        columnNombre = Column(
            [
                labelInputNombre,
                containerInputNombre
            ],
            horizontal_alignment="center"
        )
        columnApellido = Column(
            [
                labelInputApellido,
                containerInputApellido
            ],
            horizontal_alignment="center"
        )
        columnNombreUsuario = Column(
            [
                labelInputNombreUsuario,
                containerInputNombreUsuario
            ],
            horizontal_alignment="center"
        )
        columnRolUsuario = Column(
            [
                labelInputRol,
                containerInputRol
            ],
            horizontal_alignment="center"
        )
        columnPassword = Column(
            [
                labelInputPassword,
                containerPassword
            ],
            horizontal_alignment="center"
        )
        columnConfirmarPassword = Column(
            [
                labelInputConfirmarPassword,
                containerConfirmarPassword
            ],
            horizontal_alignment="center"
        )

        rowNombres = Row(
            [
                columnNombre,
                columnApellido
            ],
            alignment="center",
            spacing=50
        )
        rowNombreUsuarioRol = Row(
            [
                columnNombreUsuario,
                columnRolUsuario
            ],
            alignment="center",
            spacing=50
        )
        rowPasswords = Row(
            [
                columnPassword,
                columnConfirmarPassword
            ],
            alignment="center",
            spacing=50
        )

        columnFormularioRegistro = Column(
            [
                rowNombres,
                rowNombreUsuarioRol,
                rowPasswords,
                containerButtonRegistrarse
            ],
            horizontal_alignment="center"
        )

        containerVistaRegistro = Container(
            content=Column(
                [
                    tituloRegistrarse,
                    columnFormularioRegistro,
                    buttonRegresar
                ],
                horizontal_alignment="center",
                alignment="spaceBetween"
            ),
            padding=50
        )

        return containerVistaRegistro

    def configurarDialog(self):
        self.dialogResultados = AlertDialog(
            modal=True,
            title=Text("Añadir Jugador", text_align="center", color="#001f60"),
            content=Text("Aquí va el contenido del dialog"),
            actions=[
                TextButton(content=Text("Aceptar", color="#00BC06")),
                TextButton(content=Text("Cancelar", color="#d50037"))
            ],
            actions_alignment="center"
        )
        self.pagina.dialog = self.dialogResultados

    def iniciarDialogError(self, msg):
        self.dialogResultados.title = Text("¡Error!", text_align="center", color="#d50037")
        self.dialogResultados.content = Text(msg, text_align="center", size=20)
        self.dialogResultados.actions = [
            TextButton(content=Text("Aceptar", color="#001f60"), on_click=self.cerrarDialog)
        ]

    def iniciarDialogExito(self, msg):
        self.dialogResultados.title = Icon(name=icons.DONE, color="#00BC06")
        self.dialogResultados.content = Text(msg, text_align="center", size=20)
        self.dialogResultados.actions = [
            TextButton(content=Text("Aceptar", color="#001f60"), on_click=self.cerrarDialog)
        ]

    def abrirErrorDialog(self, msg):
        self.iniciarDialogError(msg)
        self.dialogResultados.open = True
        self.pagina.update()

    def abrirDialogExito(self, msg):
        self.iniciarDialogExito(msg)
        self.dialogResultados.open = True
        self.pagina.update()

    def cerrarDialog(self, e):
        self.dialogResultados.open = False
        self.pagina.update()

    def clickRegistrarse(self, e):
        usuario = {
            "nombre": self.inputNombre.value,
            "apellido": self.inputApellido.value,
            "usuario": self.inputNombreUsuario.value,
            "rol": self.inputRolUsuario.value if self.inputRolUsuario.value is not None else "",
            "password": self.inputPassword.value
        }
        if not self.validarUsuarioVacio(usuario):
            if self.validarPasswords():
                from Controllers.RegistroControl import RegistroControlador
                controlador = RegistroControlador(self.pagina)
                controlador.registrarUsuario(usuario)
                self.abrirDialogExito("Usuario registrado con éxito")
                controlador.registrarse()
            else:
                self.abrirErrorDialog("Las contraseñas no son iguales")
        else:
            self.abrirErrorDialog("No puede haber campos vacíos")

    def clickRegresar(self, e):
        from Controllers.RegistroControl import RegistroControlador
        controlador = RegistroControlador(self.pagina)
        controlador.regresar()

    def validarUsuarioVacio(self, usuario: {}):
        from Controllers.RegistroControl import RegistroControlador
        controlador = RegistroControlador(self.pagina)
        return controlador.validarUsuarioVacio(usuario)

    def validarPasswords(self):
        password = self.inputPassword.value
        confirmacionPassword = self.inputConfirmarPassword.value
        from Controllers.RegistroControl import RegistroControlador
        controlador = RegistroControlador(self.pagina)
        return controlador.validarPasswords(password, confirmacionPassword)
