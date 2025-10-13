from datetime import datetime
from models.post import Post
from models.usuario import Usuario

class Like:
    def __init__(self, post:Post, usuario:Usuario, id:int = None, data_hora:datetime = None):
        self.post = post
        self.usuario = usuario
        self.id = id
        self.data_hora = data_hora
        