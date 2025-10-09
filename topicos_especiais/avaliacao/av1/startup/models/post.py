from datetime import datetime
from models.usuario import Usuario

class Post:
    def __init__(self, data_hora:datetime , conteudo:str, usuario: Usuario, id:int= None, midia:str=None):
        self.data_hora = data_hora
        self.conteudo = conteudo
        self.midia = midia
        self.ususario = usuario
        self.id = id
        