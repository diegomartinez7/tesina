from flet import *
from flet import UserControl, border, padding, colors
from flet.border import BorderSide


class CompetenciasYPartidosVista(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.pagina = page

    def build(self):
        self.expand = True
        return self.inicializarComponentes()

    def inicializarComponentes(self):
        encabezadoCompetencia = Text(
            value="Competencia",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=1,
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
        encabezadoActiva = Text(
            value="Activa",
            color="#001f60",
            size=16,
            font_family="Nunito",
            expand=1,
            text_align="start"
        )

        rowEncabezadoTablaCompetencias = Row(
            controls=[
                encabezadoCompetencia,
                encabezadoFechaInicio,
                encabezadoFechaFin,
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

        containerCompetenciasYPartidosVista = Container(
            content=Column(
                [
                    containerEncabezadoTablaCompetencias
                ],
                spacing=0,
                expand=True
            )
        )

        return containerCompetenciasYPartidosVista
