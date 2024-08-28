from encuesta import Encuesta, EncuestaLimitadaEdad, EncuestaLimitadaRegion
from pregunta import Pregunta
from alternativa import Alternativa
from usuario import Usuario
from listado_respuestas import ListadoRespuestas

def main():
    alternativa1 = Alternativa("Opción 1", "Esta es la primera opción")
    alternativa2 = Alternativa("Opción 2","Sin ayuda")
    
    pregunta = Pregunta("¿Cuál es tu color favorito?", "Por favor, elige uno", True, [alternativa1, alternativa2])
    
    encuesta = Encuesta("Encuesta de Preferencias de Color")
    encuesta.AgregarPregunta(pregunta)
    
    usuario = Usuario("usuario@example.com", 25, 1)
    
    listado_respuestas = ListadoRespuestas(usuario, [1])
    
    encuesta.AgregarListadoRespuestas(listado_respuestas)
    
    print(encuesta.Mostrar())

    encuesta_edad = EncuestaLimitadaEdad("Encuesta para Adultos", 18, 99)
    encuesta_edad.AgregarPregunta(pregunta)
    
    encuesta_edad.AgregarListadoRespuestas(listado_respuestas)
    
    print(encuesta_edad.Mostrar())
    
    encuesta_region = EncuestaLimitadaRegion("Encuesta Regional", [1, 2])
    encuesta_region.AgregarPregunta(pregunta)
    
    encuesta_region.AgregarListadoRespuestas(listado_respuestas)
    
    print(encuesta_region.Mostrar())

if __name__ == "__main__":
    main()
