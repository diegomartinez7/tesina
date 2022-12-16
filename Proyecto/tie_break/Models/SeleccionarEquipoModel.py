from Models.Entidades.Equipo import Equipo
from Models.Entidades.Jugadores.JugadorContrario import JugadorContrario
from Models.Entidades.Jugadores.JugadorPropio import JugadorPropio
from Models.Entidades.Usuario import Usuario
from Models.Entidades.Jugadores.Jugador import Jugador

import requests


class SeleccionarEquipoModel(object):
    def __init__(self):
        self.equipo: Equipo = None
        self.jugadores: [Jugador] = []
        self.entrenador: Usuario = None

    def setEquipoSeleccionado(self, equipo: Equipo):
        self.equipo = equipo
        self.jugadores = self.equipo.getJugadores()

    def getEquipos(self, idUsuario):
        #return Equipo.getEquipos()
        url = f"http://localhost:8080/usuario/{idUsuario}/equipos"
        respuesta = requests.get(url)
        print(respuesta.json())
        listaEquiposJsn = respuesta.json()
        listaEquipos = []

        for equipo in listaEquiposJsn:
            nuevoEquipo = Equipo(
                equipo.get("nombre_equipo"),
                equipo.get("categoria"),
                equipo.get("rama"),
                equipo.get("tipo_equipo"),
                equipo.get("nombre_entidad"),
                equipo.get("contrario")
            )
            nuevoEquipo.setId(equipo.get("id"))
            jugadoresJsn = equipo.get("jugadoresPropio")
            jugadores = self.construirJugadores(jugadoresJsn, False)
            nuevoEquipo.setJugadores(jugadores)
            listaEquipos.append(nuevoEquipo)

        return listaEquipos

    def editarJugador(self, jugador):
        id = jugador.getId()
        url = f"http://localhost:8080/jugadorPropio/{id}"
        jugadorEditar = {
            "capitan": jugador.isCapitan(),
            "genero": jugador.getGenero(),
            "lesiones": False,
            "no_jugador": jugador.getNumero(),
            "nombre": jugador.getNombre(),
            "posicion": jugador.getPosicion(),
            "titular": False
        }

        respuesta = requests.put(url, json=jugadorEditar)
        print(respuesta.status_code)
        if respuesta.status_code == 200:
            return self.construirJugadorRespuesta(respuesta.json(), id)
        else:
            return None

    def borrarJugador(self, jugador):
        id = jugador.getId()
        url = f"http://localhost:8080/jugadorPropio/{id}"
        respuesta = requests.delete(url)
        print(respuesta)
        if respuesta.status_code == 200:
            return True
        else:
            return False

    def construirJugadores(self, jugadores, contrarios):
        listaJugadores = []
        for jugador in jugadores:
            if not contrarios:
                nuevoJugador = JugadorPropio(
                    jugador.get("nombre"),
                    jugador.get("genero"),
                    jugador.get("posicion"),
                    jugador.get("no_jugador"),
                    jugador.get("capitan")
                )
                nuevoJugador.setLesion(jugador.get("lesiones"))
                nuevoJugador.setTitular(jugador.get("titular"))
            else:
                nuevoJugador = JugadorContrario(
                    jugador.get("nombre"),
                    jugador.get("genero"),
                    jugador.get("posicion"),
                    jugador.get("no_jugador"),
                    jugador.get("capitan")
                )
            nuevoJugador.setId(jugador.get("id"))

            listaJugadores.append(nuevoJugador)

        return listaJugadores

    def construirJugadorRespuesta(self, jugador: {}, id):
        nombre = jugador.get("nombre")
        capitan = jugador.get("capitan")
        genero = jugador.get("genero")
        posicion = jugador.get("posicion")
        numero = jugador.get("no_jugador")
        lesiones = jugador.get("lesiones")
        titular = jugador.get("titular")

        jugadorEditado = JugadorPropio(nombre, genero, posicion, numero, capitan)
        jugadorEditado.setId(id)
        jugadorEditado.setLesion(lesiones)
        jugadorEditado.setTitular(titular)

        return jugadorEditado

    @classmethod
    def getJugadores(cls, equipo):
        return Equipo.getJugadoresEquipo(equipo)
