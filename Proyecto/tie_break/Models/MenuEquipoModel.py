from Models.Entidades.Equipo import Equipo
from Models.Entidades.Jugadores.Jugador import Jugador
from Models.Entidades.Competencia import Competencia
from Models.Entidades.Jugadores.JugadorPropio import JugadorPropio
from Models.Entidades.Partido import Partido
import requests


class MenuEquipoModel(object):
    def __init__(self, equipo: Equipo):
        self.equipo: Equipo = equipo
        self.jugadores = self.equipo.getJugadores()

    def getJugadores(self):
        return self.jugadores

    def insertarJugador(self, jugador: {}):
        id = self.equipo.obtenerUltimoIdJugador()
        nombre = jugador.get("nombre")
        genero = self.equipo.obtenerGeneroEquipo()
        posicion = jugador.get("posicion")
        numero = int(jugador.get("no_jugador"))
        capitan = jugador.get("capitan")

        nuevoJugador = Jugador(nombre, genero, posicion, numero, capitan)

        if self.equipo.checarJugadorRepetido(nuevoJugador):
            return 0
        else:
            url = "http://localhost:3000/api/jugadores"

            jugadorJSN = {
                "capitan": jugador.get("capitan"),
                "genero": self.equipo.obtenerGeneroEquipo(),
                "lesiones": False,
                "no_jugador": int(jugador.get("no_jugador")),
                "nombre": jugador.get("nombre"),
                "posicion": jugador.get("posicion"),
                "titular": False
            }

            respuesta = requests.post(url, json=jugadorJSN)
            print(f"Jugador creado con resultado: {respuesta.text}")

            if respuesta.status_code == 200:
                return respuesta.json().get("id")
            else:
                return 0

    def asociarJugador(self, idJugador: int):
        idEquipo = self.equipo.getId()
        url = f"http://localhost:3000/api/equipos/{idEquipo}/jugadorPropio/{idJugador}"
        respuesta = requests.put(url)
        print(f"Jugador asociado con resultado: {respuesta}")
        return respuesta

    # def crearJugadorRespuesta(self, respuesta: {}):
    #     id = respuesta.get("id")
    #     nombre = respuesta.get("nombre")
    #     capitan = respuesta.get("capitan")
    #     genero = respuesta.get("genero")
    #     posicion = respuesta.get("posicion")
    #     numero = respuesta.get("no_jugador")
    #     lesiones = respuesta.get("lesiones")
    #     titular = respuesta.get("titular")
    #
    #     nuevoJugador = JugadorPropio(nombre, genero, posicion, numero, capitan)
    #     nuevoJugador.setId(id)
    #     nuevoJugador.setLesion(lesiones)
    #     nuevoJugador.setTitular(titular)
    #
    #     return nuevoJugador

    def editarJugador(self, jugador):
        self.equipo.editarJugador(jugador)

    def borrarJugador(self, jugador):
        self.equipo.borrarJugador(jugador.getId())

    def insertarRival(self, rival: {}):
        nombre = rival.get("nombre_equipo")
        entidad = rival.get("nombre_entidad")
        categoria = rival.get("categoria")
        rama = rival.get("rama")
        tipo = rival.get("tipo_equipo")
        nuevoEquipo = Equipo(nombre, categoria, rama, tipo, entidad, True)
        if self.equipo.checarRivalRepetido(nuevoEquipo):
            return False
        else:
            self.equipo.insertarRival(nuevoEquipo)
            return True

    def editarRival(self, rival):
        self.equipo.editarRival(rival)

    def borrarRival(self, rival):
        self.equipo.borrarRival(rival)

    def insertarCompetencia(self, competencia: {}):
        nombre = competencia.get("nombre")
        inicio = competencia.get("fecha_inicio")
        fin = competencia.get("fecha_fin")
        activa = competencia.get("activa")
        tipo = competencia.get("id_tipo")
        nuevaCompetencia = Competencia(tipo, nombre, inicio, fin, activa)
        if self.equipo.checarCompetenciaRepetida(nuevaCompetencia):
            return False
        else:
            self.equipo.insertarCompetencia(nuevaCompetencia)
            return True

    def editarCompetencia(self, competencia):
        self.equipo.editarCompetencia(competencia)

    def borrarCompetencia(self, competencia):
        self.equipo.borrarCompetencia(competencia)

    def getCompetencias(self):
        return self.equipo.getCompetencias()

    def getPruebas(self):
        return self.equipo.getPruebasFisicas()

    def getRivales(self):
        return self.equipo.getRivales()

    def getJugadoresContrarios(self, equipoBuscado: Equipo):
        for equipo in self.equipo.getRivales():
            if equipo.getNombre() == equipoBuscado.getNombre():
                return equipo.getJugadores()

    def obtenerCompetenciaPorNombre(self, nombre):
        return self.equipo.obtenerCompetenciaPorNombre(nombre)

    def insertarPartido(self, partido: {}):
        id = partido.get("id")
        idCompetencia = partido.get("id_competencia")
        idContrario = partido.get("id_contrario")
        idPropio = partido.get("id_equipo")
        resultado = partido.get("resultado")
        ubiacion = partido.get("ubicacion")
        fecha = partido.get("fecha")
        nuevoPartido = Partido(idPropio, idContrario,idCompetencia, ubiacion, fecha)
        nuevoPartido.setId(id)
        self.equipo.insertarPartido(nuevoPartido)

    @classmethod
    def getJugadoresEquipo(cls, equipo):
        return Equipo.getJugadores(equipo)
