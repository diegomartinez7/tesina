from flet import *

from Models.RegistrarPartidoModel import RegistrarPartidoModel
from Views.RegistrarPartidoView import RegistrarPartidoVista


class RegistrarPartidoControlador(object):
    def __init__(self, page: Page):
        self.page = page
        self.modelo = RegistrarPartidoModel(self.page.session.get("equipo"), self.page.session.get("equipoContrario"))
        self.modelo.setPartido(self.page.session.get("partidoRegistrado"))
        self.vista = None

    def iniciarVista(self):
        self.page.clean()
        self.vista = RegistrarPartidoVista(self.page)
        self.page.vertical_alignment = "start"
        self.page.add(self.vista)
        #self.vista.iniciarPartido()

    def obtenerNombreEquipoPropio(self):
        return self.modelo.getNombreEquipoPropio()

    def obtenerJugadoresPropios(self):
        return self.modelo.getJugadoresPropios()

    def obtenerNombreEquipoContrario(self):
        return self.modelo.getNombreEquipoContrario()

    def obtenerJugadoresContrarios(self):
        return self.modelo.getJugadoresContrarios()

    def registrarAccion(self, comando: str, ladoPropio: str):
        print(self.modelo.getNombreEquipoContrario())

        traduccion = ""
        if comando[0] == ladoPropio:
            traduccion += f"{self.modelo.getNombreEquipoPropio()}: "
        else:
            traduccion += f"{self.modelo.getNombreEquipoContrario()}: "
        traduccion += comando[1:comando.index(":")]
        traduccion += f"{self.obtenerAccion(comando[comando.index(':') + 1: comando.index(':') + 2])} desde zona "
        traduccion += f"{comando[comando.index(':') + 2: comando.index('-')]}  hasta zona "
        traduccion += comando[comando.index("-") + 1: comando.index(".")]
        return traduccion

    def regresar(self):
        #self.page.session.remove("equipoContrario")
        self.page.controls.pop()
        self.page.update()
        from Controllers.MenuEquipoControl import MenuEquipoControlador
        menuEquipo = MenuEquipoControlador(self.page)
        menuEquipo.iniciarVista()

    def obtenerAccion(self, abreviatura: str):
        print(abreviatura)
        if abreviatura == "S":
            return " saca"
        if abreviatura == "P":
            return " da pase"
        if abreviatura == "A":
            return " acomoda"
        if abreviatura == "R":
            return " remata"
        if abreviatura == "B":
            return " bloquea"

    def agregarSet(self, set):
        self.modelo.agregarSet(set)
