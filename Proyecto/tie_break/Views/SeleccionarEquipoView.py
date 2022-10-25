from flet import *
from flet import UserControl, Page, colors, padding, border, margin, icons
from flet.border import BorderSide
from flet.buttons import RoundedRectangleBorder


class SeleccionarEquipoVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page
        self.listaEquipos = [
            {
                "nombre": "Gallos UAA",
                "jugadores": [
                    {
                        "nombre": "Sergio Ruvalcaba Lozano",
                        "numero": 4,
                        "capitan": True,
                        "posicion": "Acomodador"
                    },
                    {
                        "nombre": "Iván Alejandro Luna Hermosillo",
                        "numero": 1,
                        "capitan": False,
                        "posicion": "Libero"
                    },
                    {
                        "nombre": "Eduardo Velazco",
                        "numero": 6,
                        "capitan": False,
                        "posicion": "Banda"
                    }
                ]
            },
            {
                "nombre": "Aguilas Reales UPA",
                "jugadores": [
                    {
                        "nombre": "Benjamín Esqueda Medrano",
                        "numero": 10,
                        "capitan": True,
                        "posicion": "Banda"
                    },
                    {
                        "nombre": "Daichi Guerrero",
                        "numero": 5,
                        "capitan": False,
                        "posicion": "Acomodador"
                    }
                ]
            }
        ]
        # self.equipoSeleccionado = {
        #     "nombre": None,
        #     "jugadores": [{
        #         "nombre": None,
        #         "numero": None,
        #         "capitan": None,
        #         "posicion": None
        #     }]
        # }
        self.equipoSeleccionado = self.listaEquipos[0]
        self.nombreEquipo = self.equipoSeleccionado.get("nombre")
        self.tituloNombreEquipo = Text(
            value=f"{self.nombreEquipo}",
            color="#D9D9D9",
            size=32,
            font_family="Nunito"
        )
        self.filasJugadores = []
        self.obtenerContenedoresJugadores()
        self.columnListaJugadores = Column(
            controls=self.filasJugadores,
            scroll="auto",
            expand=True
        )

    def build(self):
        self.expand = True
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

        rowEquipoYBusqueda = Row(
            controls=[
                containerTituloNombreEquipo,
                containerInputBuscarJugador
            ],
            expand=3,
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
            expand=3
        )

        rowListaEquiposTablaJugadores = Row(
            controls=[
                containerColumnListaDeEquipos,
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
                        value=equipo.get("nombre"),
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
        equipoClickeado = {
            "nombre": e.control.content.value,
            "jugadores": self.obtenerJugadores(e.control.content.value)
        }

        if not self.equipoSeleccionado:
            self.equipoSeleccionado = equipoClickeado
        elif not self.equipoSeleccionado.get("nombre") == equipoClickeado.get("nombre"):
            self.equipoSeleccionado = equipoClickeado

        self.tituloNombreEquipo.value = self.equipoSeleccionado.get("nombre")
        self.obtenerContenedoresJugadores()
        self.update()

    def obtenerContenedoresJugadores(self):
        self.filasJugadores.clear()
        for jugador in self.equipoSeleccionado.get("jugadores"):
            self.filasJugadores.append(
                Container(
                    content=Row(
                        controls=[
                            Text(
                                value=jugador.get("numero"),
                                size=20,
                                color="#001f60",
                                expand=1,
                                text_align="center"
                            ),
                            Text(
                                value=f"{jugador.get('nombre')} {' C' if jugador.get('capitan') else ''}",
                                size=20,
                                color="#001f60",
                                expand=3,
                                text_align="center"
                            ),
                            Text(
                                value=jugador.get("posicion"),
                                size=20,
                                color="#001f60",
                                expand=2,
                                text_align="center"
                            ),
                            Row(
                                controls=[
                                    IconButton(
                                        icon=icons.EDIT_NOTE,
                                        icon_color="#ffa400"
                                    ),
                                    IconButton(
                                        icon=icons.DELETE,
                                        icon_color="#d50037"
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

    def obtenerJugadores(self, nombreSeleccionado):
        jugadores = []

        for equipo in self.listaEquipos:
            if equipo.get("nombre") == nombreSeleccionado:
                jugadores = equipo.get("jugadores")

        return jugadores
