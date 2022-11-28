from flet import Page

from Views.MenuEquipoView import MenuEquipoVista
from Models.MenuEquipoModel import MenuEquipoModel

from Models.Entidades.Jugadores import Jugador


class MenuEquipoControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.modelo = MenuEquipoModel(self.page.session.get("equipo"))
        #self.equipo = self.page.session.get("equipo")

    def iniciarVista(self):
        self.page.clean()
        self.vista = MenuEquipoVista(self.page)
        self.page.vertical_alignment = "start"
        self.page.add(self.vista)

    def obtenerJugadores(self):
        return self.modelo.getJugadores()

    def validarInsertarJugadorVacio(self, jug: {}):
        if jug.get("nombre") == "" or jug.get("numero") == "" or jug.get("posicion") == "":
            return True
        else:
            return False

    def validarEditarJugadorVacio(self, jug: {}, capitanCambiado: bool):
        if jug.get("nombre") == "" and jug.get("numero") == "" and jug.get("posicion") == "" and not capitanCambiado:
            return True
        else:
            return False

    def vaildarJugadoresIguales(self, jugadorEditado: {}, jugadorNoEditado: Jugador):
        if(jugadorEditado.get("nombre") == jugadorNoEditado.getNombre()
                and jugadorEditado.get("numero") == str(jugadorNoEditado.getNumero())
                and jugadorEditado.get("posicion") == jugadorNoEditado.getPosicion()
                and jugadorEditado.get("capitan") == jugadorNoEditado.isCapitan()):
            return True
        else:
            return False

    def construirJugadorEditado(self, jugadorEditado: {}, jugadorNoEditado: Jugador):
        if not jugadorEditado.get("numero") == "":
            jugadorNoEditado.setNumero(int(jugadorEditado.get("numero")))
        if not jugadorEditado.get("nombre") == "":
            jugadorNoEditado.setNombre(jugadorEditado.get("nombre"))
        if not jugadorEditado.get("posicion") == "":
            jugadorNoEditado.setPosicion(jugadorEditado.get("posicion"))
        if not jugadorEditado.get("capitan") == jugadorNoEditado.isCapitan():
            jugadorNoEditado.setCapitan(jugadorEditado.get("capitan"))

        return jugadorNoEditado

    def insertarJugador(self, jug: {}):
        return self.modelo.insertarJugador(jug)

    def editarJugador(self, jugador):
        self.modelo.editarJugador(jugador)

    def borrarJugador(self, jugador):
        self.modelo.borrarJugador(jugador)

    def regresar(self):
        self.page.session.remove("equipo")
        self.page.controls.pop()
        self.page.update()
        from Controllers.SeleccionarEquipoControl import SeleccionarEquipoControlador
        seleccionarEquipo = SeleccionarEquipoControlador(self.page)
        seleccionarEquipo.iniciarVista()
