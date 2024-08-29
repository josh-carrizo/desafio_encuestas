from alternativa import Alternativa as a

class Pregunta():
   
    def __init__(self, enunciado_pregunta:str, ayuda_alternativa:str, indicacion_requerida:False, alternativas):
        self._enunciado_pregunta = enunciado_pregunta
        self._ayuda_alternativa = ayuda_alternativa
        self._indicacion_requerida = indicacion_requerida
        self._alternativas = alternativas if alternativas else []
        
    @property 
    def enunciado_pregunta(self):
        return self._enunciado_pregunta
    @property
    def ayuda_alternativa(self):
        return self._ayuda_alternativa     
    @property
    def indicacion_requerida(self):
        return self._indicacion_requerida     
    @property
    def alternativas(self):
        return self._alternativas     
    
def MostrarPregunta(self):
    retorno = f'Pregunta: {self._enunciado_pregunta}\n'
    if self._ayuda_alternativa:
        retorno = retorno + f'Aiuda: {self._ayuda_alternativa}\n'
        print(retorno)
    for a in self._alternativas:
        retorno = retorno + f'{a.MostrarAlternativa()}\n'
        print(retorno)
    return retorno