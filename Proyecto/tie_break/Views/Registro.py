from flet import *
from flet import Page, padding, colors, margin, icons
from flet.buttons import RoundedRectangleBorder

from Views import Login


def registro(page: Page):
    prepararPagina(page)
    inicializarComponentes(page)


def prepararPagina(page: Page):
    page.clean()
    page.horizontal_alignment = "center"
    page.vertical_alignment = "spaceBetween"
    page.padding = padding.all(50)


def inicializarComponentes(page: Page):
    # TODO cambiar esta función para mandar los datos a backend
    def registrarse(e):
        Login.login(page)

    def regresar(e):
        Login.login(page)

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

    inputNombre = TextField(
        color="#001f60",
        text_size=16,
        border_radius=12.5,
        width=300,
        border_color=colors.WHITE,
        focused_border_color="#001f60",
        content_padding=15
    )
    inputApellido = TextField(
        color="#001f60",
        text_size=16,
        border_radius=12.5,
        width=300,
        border_color=colors.WHITE,
        focused_border_color="#001f60",
        content_padding=15
    )
    inputNombreUsuario = TextField(
        color="#001f60",
        text_size=16,
        border_radius=12.5,
        width=300,
        border_color=colors.WHITE,
        focused_border_color="#001f60",
        content_padding=15
    )
    inputPassword = TextField(
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
    inputConfirmarPassword = TextField(
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
    inputRolUsuario = Dropdown(
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
        on_click=registrarse
    )
    buttonRegresar = IconButton(
        icon=icons.KEYBOARD_RETURN_ROUNDED,
        icon_color="#001f60",
        icon_size=36,
        on_click=regresar
    )

    containerInputNombre = Container(
        content=inputNombre,
        bgcolor=colors.WHITE,
        border_radius=12.5
    )
    containerInputApellido = Container(
        content=inputApellido,
        bgcolor=colors.WHITE,
        border_radius=12.5
    )
    containerInputNombreUsuario = Container(
        content=inputNombreUsuario,
        bgcolor=colors.WHITE,
        border_radius=12.5
    )
    containerInputRol = Container(
        content=inputRolUsuario,
        bgcolor=colors.WHITE,
        border_radius=12.5
    )
    containerPassword = Container(
        content=inputPassword,
        bgcolor=colors.WHITE,
        border_radius=12.5
    )
    containerConfirmarPassword = Container(
        content=inputConfirmarPassword,
        bgcolor=colors.WHITE,
        border_radius=12.5
    )
    containerButtonRegistrarse = Container(
        content=buttonRegistrarse,
        margin=margin.symmetric(30,0)
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

    page.add(tituloRegistrarse, columnFormularioRegistro, buttonRegresar)