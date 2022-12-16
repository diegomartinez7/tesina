from Models.Entidades.Equipo import Equipo
from Models.Entidades.Jugadores.JugadorPropio import JugadorPropio
import requests


class RegistrarEquipoModel(object):
    def __init__(self):
        self.listaJugadoresTemporal = []
        self.url = "http://localhost:8080/equipo"
        self.urlJugador = "http://localhost:8080/jugadorPropio"

    def crearJugador(self, jug: {}):
        nombre = jug.get("nombre")
        genero = jug.get("genero")
        posicion = jug.get("posicion")
        numero = jug.get("numero")
        capitan = jug.get("capitan")

        nuevoJugador = JugadorPropio(nombre, genero, posicion, numero, capitan)

        return nuevoJugador

    def agregarJugador(self, jugador: {}):
        respuesta = requests.post(self.urlJugador, json=jugador)
        print(f"Jugador creado con resultado: {respuesta.text}")
        return self.crearJugadorRespuesta(respuesta.json())

    def insertarEquipo(self, equipo: {}):
        respuesta = requests.post(self.url, equipo)
        print(f"Equipo creado con resultado: {respuesta}")
        return self.crearEquipoRespuesta(respuesta.json())

    def crearEquipoRespuesta(self, respuesta: {}):
        id = respuesta.get("id")
        nombre = respuesta.get("nombre_equipo")
        entidad = respuesta.get("nombre_entidad")
        categoria = respuesta.get("categoria")
        tipo = respuesta.get("tipo_equipo")
        rama = respuesta.get("rama")
        contrario = respuesta.get("contrario")

        nuevoEquipo = Equipo(nombre, categoria, rama, tipo, entidad, contrario)
        nuevoEquipo.setId(id)
        return nuevoEquipo

    def crearJugadorRespuesta(self, respuesta: {}):
        id = respuesta.get("id")
        nombre = respuesta.get("nombre")
        capitan = respuesta.get("capitan")
        genero = respuesta.get("genero")
        posicion = respuesta.get("posicion")
        numero = respuesta.get("no_jugador")
        lesiones = respuesta.get("lesiones")
        titular = respuesta.get("titular")

        nuevoJugador = JugadorPropio(nombre, genero, posicion, numero, capitan)
        nuevoJugador.setId(id)
        nuevoJugador.setLesion(lesiones)
        nuevoJugador.setTitular(titular)

        return nuevoJugador

    def asociarUsuario(self, idUsuario, idEquipo):
        url = f"http://localhost:8080/usuario/{idUsuario}/equipo/{idEquipo}"
        respuesta = requests.put(url)
        print(f"Usuario asociado con resultado: {respuesta}")
        return respuesta

    def asociarJugador(self, idJugador, idEquipo):
        url = f"http://localhost:8080/equipo/{idEquipo}/jugadorPropio/{idJugador}"
        respuesta = requests.put(url)
        print(f"Jugador asociado con resultado: {respuesta}")
        return respuesta

