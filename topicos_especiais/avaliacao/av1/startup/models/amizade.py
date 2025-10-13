from models.usuario import Usuario
from datetime import datetime

class Amizade:
    def __init__(self, usuario1: Usuario, usuario2:Usuario, data_hora:datetime = None):
        self.usuario1 = usuario1
        self.usuario2 = usuario2
        self.data_hora = data_hora

    