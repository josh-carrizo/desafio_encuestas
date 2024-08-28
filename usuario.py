from listado_respuestas import ListadoRespuestas

class Usuario():
    def __init__(self, correo: str, edad: int, region: int):
        self._correo = correo
        self._edad = edad
        self._region = region
    
    @property
    def correo(self):
        return self._correo
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def region(self):
        return self._region
    
    def ContestarEncuesta(self, encuesta):
        listado_respuestas = ListadoRespuestas(self, [])
        encuesta.AgregarListadoRespuestas(listado_respuestas)