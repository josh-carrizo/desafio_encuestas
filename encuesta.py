from pregunta import Pregunta
from usuario import Usuario
from listado_respuestas import ListadoRespuestas


class Encuesta:
    def __init__(self, nombre:str):
        self._nombre = nombre
        self._preguntas = []
        self._listados_respuestas = []
    @property
    def nombre(self):
        return self._nombre    

    def nombre(self, NuevoNombre:str):
        self._nombre = NuevoNombre
        
    def AgregarPregunta(self, pregunta:Pregunta):
        self._preguntas.append(pregunta)    

    def Mostrar(self):
        resultado = f"Encuesta: {self._nombre}\n"
        for pregunta in self._preguntas:
            resultado = resultado + pregunta.MostrarPregunta() + "\n"
        return resultado
    
    def AgregarListadoRespuestas(self, listado_respuestas: ListadoRespuestas):
        self._listados_respuestas.append(listado_respuestas)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edad_minima: 18, edad_maxima: 96):
        Encuesta.__init__(self, nombre)  
        self._edad_minima = edad_minima
        self._edad_maxima = edad_maxima
    
    @property
    def edad_minima(self):
        return self._edad_minima
    
    def edad_minima(self, edad_minima: int):
        self._edad_minima = edad_minima
    
    @property
    def edad_maxima(self):
        return self._edad_maxima
    
    def edad_maxima(self, edad_maxima: int):
        self._edad_maxima = edad_maxima

    def AgregarListadoRespuestas(self, listado_respuestas: ListadoRespuestas):
        if self._edad_minima <= listado_respuestas.usuario.edad <= self._edad_maxima:
            Encuesta.AgregarListadoRespuestas(self, listado_respuestas) 

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, regiones: list):
        Encuesta.__init__(self, nombre) 
        self._regiones = regiones
    
    @property
    def regiones(self):
        return self._regiones

    def regiones(self, regiones: list):
        self._regiones = regiones

    def AgregarListadoRespuestas(self, listado_respuestas: ListadoRespuestas):
        if listado_respuestas.usuario.region in self._regiones:
            Encuesta.AgregarListadoRespuestas(self, listado_respuestas) 