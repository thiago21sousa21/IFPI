from models import Post, Usuario
from datetime import datetime

class Comentario:
    def __init__(self, conteudo:str, post:Post, usuario:Usuario, data_hora:datetime = None, id:int = None):
        self.data_hora = data_hora
        self.conteudo = conteudo
        self.post = post
        self.usuario = usuario
        self.id = id