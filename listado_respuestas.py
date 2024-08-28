
class ListadoRespuestas:
    def __init__(self, usuario, respuestas):
        self._usuario = usuario
        self._respuestas = respuestas
    
    @property
    def usuario(self):
        return self._usuario
    
    @property
    def respuestas(self):
        return self._respuestas
    
    def MostrarListado(self):
        return f'Usuario: {self._usuario.correo}\nRespuestas: {self._respuestas}'
