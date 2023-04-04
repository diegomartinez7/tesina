from flet import *

from Models.RegistrarEquipoModel import RegistrarEquipoModel
from Views.RegistrarEquipoView import RegistrarEquipoVista

from Models.Entidades.Jugadores import Jugador
from Models.Entidades.Equipo import Equipo


class RegistrarEquipoControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.vista = None
        self.modelo = RegistrarEquipoModel()
        self.usuario = self.page.session.get("usuario")

    def iniciarVista(self):
        self.vista = RegistrarEquipoVista(self.page)
        self.page.vertical_alignment = "center"
        self.page.add(self.vista)

    def validarInsertarJugadorVacio(self, jug: {}):
        if jug.get("nombre") == "" or jug.get("numero") == "" or jug.get("posicion") == "" or jug.get("genero") == "":
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

    def validarEquipoVacio(self, equipo: {}):
        if(equipo.get("categoria") == "" or equipo.get("nombre_entidad") == "" or equipo.get("nombre_equipo") == ""
                or equipo.get("rama") == "" or equipo.get("tipo_equipo") == ""):
            return True
        else:
            return False

    def crearJugador(self, jug: {}):
        nuevoJugador = self.modelo.crearJugador(jug)
        return nuevoJugador

    def insertarEquipo(self, equipo: {}):
        return self.modelo.insertarEquipo(equipo)

    def asociarUsuario(self, equipo: Equipo):
        return self.modelo.asociarUsuario(self.usuario.getId(), equipo.getId())

    def agregarJugador(self, jugador: {}):
        return self.modelo.agregarJugador(jugador)

    def asociarJugador(self, idJugador, idEquipo):
        return self.modelo.asociarJugador(idJugador, idEquipo)

    def regresar(self):
        self.limpiarVista()
        from Controllers.MenuSeleccionOCreacionControl import MenuSeleccionOCreacionControlador
        menu = MenuSeleccionOCreacionControlador(self.page)
        menu.iniciarVista()

    def limpiarVista(self):
        self.page.controls.pop()
        self.page.update()
