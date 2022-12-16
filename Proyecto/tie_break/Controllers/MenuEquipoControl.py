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

    def obtenerCompetencias(self):
        return self.modelo.getCompetencias()

    def obtenerPruebas(self):
        return self.modelo.getPruebas()

    def obtenerRivales(self):
        return self.modelo.getRivales()

    def obtenerJugadoresContrarios(self, equipo):
        return self.modelo.getJugadoresContrarios(equipo)

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

    def validarInsertarRivalVacio(self, rival: {}):
        if(rival.get("nombre_equipo") == "" or rival.get("categoria") == "" or rival.get("nombre_entidad") == ""
                or rival.get("rama") == "" or rival.get("tipo_equipo") == ""):
            return True
        else:
            return False

    def validarEditarRivalVacio(self, rival: {}):
        if (rival.get("nombre_equipo") == "" and rival.get("categoria") == "" and rival.get("nombre_entidad") == ""
                and rival.get("rama") == "" and rival.get("tipo_equipo") == ""):
            return True
        else:
            return False

    def vaildarRivalesIguales(self, rivalEditado: {}, rivalNoEditado):
        if(rivalEditado.get("nombre_equipo") == rivalNoEditado.getNombre()
                and rivalEditado.get("categoria") == rivalNoEditado.getCategoria()
                and rivalEditado.get("nombre_entidad") == rivalNoEditado.getEntidadRepresentada()
                and rivalEditado.get("rama") == rivalNoEditado.getRama()
                and rivalEditado.get("tipo_equipo") == rivalNoEditado.getTipoEquipo()):
            return True
        else:
            return False

    def construirRivalEditado(self, rivalEditado: {}, rivalNoEditado: Jugador):
        if not rivalEditado.get("nombre_equipo") == "":
            rivalNoEditado.setNombre(rivalEditado.get("nombre_equipo"))
        if not rivalEditado.get("categoria") == "":
            rivalNoEditado.setCategoria(rivalEditado.get("categoria"))
        if not rivalEditado.get("nombre_entidad") == "":
            rivalNoEditado.setEntidadRepresentada(rivalEditado.get("nombre_entidad"))
        if not rivalEditado.get("rama") == "":
            rivalNoEditado.setRama(rivalEditado.get("rama"))
        if not rivalEditado.get("tipo_equipo") == "":
            rivalNoEditado.setTipoEquipo(rivalEditado.get("tipo_equipo"))

        return rivalNoEditado

    def insertarRival(self, rival: {}):
        return self.modelo.insertarRival(rival)

    def editarRival(self, rival):
        self.modelo.editarRival(rival)

    def borrarRival(self, rival):
        self.modelo.borrarRival(rival)

    def validarInsertarCompetenciaVacia(self, competencia: {}):
        if(competencia.get("nombre") == "" or competencia.get("fecha_inicio") == ""
                or competencia.get("fecha_fin") == "" or competencia.get("id_tipo") == ""):
            return True
        else:
            return False

    def validarEditarCompetenciaVacia(self, competencia: {}):
        if (competencia.get("nombre") == "" and competencia.get("fecha_inicio") == ""
                and competencia.get("fecha_fin") == "" and competencia.get("id_tipo") == ""):
            return True
        else:
            return False

    def vaildarCompetenciasIguales(self, comptenenciaEditada: {}, competenciaNoEditada):
        if(comptenenciaEditada.get("nombre") == competenciaNoEditada.getNombre()
                and comptenenciaEditada.get("fecha_inicio") == competenciaNoEditada.getInicio()
                and comptenenciaEditada.get("fecha_fin") == competenciaNoEditada.getFin()
                and comptenenciaEditada.get("id_tipo") == competenciaNoEditada.getTipo()):
            return True
        else:
            return False

    def construirCompetenciaEditada(self, comptetenciaEditada: {}, competeciaNoEditada: Jugador):
        if not comptetenciaEditada.get("nombre") == "":
            competeciaNoEditada.setNombre(comptetenciaEditada.get("nombre"))
        if not comptetenciaEditada.get("fecha_inicio") == "":
            competeciaNoEditada.setInicio(comptetenciaEditada.get("fecha_inicio"))
        if not comptetenciaEditada.get("fecha_fin") == "":
            competeciaNoEditada.setFin(comptetenciaEditada.get("fecha_fin"))
        if not comptetenciaEditada.get("id_tipo") == "":
            competeciaNoEditada.setTipo(comptetenciaEditada.get("id_tipo"))

        return competeciaNoEditada

    def insertarCompetencia(self, competencia: {}):
        return self.modelo.insertarCompetencia(competencia)

    def editarCompetencia(self, competencia):
        self.modelo.editarCompetencia(competencia)

    def borrarCompetencia(self, competencia):
        self.modelo.borrarCompetencia(competencia)

    def registrarPartido(self, equipo):
        equipoContrario = equipo
        self.page.session.set("equipoContrario", equipoContrario)
        self.page.controls.pop()
        self.page.update()
        from Controllers.RegistrarPartidoControl import RegistrarPartidoControlador
        registrarPartido = RegistrarPartidoControlador(self.page)
        registrarPartido.iniciarVista()

    def regresar(self):
        self.page.session.remove("equipo")
        self.page.controls.pop()
        self.page.update()
        from Controllers.SeleccionarEquipoControl import SeleccionarEquipoControlador
        seleccionarEquipo = SeleccionarEquipoControlador(self.page)
        seleccionarEquipo.iniciarVista()
