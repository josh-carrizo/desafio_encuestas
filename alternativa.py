class Alternativa():
    
    def __init__(self, contenido_alternativa:str, ayuda_alternativa:str):
        self._contenido_alternativa = contenido_alternativa
        self._ayuda_alternativa = ayuda_alternativa
        
    @property
    def contenido_alternativa(self):
        return self._contenido_alternativa
    @property
    def ayuda_alternativa(self):
        return self._ayuda_alternativa     
    
    def MostrarAlternativa(self):
        if self._ayuda_alternativa:
            return f'{self._contenido_alternativa}\t (Aiuda: {self._ayuda_alternativa})'
        return self._ayuda_alternativa
    